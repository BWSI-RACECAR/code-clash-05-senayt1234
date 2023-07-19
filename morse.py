"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #5 - Morse Code Encryption(morse.py)


Author: Andrew Scott White

Difficulty Level: 4/10

Prompt:Sam is trying to communicate with his friend Alfie using Morse Code, but he
is tired of manually encrypting the messages. He has asked you to create a Python 
script that converts messages to Morse code and vice versa. Sam’s Morse Code key is attached below. 

Note: There is one space between characters and two spaces between words in Morse Code
Hints: 	i) You can convert a message to uppercase using  message.upper()
	ii) You can remove leading/trailing whitespace from text using text.strip()
 
 
Morse Code Key:

'A':'.-', 
'B':'-...',            
'C':'-.-.', 
'D':'-..', 
'E':'.',                    
'F':'..-.', 
'G':'--.', 
'H':'....',                    
'I':'..', 
'J':'.---', 
'K':'-.-',                    
'L':'.-..', 
'M':'--', 
'N':'-.',                    
'O':'---', 
'P':'.--.', 
'Q':'--.-',                    
'R':'.-.', 
'S':'...', 
'T':'-',                    
'U':'..-', 
'V':'...-', 
'W':'.--',                   
'X':'-..-', 
'Y':'-.--', 
'Z':'--..', 


'.':'.-.-.-',                    
'?':'..--..', 
‘!’:’-.-.--’,

'1':'.----', 
'2':'..---', 
'3':'...--',                    
'4':'....-', 
'5':'.....', 
'6':'-....',                    
'7':'--...', 
'8':'---..', 
'9':'----.',                    
'0':'-----', 

'/':'-..-.', 
'-':'-....-',         
'(':'-.--.', 
')':'-.--.-'


Test Cases:
Input: SOS Output: ...---...


Input: Hello! Output: .... . .-.. .-.. --- -.-.--


Input: HUNTER2 Output: .... ..- -. - . .-. ..---
"""


##########################################################################
# MORSE DICTIONARY
##########################################################################

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', '.':'.-.-.-', '?':'..--..', '!':'-.-.--', 
                    '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}


##########################################################################
# Function to encrypt the string
# according to MORSE_CODE_DICT
##########################################################################

class Solution:
    def encrypt(self, message):
            #type message: string
            #return type: string
            
            #TODO: Write code below to return a string with the solution to the prompt.
             message = message.upper()
             message.strip()
             for i in message:
                   for point in MORSE_CODE_DICT:
                         letter = point
                         if message[i] == letter:
                               message[i] == MORSE_CODE_DICT[letter]
                         

             return message

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.encrypt(str1)
     print(ans)

if __name__ == '__main__':
    main()
