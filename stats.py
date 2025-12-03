
def spilt_words(text):
    return text.split()



def char_counter(text):
    counter = {}
    words = text.split()   

    for word in words:
        for char in word:
            lowerCase=char.lower()
            if not lowerCase.isalpha():
                continue
            if lowerCase not in counter:
                counter[lowerCase]=1
            else:
                counter[lowerCase]+=1
    return counter

def sort_counter(counter):
    newDict=[]
    for key,value in counter.items():
        entry={}
        entry["char"]=key
        entry["num"]=value
        newDict.append(entry)
    newDict.sort(reverse=True,key=sort_on)
    return (newDict)
def sort_on(item):
    return item["num"]


        
        

        


    
   
        
