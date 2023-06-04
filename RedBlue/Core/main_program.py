import asyncio
import random
from datetime import datetime, timedelta
import redis
from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer
from django.db.models import Sum

from Core.models import Stavka

redis_client = redis.Redis(host="localhost", port=6379, db=0)

async def main_casino_worker():
    with redis.Redis() as redis_client:  # по дефолту там хост локал хост а порт 6379
        channel_layer = get_channel_layer()
        while True:
            redis_client.set("access_for_make_stavka", "on")
            start_resulting = datetime.now() + timedelta(seconds=30)
            redis_client.set(name="time", value=(start_resulting.minute * 60 + start_resulting.second))
            while datetime.now() < start_resulting:
                await asyncio.sleep(1)

            await channel_layer.group_send(
                'room_auction',
                {
                    'type': 'Send.auction.start',
                    'state': "wait"
                }
            )
            redis_client.set("access_for_make_stavka", "off")

            red_stavka = await sync_to_async(Stavka.objects.filter)(color="r")
            red_money = await sync_to_async(red_stavka.aggregate)(Sum('quantity'))
            blue_stavka = await sync_to_async(Stavka.objects.filter)(color="b")
            blue_money = await sync_to_async(blue_stavka.aggregate)(Sum('quantity'))
            if red_money["quantity__sum"]==None:
                red_money = 0
            else:
                red_money = int(red_money["quantity__sum"])
            if blue_money["quantity__sum"]==None:
                blue_money = 0
            else:
                blue_money = int(blue_money["quantity__sum"])

            winner_color = 0
            if blue_money<red_money:
                winner_color = "b"
            if red_money<blue_money:
                winner_color = "r"
            if red_money==blue_money:
                r = random.randint(0,1)
                if r==0:
                    winner_color="r"
                else:
                    winner_color="b"


            all_stavka = await sync_to_async(Stavka.objects.all)()
            await stav1(all_stavka,winner_color)

            delete = await sync_to_async(Stavka.objects.all)()
            await sync_to_async(delete.delete)()
            await asyncio.sleep(1)
            await channel_layer.group_send(
                'room_auction',
                {
                    'type': 'Send.winner.color',
                    'color': winner_color
                }
            )
            await asyncio.sleep(5)
            await channel_layer.group_send(
                'room_auction',
                {
                    'type': 'Send.auction.start',
                    'state': "start"
                }
            )

@sync_to_async
def stav1(all_stavka, winner_color):

    for stavka in all_stavka:
        if stavka.color == winner_color:
            stavka.owner_id.balance += stavka.quantity
            stavka.owner_id.save()
        else:
            stavka.owner_id.balance -= stavka.quantity
            stavka.owner_id.save()

def time_round():
    start_resulting = int(redis_client.get("time"))
    round_time = start_resulting - (datetime.now().minute * 60 + datetime.now().second)

    return round_time - 1

