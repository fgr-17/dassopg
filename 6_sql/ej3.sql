select u.idUser, u.name, u.lastname, j.description from Users u inner join Jobs j
on (u.idJob == j.idJob)
/* where (j.description == "Gerente") */