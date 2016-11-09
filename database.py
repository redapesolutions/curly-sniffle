import pymysql
import pymysql.cursors

### super secret credentials ###
host = 'localhost'
user = 'root'
password = '199072zhuma'
db = 'lumberjack'
charset = 'utf8mb4'

conn = pymysql.connect(host=host,user=user,password=password,db=db,charset=charset,cursorclass=pymysql.cursors.DictCursor)
db_cursor = conn.cursor()	


def get_all_users():
	sql = "SELECT * FROM `lj_users`;"
	db_cursor.execute(sql)
	result = db_cursor.fetchone()
	print(result)

def get_user_by_id(id):
	sql = "SELECT * FROM `lj_users` WHERE id = {};".format(id)
	db_cursor.execute(sql)
	result = db_cursor.fetchone()
	print(result)

def create_user(user):
	try:
		with conn.cursor() as cursor:
			# Create a new record
			sql = "INSERT INTO `lj_users` (`name`, `email`, `password`) VALUES (%s, %s, %s)"
			cursor.execute(sql, (user.name, name.email, name.password))
		# conn is not autocommit by default. So you must commit to save
		# your changes.
		conn.commit()

		with conn.cursor() as cursor:
			# Read a single record
			sql = "SELECT `id`, `password` FROM `lj_users` WHERE `email`=%s"
			cursor.execute(sql, (user.email))
			result = cursor.fetchone()
			print(result)
	finally:
		conn.close()