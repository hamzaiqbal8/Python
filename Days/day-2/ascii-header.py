""" Build ascii_header.py – Print a stylized heading using *, =, or # """

def print_ascii_header(title, char='*', width=40):
    if width < len(title) + 4:
        width = len(title) + 4
    
    border = char * width
    
    padded_title = f"{char} {title.center(width - 4)} {char}"
  
    print(border)
    print(padded_title)
    print(border)

if __name__ == "__main__":
    print_ascii_header("Hello World", '*')
    print_ascii_header("Today", '=', 30)
    print_ascii_header("Time", '#', 20)

