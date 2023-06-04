from asgiref.sync import sync_to_async
from channels.layers import get_channel_layer
from django.shortcuts import redirect

from Account.models import Account
from Core.models import Stavka


async def make_stavka(data):
    color = data["color"]
    sum_for_buy = data["quantity"]
    user = data["user"]
    channel_layer = get_channel_layer()
    have_stavka = await sync_to_async(Stavka.objects.filter)(owner_id=user.id)
    if user.is_authenticated:
        if not await sync_to_async(have_stavka.exists)():
            if int(sum_for_buy) <= user.balance and int(sum_for_buy)>=25:
                await sync_to_async(Stavka.objects.create)(owner_id=user, color=color,quantity=sum_for_buy)

                await channel_layer.group_send(
                    f'user_{user.id}',
                    {
                        'type': 'Send.notification',
                        'message': "succses"
                    }
                )

            else:
                await channel_layer.group_send(
                    f'user_{user.id}',
                    {
                        'type': 'Send.notification',
                        'message': "you_havent_money"
                    }
                )
        else:
            await channel_layer.group_send(
                f'user_{user.id}',
                {
                    'type': 'Send.notification',
                    'message': "stavka_alredy_create"
                }
            )
    else:
        print("user not autorizated")

