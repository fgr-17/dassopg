select *
from Users u 
inner join Jobs j on (u.idJob == j.idJob) 
inner join AccessLogs a on (u.idUser == a.idUser)
where (j.description = "Gerente") and (a.inOut = 1)
order by u.idUser, a.timestamp desc