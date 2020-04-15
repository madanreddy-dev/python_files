#!/usr/bin/env python
#************************************************************************************************************************
#  DEPARTMENT     : DCI - Data Center Intelligence                                                                      #
#  NAME           : hfreqn.py                                                                                           #
#  DATA DOMAIN    : ****                                                                                                #
#  FREQUENCY      : *****                                                                                               #
#  RESTARTABILITY : ****                                                                                                #
#  CONVERSION     : This script is mainly used to find N high frequency words and if there are same number of words     #
#                 : then the words will be displayed in alphabetical order and highest freq of specific word           	#
#------------------------------------------------------------------------------------------------------------------------
# MODIFICATION HISTORY                                                                                                  #
#------------------------------------------------------------------------------------------------------------------------
#  DATE        TICKET/STORY        AUTHOR                               COMMENTS                                        #
#------------------------------------------------------------------------------------------------------------------------
# 20200213                         MADAN REDDY                          Assignment                                      #
#========================================================================================================================
import sys
import re
from collections import Counter 
x = 0

class HighFrequency:


#Converts the text into lower case and splits the sentence into words by removing special characters and
#retuns N number of most frequent words from the entered text
  def calculate_most_freq_words(self,textdata,n):
      text_data = textdata
      tet_d=re.sub("[^0-9a-zA-Z']+", ' ', text_data).rstrip()
      word_split = tet_d.lower().split()
      sorted_data = sorted(Counter(word_split).most_common(n), key=lambda item: (-item[1], item[0]))
      print("Highest Frequeny words are:")
      print(sorted_data)#end execution for counting high frequency


#Converts the entered text into lower case by separating words and returns the high frequency word from the entered text
  wanted = " "
  def cal_specific_freq_word(self,textdata,wantedword):
      words_stetement = textdata
      wanted = wantedword
      tet_s=re.sub("[^0-9a-zA-Z']+", ' ', words_stetement).rstrip()
      wordlist = tet_s.lower().split()
      cnt = Counter()
      for word in wordlist:
          if word == wanted:
              cnt[word] += 1
      print (cnt)
      
      
#Validates user provided options!
  def valid_options(self,message):
     while True:
       userInput = 0
       global x
       try:
         userInput=int(input(message))
       except ValueError:
              if x!= 3:
                 x+= 1
                 print("That was not a valid input. Please enter integer value!")
              else:
                print ("Sorry, you have exceeded maximum attempts!")
                sys.exit()        

       else:
          return userInput
          break

print('T - For N number of High Frequency Words\nW - For High Frequecny word of any specific word\nE - Exit')
option=input('Please choose any of the above options:')

#HighFrequency Class is called here.
p1 = HighFrequency()


#processes the data based on the user provided inputs.
if option.lower()=='t':
    text_data = input("Enter the text for highest Frequency word(s):") 
    ncount = p1.valid_options("Enter the nth highest Frequency:")
    p1.calculate_most_freq_words(text_data,ncount)

elif option.lower()=='w':
    words_stetement = input("Enter your text:")
    wanted = input("Enter your desired word to search from the above entered text:")
    p1.cal_specific_freq_word(words_stetement,wanted)

elif option=='e' or option=='E':
    print("Thanks for using, BYE for now!")
    sys.exit()

else:
    print("That was not a Valid Option")

#end of execution!

