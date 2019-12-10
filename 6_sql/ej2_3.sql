-- select *
select datetime(l.timestamp, 'unixepoch')
from LogSensors l
inner join Sensors s on (l.idSensor = s.idSensor)
where s.name like "%Hum%" and l.valueSensor > 50.0