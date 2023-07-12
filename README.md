# chatgpt export to text

A quick python script to convert chatgpt exports from json into plain text

## Why?

I want to be able to ripgrep my chatgpt chats from the command-line

## How?

Get your archive from: https://chat.openai.com/ > ... > Data Controls > Export

Then, extract the zip file that OpenAI made for you:

	$ make extract

Populate a directory named chats/ with one text file per chat:

	$ make parse

The files will be named like this:

	2023-05-24_Baltic_Dry_Index_Surge.txt
	2023-05-24_City_Time_CLI.txt
	2023-05-24_Laptops_without_Management_Engine.txt

The files also have their modified times datestamped correctly, for sorting by most recent.

## Needs 

- python3

## See also

https://github.com/daugaard47/ChatGPT_Conversations_To_Markdown
