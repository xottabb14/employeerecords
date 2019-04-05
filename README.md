# Пример системы учета посещения сотрудниками места работы посредством пинга рабочих машин.

База сотрудников хранится в файле **base.txt**. Синтаксис выглядит следующим образом: Иванов,192.168.1.228,1
* Иванов - фамилия сотрудника.
* 192.168.1.228 - ip-адрес рабочей машины
* 1 - флаг, обозначающий, что рабочая машина в сети

##### Для работы требуется:
* Python3
* Библиотека: ***pip install flask***

##### Порт можно изменить в файле ***serv.py***

##### Get-запрос осуществляется двумя способами:
* http://<host>:3309/ - выводит текущий статус рабочих машин.
* http://<host>:3309/фамилия - статистика включения/выключения рабочей машины конкретного сотрудника 