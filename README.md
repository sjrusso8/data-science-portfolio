# Data Science Portfolio Site

[Data Science Portfolio][1] website, made with [Wagtail][2] & [Tailwindcss][3]!
## Requirements

To run this project you need the Docker engine (>=1.12.1) and the docker-compose command (>=1.8.0) installed.

To install the Docker engine on your platform see:

    https://docs.docker.com/engine/getstarted/step_one/

To install docker-compose command:

    https://docs.docker.com/compose/install/


## Getting Started

To start this Website project run this command from the root folder:

    $ docker-compose up -d --build

Migration and a user are needed so run:

    $ docker exec -it ds_django python manage.py migrate
    $ docker exec -it ds_django python manage.py createsuperuser


[1]: https://google.come/ "Data Science Portfolio"
[2]: https://wagtail.io/ "Wagtail"
[3]: https://tailwindcss.com/ "Taildwindcss"
