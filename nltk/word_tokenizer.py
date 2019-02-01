""" this is the tokenization of any paragraph in
        word and sentence manner...
        (.) ,(!),(?) has been used for sentence tokenization and
        only "space" has been used for word tokenization
        
"""


l="this is iit ism dhanbad.Is this place nice? Hey Mr. Pritam Patel ."
alphabet_capital=['A','B','C','D','E','F','G','H',
				'I','J','K','L','M','N','O','P','Q','R','S','T',
				'U','V','W','X','Y','Z']
alphabet_small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                    'o','p','q','r','s','t','u','v','w','x','y','z']

def large(s):
    for i in alphabet_capital:
        if s==i:
            return True
    return False

def small(s):
    for i in alphabet_small:
        if i==s:
            return True
    return False

def word_tokenize(l):
    s=""
    final=[] ## the list that is to be returned..or this is the tokenized list
    flag=False
    for i in range(len(l)):
        
        if not(large(l[i]) or small(l[i])) and  flag:
            final.append(s) ## appending the value to the final tokenized array ....
            flag=False 
            s=""  ## setting the value of s to be null string so that it can store the next value of the string before .
        else:
            flag=True
            s+=l[i] ## concatenating all the values before any . is observed...
    final1=[]
    t=""
    #for i in range(len(final)):
        #for j in range(len(final[i])):
            #if final[i][j]==' ':
                #continue
            #else:
                #t+=final[i][j]
        #final1.append(t)
        
    #return final1
    return final


def sentence_tokenizer(l):
    s=""
    final=[]
    for i in l:
        if i=='.' or i=='?' or i=='!' or i=='\n':
            final.append(s)
            s=""
        else:
            s+=i
    return final

        

para="A complete sentence has at least a subject\n and a main verb to state (declare) a complete thought. Short example: Walker walks. A subject is the noun that is doing the main verb. The main verb is the verb that the subject is doing. In English and many other languages, the first word of a written sentence has a capital letter. At the end of the sentence there is a full stop or full point (American: 'period')."
print(sentence_tokenizer(l))
print(word_tokenize(l))
for i in range(3):
    print("")
#print(sentence_tokenizer(para))
#print(word_tokenize(para))
