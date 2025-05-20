"""contact_card.py"""

name = "Hamza Iqbal"
phone = "123-456-7890"
email = "hamza@example.com"

width = 40  

def print_centered(text):
    print(text.center(width, '-'))

print_centered("CONTACT CARD")
print_centered(name)
print_centered(phone)
print_centered(email)
print('-' * width)
