-- select *
select s.name, s.unit, st.description
from Sensors s
inner join SensorsTypes st on s.idType = st.id