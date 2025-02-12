#!/bin/sh

until mysql -h db -u user -ppassword -e 'SELECT 1'; do
  echo "Ожидание запуска базы данных..."
  sleep 2
done

echo "База данных запущена!"