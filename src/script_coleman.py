hey_jude = [["Hey", "Jude" , "don't",  "make",  "it",  "bad"],
            ["Take",  "a",  "sad",  "song",  "and", "make",  "it",  "better"],
            ["Remember", "to", "let", "her", "into", "your", "heart"],
            ["Then", "you", "can", "start", "to", "make", "it", "better"],
            ["Hey", "Jude", "don't", "be", "afraid"],
            ["You", "were", "made", "to", "go", "out", "and", "get", "her"],
            ["The", "minute", "you", "let", "her", "under", "your", "skin"],
            ["Then", "you", "begin", "to", "make", "it", "better"],
            ["And", "anytime", "you", "feel", "the", "pain", "hey","Jude", "refrain"],
            ["Don't", "carry", "the", "world", "upon", "your", "shoulders"],
            ["For", "well", "you", "know", "that", "it's", "a", "fool", "who", "plays", "it", "cool"],
            ["By", "making", "his", "world", "a", "little", "colder"],
            ["Hey", "Jude", "don't", "let", "me", "down"],
            ["You", "have", "found", "her", "now", "go", "and", "get", "her"],
            ["Remember", "to", "let", "her", "into", "your", "heart"],
            ["Then", "you", "can", "start", "to", "make", "it", "better"],
            ["So", "let", "it", "out", "and", "let", "it", "in", "hey", "Jude", "begin"],
            ["You're", "waiting", "for", "someone", "to", "perform", "with"],
            ["And", "don't", "you", "know", "that", "it's", "just", "you", "hey", "Jude", "you'll", "do"],
            ["The", "movement", "you", "need", "is", "on", "your", "shoulder"],
            ["Hey", "Jude", "don't", "make", "it", "bad"],
            ["Take", "a", "sad", "song", "and", "make", "it", "better"],
            ["Remember", "to", "let", "her", "under", "your", "skin"],
            ["Then", "you'll", "begin", "to", "make", "it"],
            ["Better", "better", "better", "better", "better", "better", "oh"]]

word = 0
letter = 0
sentence = 0

for index  in range(len(hey_jude)):
    word += len(hey_jude[index])
    for index2  in range(len(hey_jude[index])):
        letter += len(hey_jude[index][index2])

sentence = len(hey_jude)
    
l = letter / (word/100)
 
s = sentence / (word/100)

cli = 0.0588 * l - 0.296 * s - 15.8

print (round(cli))