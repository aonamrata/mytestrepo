#!/bin/bash

echo ""
echo Creating Database
echo ""
echo MYSQL: $(which mysql)
echo PHP: $(which php)
echo ""
echo ""
$ mysql -h "localhost" -u "root" "-psupersecure" < "queries.sql"
