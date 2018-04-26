## Налаштування середи розробки

Для локальної розробки простіше усього використовувати [Vagrant](https://www.vagrantup.com/downloads.html) + [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

 > інструмент дозволяє зменшити час початкового налаштування середи розробки відносно незалежно від того, яка система використовується у якості хоста. Іншим плюсом є досягнення максимальної одноманітності середи розробки у команди.

### Створення та запуск "гостьової" віртуальної машини
Vagrant використовує підготовлений (з попередньо встановленими і сконфігурованим програмними інструментами) `бокс` (`box`), який періодично оновлюється.

Vagrantfile містить конфігурацію з якою бокс запускається.

Наразі за основу використовується бокс на основі Ubuntu (`ubuntu/xenial64`).

Для початку роботи можна створити нову директорію для майбутнього проекту на хост-машині:

```
mkdir prozorro_sale_project
cd prozorro_sale_project
```

 В дану директорію склонувати репозиторій з білдаутом для локальної розробки (див.[Інструменти розробки])

```
git clone https://github.com/prozorro-sale/openprocurement.buildout
```

Поруч із склонованим репозиторієм покласти Vagrantfile:

```
curl -O https://raw.githubusercontent.com/raccoongang/openprocurement.auctions.dgf/vagrant_setup/Vagrantfile
```

Запустити розгортання боксу:

```
vagrant up
```

> Vagrant завантажить бокс із сховища, проімпортує для подальшого використання, а також створить віртуальну машину (ВМ) на основі боксу.

> **Альтернативно:** у разі наявності завантаженого файлу образу (`prozorro_sale_dev.box`) можна локально додати образ (`vagrant add -h`), і на основі нього створити віртуальну машину.

> ВМ потребує певний час для старту

Далі можна перевірити стан ВМ:

```
vagrant status
```

### Робота з віртуальною машиною

ВМ повинна бути запущена.

> Після запуску директорія проекту (в якій знаходиться Vagrantfile) автоматично доступна на ВМ як `\vagrant` і належить користувачеві `api_service`.

Під'єднуємось до ВМ через `ssh`:

```
vagrant ssh
```

> на поточному етапі потрібно ввести пароль 'ubuntu' (TBD: спростити до стандартної конфігурації з несекьюрними ключами)

Переходимо в користувача `api_service`:

```
sudo -iu api_service
cd /vagrant/openprocurement.buildout
```

Міняємо гілку git на необхідну (наприклад, `production`):

> на момент написання робочою є гілка `ea2_master`

```
git checkout production
```

Для побудови проекту необхідний конфігураційний файл (копіюємо зі зразка):

```
cp buildout.cfg.example buildout.cfg
```

Запускаємо побудову проекта:
(використовується [bildout](http://www.buildout.org/en/latest/contents.html))

```
python bootstrap.py
bin/buildout -N
```

Наразі, середа розробки підготовлена.

### Запуск сервісів

Для запуску процесів використовується [Circus](http://circus.readthedocs.io/en/latest/):

```
bin/circusd --daemon
```

Сервіс API запускається через [pserve](https://docs.pylonsproject.org/projects/pyramid/en/latest/pscripts/pserve.html):

```
bin/pserve etc/openprocurement.api.ini
```

> API доступний на хост-машині по `192.168.50.5:6543` (див. [Робота з API під час розробки])

### Запуск тестів

Можна, наприклад, запустити всі тести:

```
bin/nosetests
```

Тести також можна запускати індивідуально:
([nose](http://nose.readthedocs.io/en/latest/index.html))

```
bin/nosetests openprocurement.auctions.dgf.tests.bidder --nocapture
bin/nosetests openprocurement.auctions.dgf.tests.bidder:AuctionBidderResourceTest --nocapture -v
bin/nosetests openprocurement.auctions.dgf.tests.bidder:AuctionBidderResourceTest.test_patch_auction_bidder --nocapture -vv
```


### [Інструменти розробки]

```
# основні залежності:
python==2.7
pyramid==1.5.7          - веб-фреймворк
schematics==1.1.0       - моделі даних
cornice==1.0.0          - REST-фреймворк
CouchDB==1.0            - документна БД
Sphinx==1.3.1           - генерація документації
WebTest==2.0.18         - функціональні тести
Jinja2==2.7.3           - рендер шаблонів
```

[Vagrant](https://www.vagrantup.com/downloads.html) -  управління образами віртуальних машин...

[VirtualBox](https://www.virtualbox.org/wiki/Downloads) - провайдер віртуалізації

[bildout](http://www.buildout.org/en/latest/contents.html) - інструмент для автоматизації

[circus](http://circus.readthedocs.io/en/latest/) - менеджер процесів і сокетів

[nose](http://nose.readthedocs.io/en/latest/index.html) - розширення можливостей стандартного `unittest`

[Postman](https://www.getpostman.com/) - зручна робота з API


## [Робота з API під час розробки]

Описати інструменти для тестування, опитування існуючого програмного інтерфейсу.
