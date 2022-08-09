import sys

def add_new_word(database):
	word_english = input('Please enter english word: ')
	word_persian = input('Please enter persian word: ')
	database.append({'english': word_english, 'persian': word_persian})
	return database

def english2persian(database, clause):
	sentences = clause.split('.')
	translated_list = list()
	for sentence in sentences:
		if len(sentence) < 1:
			break
		words = sentence.split(' ')
		for word in words:
			for words_database in database:
				if words_database['english'] == word:
					translated_list.append(words_database['persian'])
					break
		translated_list.append('.')
	translated = ' '.join(translated_list)
	print("translated clause is: ", translated)

def persian2english(database, clause):
	sentences = clause.split('.')
	translated_list = list()
	for sentence in sentences:
		if len(sentence) < 1:
			break
		words = sentence.split(' ')
		for word in words:
			for words_database in database:
				if words_database['persian'] == word:
					translated_list.append(words_database['english'])
					break
		translated_list.append('.')
	translated = ' '.join(translated_list)
	print("translated clause is: ", translated)

def exit(database, database_name):
	file_database = open(database_name, 'w')
	for words in database:
		file_database.write(words['english'] + ',' + words['persian'] + '\n')
	print('Exiting ....... ')
	sys.exit()

def read_database(database_name):
	file_database = open(database_name, 'r')
	database = list()
	for line in file_database:
		words = dict()
		words_list = line.split(',')
		words['english'] = words_list[0]
		words['persian'] = words_list[1].strip()
		database.append(words)
	return database

if __name__ == "__main__":
	database_name = 'database.txt' # input('Please enter name of database: ')
	print('Loading database ....... ')
	database = read_database(database_name)
	while True:
		print('1- add new word')
		print('2- translation english2persian')
		print('3- translation persian2english')
		print('4- exit')

		operation = input('Please choose your operation: ')	
		if operation == '1':
			database = add_new_word(database)
		elif operation == '2':
			clause = input('Enter your cluase: ')
			english2persian(database, clause)
		elif operation == '3':
			clause = input('Enter your cluase: ')
			persian2english(database, clause)
		elif operation == '4':
			exit(database, database_name)
		else:
			print('Wrong command')

