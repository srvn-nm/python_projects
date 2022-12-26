Q1 = "SELECT Student.Sname, Student.Sfamily, Student.city, College.clg_name FROM Student INNER JOIN College ON Student.#clg = College.#clg WHERE Student.city != College.city"
Q2 = "SELECT Proof.Pname, Proof.Pfamily FROM Proof INNER JOIN Sec INNER JOIN Course ON Proof.#P = Sec.#P and Course.#C = Sec.#C WHERE Course.Cname = 'database' and Sec.term = 1 and Sec.year = 1401"
