import MySQLdb


conexao_mysql = MySQLdb.connect(host = 'localhost', database = 'invest', user = 'root', password = '')

nome_aluno = 'natan'

cursor = conexao_mysql.cursor()

cursor.execute(f"INSERT INTO aluno (nome) VALUES ('{nome_aluno}')")

# cursor.execute("CREATE TABLE sextou(id int not null)")

cursor.execute('SELECT nome FROM aluno')


conexao_mysql.commit()
for b in cursor.fetchall():
    print(b)