# Космический Инстаграм
Этот проект поможет вам скачать фотографии с сайтов [spacexdata.com](https://api.spacexdata.com/v3/launches/99) и [hubblesite.org](http://hubblesite.org/api/v3/images?page=all&collection_name=spacecraft). Также при желании вы можете выложить скаченные фотографии в инстаграм.
## Как установить
Для запуска программы необходим Python версии 3.7. В него установите зависимости командой   `pip install -r requirements.txt`
  
Чтобы скачать фотографии с сайта [spacexdata.com](https://api.spacexdata.com/v3/launches/99), перейдите в файл "fetch_spacex.py" и запустите его. Скаченные фотографии будут находиться в папке "images". 
 
Чтобы скачать фотографии с сайта [hubblesite.org](http://hubblesite.org/api/v3/images?page=all&collection_name=spacecraft), перейдите в файл "fetch_hubble.py" и запустите его. Скаченные фотографии будут находиться в папке "images". 
 
Чтобы выложить в инстаграм все скаченные фотографии откройте файл "publish_images" и запустите его. Фотографии будут размещены на этом аккаунте [spacemongoose](https://www.instagram.com/spacemongoose/).
## Переменные окружения
* **LOGIN** - логин от instagram аккаунта, на ктороый будут выкладываться фотграфии  
* **PASSWORD** - пароль от instagram аккаунта, на ктороый будут выкладываться фотграфии  
* **IMAGES_FOLDER** - путь до папки, в которую будут сохраняться фотографии
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/).
