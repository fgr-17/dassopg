select l.id, max(l.valueSensor), s.name, datetime(l.timestamp, 'unixepoch', 'localtime')
from LogSensors l
inner join Sensors s on l.idSensor = s.idSensor
where s.name like "%Temp%"