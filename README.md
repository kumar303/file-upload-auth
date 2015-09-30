Run this to build and start the container(s):

    docker-compose up -d

Find your IP somehow (maybe like this):

    $ boot2docker ip
    192.168.59.103

Open the site at `http://192.168.59.103:8000/`

Run this to get a shell:

    docker-compose run web bash
