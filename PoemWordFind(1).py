f = open("poems.txt")

content = f.read()

if("twinkle" in content):
    print("The Word twinkle IS Present In The Content")

else:
    print("The Word twinkle Is NOT Present In The Content")

Warning