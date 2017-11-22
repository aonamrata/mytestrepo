## Simple flask app:
http://flask.pocoo.org/docs/0.12/quickstart/#routing
```
$ cd mytestrepo/
$ virtualenv env
$ source env/Scripts/activate
$ pip install -r requirements.txt
$ python handler.py
```

## Think
    Docker container - process in background 
    Docker image - like github repo or an application installed
    docker build - is like compiling and commiting to github
    docker run - like python xxx.py 


## Docker 2.0
Intro: https://youtu.be/Q5POuMHxW-0
- Developer worry about inside the box and ops/cloud team need to worry about outside the box.

## Basic Commands:
```
docker ps 
docker images -- file system state/tarball that you want to run. You exec processes inside those iamges.
docker run -i image1 /bin/bash -- start a container
in another shell docker ps 
docker diff <psid>
docker commit <psid> <to_path>
```

### Example:
A container is a runnable instance of an image. 
 If the image 'busybox' is not present, then docker will attempt to fetch an image named 'busybox' from the public Docker hub.
```
$ docker run alpine ls -l          https://github.com/docker/labs/blob/master/beginner/chapters/alpine.md#11-docker-run
$ docker run -it alpine /bin/sh     -it flags attaches us to an interactive tty in the container
     / # python --version
        /bin/sh: python: not found
    with 
     > docker container ls 
     > docker diff 9ddb1cdc6eed
```     
     
     

## Alpine: https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Packages_and_Repositories
```
-bash-4.2$ docker run -it alpine:3.5 /bin/sh     -it flags attaches us to an interactive tty in the container
    / # python --version
    / # apk update
    / # apk add --update py2-pip
```

## Python 3.6: https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md
```
-bash-4.2$ docker run -it python:3.6 /bin/sh
    # python --version
    # pip --version
    # ls /var/www/html_npatel/
        ls: cannot access /var/www/html_npatel/: No such file or directory
    ##  expose the port
    ##  run the app 
```

## Flask + Docker:
/var/www/html_npatel
/var/www/html_snimje

```
-bash-4.2$ git clone https://github.com/aonamrata/mytestrepo.git
-bash-4.2$ cd mytestrepo/
-bash-4.2$ git checkout -b flask_only
-bash-4.2$ git pull origin flask_only

-bash-4.2$ vim Dockerfile
-bash-4.2$ docker images

-bash-4.2$ docker build -t aonamrata/mytestrepo .
-bash-4.2$ docker run -p 8888:5000 --name test1 aonamrata/mytestrepo
```

### Browser:     http://box.vr.devorch.com:8888/

### Error:
docker: Error response from daemon: Conflict. The container name "/test1" is already in use by container "d2ffdbb79309fb2bf44bd4bc1030b45a9e7ada1a33f43e4104d7e0e932d34720". You have to remove (or rename) that container to be able to reuse that name.
```
        docker rm $(docker ps -qa --no-trunc --filter "status=exited")
        docker rmi $(docker images | grep "none" | awk '/ / { print $3 }')
```


# WHAT DID WE LEARN:
- Awesome not yet, just good 
- any service quick start 
- deploy with app having same port but diff exposed ports 

