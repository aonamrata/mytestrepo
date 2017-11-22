mytestrepo
==========

# Mysql DB + FLASK :

```
Clone to https://github.com/aonamrata/mytestrepo/tree/mytestrepo_db
-bash-4.2$ cd /var/www/html_npatel/mytestrepo_db/db/
```

## DB on Console 1:

create a data folder in db with 777 permission:
```
    -bash-4.2$ docker build -t aonamrata/mytestrepo_db_mysql .
    -bash-4.2$ docker run -p 33061:3306 -v /var/www/html_npatel/mytestrepo_db/db/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=namrata -e MYSQL_DATABASE=docker_logs aonamrata/mytestrepo_db_mysql
```

## Check mysql on Console 2:
```
    -bash-4.2$ mysql -u root -pnamrata -h 127.0.0.1 -P 33061 docker_logs
    mysql> show databases;
    mysql>  
   CREATE TABLE `access_log` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `request_data` varchar(5000) DEFAULT NULL,
      `access_timestamp` timestamp NULL DEFAULT NULL,
      PRIMARY KEY (`id`)
    )
    mysql> insert into access_log (request_data, access_timestamp) values ('test22', '2017-11-20');
```

## Run the Flask App on Console3:
```
    -bash-4.2$ docker build -t aonamrata/mytestrepo_db_app .
    -bash-4.2$ docker run -p 8888:5000 aonamrata/mytestrepo_db_app
    To Stop mysql :
    -bash-4.2$ docker stop 746ef4e734aa
```

## Test the setup on Browser: 
    http://box.vr.devorch.com:8888/hello
