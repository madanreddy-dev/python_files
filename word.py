import requests
import json
import sys
import re
app_id = '2a6f024e'
app_key = 'ad577d89bc9c035b97afb857acf31ed5'
language = 'en'


def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist


def Get_synonyms(word):
    synons = ""
    app_key = 'e16a33edadmsh04107f47a073893p1432a6jsn062d926bbdba'
    language = 'en'
    url = "https://webknox-words.p.rapidapi.com/words/"+ word +"/synonyms"
    headers={
     "x-rapidapi-host": "webknox-words.p.rapidapi.com",
     "x-rapidapi-key": "e16a33edadmsh04107f47a073893p1432a6jsn062d926bbdba"
     }

    synons = requests.request("GET", url, headers=headers)
    return synons.text 


def inputtext(message):
     while True:
       userInput = ""
       global x
       try:
         userInput=input(message)
         if len(userInput) > 100:
            print ("Error! Only 100 characters allowed!")
            print ("exit")
            sys.exit()
       except ValueError:
                print ("exit")
                sys.exit()        

       else:
          return userInput
          break  


# word_id = input("Enter the word for meaning:")
word_id = input("Enter the word for meaning:")
tet_data=re.sub("[^0-9a-zA-Z']+", ' ', word_id).rstrip()
word_id=' '.join(unique_list(tet_data.split()))
wordlist = word_id.lower().split()
for word in wordlist:
  try:
    url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'+ language + '/'+ word.lower()
    #url Normalized frequency
    urlFR = 'https://od-api.oxforddictionaries.com/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word.lower()
    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
    #print("code {}\n".format(r.status_code))
    y = json.loads(r.text) #filename should be the file where your json is saved
    y = y["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]
    for definition in y:
        print (word + ": " +definition)
        print("\n")
        print(Get_synonyms(word))
        print("\n")
  except :
    print(word+" is not found in dictionary!")
