select avg(l.valueSensor), s.name
from LogSensors l
inner join Sensors s on l.idSensor = s.idSensor
where s.idType = 3