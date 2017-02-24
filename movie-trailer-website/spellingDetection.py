import urllip

def read_text():
    text = open("/home/nan/udacity-full-stack-course/movie-trailer-website/article/random.txt")
    article = text.read()
    print(article)
    text.close()

def check(text_to_check):
    connection = url.open("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()