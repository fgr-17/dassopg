-- select *
select l.valueSensor, datetime(l.timestamp, 'unixepoch', 'localtime'), s.name
from LogSensors l
inner join Sensors s on (l.idSensor = s.idSensor)
inner join SensorsTypes st on (s.idType = st.id)
where st.description like "%Temp%"
order by l.timestamp desc
limit 3