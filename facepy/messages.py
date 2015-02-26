from pattern.web import *
from exceptions import *
from graph_api import *
SHORT_LIVED_ACCESS_TOKEN = 'CAACEdEose0cBALHzBRHkTZBgRUyJQfuF4OdhIrz5ZBDIeSoDACV2mhzbsTsV0SKNlxWhhmL7wHZA5s2ZBa0s6sn9ZBgeylcV5s1Rm8PJ9lxZAETJboCHqaCV0i5JGdN6IYzpk30prGbW4p5pOQbgCZBqkiv4cgzin3OYVynXElXDsd7fKOeJaBLCrl230ALvvMAiytb11rCVdvH60YwTq2RZAEEnsHguqSgZD'
#I got these two lines of code and some idea of how to access messages from arofcoding.blogspot.com/2012/10/python-script-to-fetch-messages-from.html
def messages():
	messages_list = graph.fql('SELECT snippet, snippet_author, recipients FROM thread WHERE folder_id = 0  and unread != 0 Limit 4')
	print messages_list
