s=input("please enter a string ")
substring=0 #cannot be list if we do assignig
palindrom=[]
for i in range(len(s)):
    for j in range(i,len(s)):
        substring = s[i:j+1] #if we do concatination so every letter will add seperatly 
        if substring == substring[::-1] and len(substring)>1:
            palindrom.append(substring)
print(palindrom)


# substring + = s[i:j+1] concatination over the previous text ,substring was string
# substring  = s[i:j+1] overwrites the previous text which will be lost ,substring was string
# substring,append(s[i:j+1]) appends the new text from the end of the list ,rather than add from the start,substring was list
