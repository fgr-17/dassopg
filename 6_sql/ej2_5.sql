select s.idSensor, s.name, s.unit, st.description
from Sensors s
inner join SensorsTypes st on s.idType = st.id
where s.name like "%Temp%"