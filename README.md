# chatgtp export to text

a quick python script to convert the .json chatgpt exports into plain text

## why?

I want to be able to ripgrep all my chatgpt chats from the command-line

## how?

get your archive @ https://chat.openai.com/ > ... > Data Controls > Export

then:

	$ make extract

will extract the json from the .zip openai send

	$ make parse

will create a directory chats/ containing datestamped and titled .txt files, one per chat.

## needs 

- python3

## see also

https://github.com/daugaard47/ChatGPT_Conversations_To_Markdown
