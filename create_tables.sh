#!/bin/bash




echo Creating Database
echo ""
echo MYSQL: $(which mysql)

mysql -h localhost -u root < "/usr/src/app/queries.sql"
