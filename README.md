<h1>Интернет Казино  <img width="30px" height="30px" src="https://github.com/Musa-0/Casino-Django-Websocket-Celery/assets/87027172/c555d958-f0ab-47eb-aa6a-50f7098037d8"></h1>

<p>Для запуска сайта вам необходимо:</p>
<ul>
    <li>Создать виртуальное окружение а после скачать все зависимости с помощью pip install -r requarements.txt, или же использовать существующее виртуальное окружение</li>
    <li>Установить Postgres и создать пользователя и пароль. И указать это в setting.py, либо если лень возиться в Postgres, можно закоментировать конфиг Postgres и расскоментировать конфиг Sqlite3</li>
    <li>Установить Редис и запустить его</li>
    <li>Создать аккаунт в почте, и забить данные в settings.py для способности отправки писем. можно использовать smtp.mail.ru</li>
    <li>Запускаем сайт python3 manage.py runserver</li>
    <li>Запускаем  celery в другом терминале с помощью:</li>
        <ul>
            <li>celery -A RedBlue worker -l info</li>
            <li>celery -A RedBlue beat -l info</li>
        </ul>
    <li>Можно переходить на сайт и играть</li>
</ul>


<h3>Работа с Сайтом</h3>
<ol>
    <li>Для начала регистрируемся на сайте, а после получаем письмо на почту и переходим по ссылке в письме</li>
    <li>Далее через администратора пополняем счет игрока</li>
    <li>После этого игрок может делать ставки на игру</li>
    <li>Сайт работает через по Websocket, на стороне фронта работает js который получаем информацию о том кто победил</li>
    <li>Казино работает в режиме реального времени, у всех игроков одинаковые результаты автоматов, тем самым обмануть клиентов казино невозможно</li>
    <li>Как же зарабатывает казино?</li>
    <ul>
        <li>В казино внедрена система, благодаря которой казино будет всегда в выигрыше</li>
        <li>Люди ставят на разные слоты, и идет таймер по истечению которого будет выведен выигрышный слот</li>
        <li>Алгоритм просчитывает на какой слот поставило меньше всего игроков, и загарает именно его</li>
        <li>В таком случае, деньги большенсвта проигравший передаются победителям, а то что остается казино забирает себе</li>
    </ul>

</ol>

<h3>Внешний вид сайта</h3>

<img src="https://github.com/Musa-0/Casino-Django-Websocket-Celery/assets/87027172/de7c2b9f-3360-4d3e-a7d5-11fce536c240" width="800" height="400">
<img src="https://github.com/Musa-0/Casino-Django-Websocket-Celery/assets/87027172/0c57c9fe-39f4-444c-887b-f72633fa29ba" width="800" height="400">


<h3>Фичи сайта</h3>
<ol>
    <li>Сайт надежно защищен от утечки информации о том какой слот выигрышный</li>
    <li>Сайт работает через Websocket</li>
    <li>Сайт использует проверку почты</li>
    <li>Сайт четко следит за тем чтобы тайминг был у всех одинаковый, и чтобы всё было в рельном времени</li>
    <li>В сайт интегрирован celery, redis, channels</li>
    <li>Работает алгоритм считающий колличество денег поставленных на оба слота, и побеждает тот на который меньше поставили</li>
    <li>В случае если почта не подтверждена, аккаунт замораживается</li>
    <li>Красивый адаптированный под телефон и Пк дизайн</li>
</ol>

<img src="https://github.com/Musa-0/Casino-Django-Websocket-Celery/assets/87027172/3bb2a622-c438-4354-a67b-23ee56deb923" width="800" height="400">
<img src="https://github.com/Musa-0/Casino-Django-Websocket-Celery/assets/87027172/ecca6579-b52b-4c71-a786-67f27a65850c" width="800" height="400">
<img src="https://github.com/Musa-0/Casino-Django-Websocket-Celery/assets/87027172/4524cfb5-d88f-43bb-a298-d363ea28a281" width="800" height="400">
