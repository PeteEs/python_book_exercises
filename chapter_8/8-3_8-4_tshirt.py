def make_shirt(size,message):
    print(f"The size of shirt should be: {size}")
    print(f"On shirt you should put text: {message}")

make_shirt("L","TikTok")
make_shirt(size = "M",message = "Youtube")

def make_shirt_2(message = "I love Python",size = "XXL"):
    print(f"The size of shirt should be: {size}")
    print(f"On shirt you should put text: {message}")

make_shirt_2()

make_shirt_2(message= "I love Python?")

make_shirt_2(size = "M")