import tkinter as tk

#### DECIMAL CONVERSION ####
def decimal_to_binary():
    decimal_value = int(decCon_decimal_input.get())
    binary = ''
    while decimal_value > 0:
        binary = str(decimal_value % 2) + binary
        decimal_value //= 2
    decCon_binary_output.configure(text=binary)

def decimal_to_octal():
    decimal_value = int(decCon_decimal_input.get())
    octal = ''
    while decimal_value > 0:
        octal = str(decimal_value % 8) + octal
        decimal_value //= 8
    decCon_octal_output.configure(text=octal)

def decimal_to_hexadecimal():
    decimal_value = int(decCon_decimal_input.get())
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ''
    while decimal_value > 0:
        hexadecimal = hex_chars[decimal_value % 16] + hexadecimal
        decimal_value //= 16
    decCon_hexadecimal_output.configure(text=hexadecimal)

#### BINARY CONVERSION ####
def binary_to_decimal():
    binary_value = int(binCon_binary_input.get(), 2)
    binCon_decimal_output.configure(text=binary_value)

def binary_to_octal():
    binary_value = int(binCon_binary_input.get(), 2)
    octal = oct(binary_value)[2:]
    binCon_octal_output.configure(text=octal)

def binary_to_hexadecimal():
    binary_value = int(binCon_binary_input.get(), 2)
    hexadecimal = hex(binary_value)[2:]

    if(hexadecimal.isdigit() and len(hexadecimal) != 0):
        binCon_hexadecimal_output.configure(text=hexadecimal)
    else:
        binCon_hexadecimal_output.configure(text=hexadecimal.upper())

#### OCTAL CONVERSION ####
def octal_to_decimal():
    octal_value = int(octCon_octal_input.get(), 8)
    octCon_decimal_output.configure(text=octal_value)

def octal_to_binary():
    octal_value = int(octCon_octal_input.get(), 8)
    binary = bin(octal_value)[2:]
    octCon_binary_output.configure(text=binary)

def octal_to_hexadecimal():
    octal_value = int(octCon_octal_input.get(), 8)
    hexadecimal = hex(octal_value)[2:]
    
    if(hexadecimal.isdigit() and len(hexadecimal) != 0):
        octCon_hexadecimal_output.configure(text=hexadecimal)
    else:
        octCon_hexadecimal_output.configure(text=hexadecimal.upper())

#### HEXADECIMAL CONVERSION ####
def hexadecimal_to_decimal():
    hexadecimal_value = int(hexCon_hexadecimal_input.get(), 16)
    hexCon_decimal_output.configure(text=hexadecimal_value)

def hexadecimal_to_binary():
    hexadecimal_value = int(hexCon_hexadecimal_input.get(), 16)
    binary = bin(hexadecimal_value)[2:]
    hexCon_binary_output.configure(text=binary)

def hexadecimal_to_octal():
    hexadecimal_value = int(hexCon_hexadecimal_input.get(), 16)
    octal = oct(hexadecimal_value)[2:]
    hexCon_octal_output.configure(text=octal)

#### STRING TO ASCII CONVERSION ####
def string_to_ascii():
    string_value = string_input.get()
    ascii_list = []
    for char in string_value:
        ascii_list.append(ord(char))
    ascii_output.configure(text=ascii_list)


root = tk.Tk()
root.configure()
root.title("Konversi Bilangan & Konversi String to ASCII")

#### DECIMAL CONVERSION ####
decCon_decimal_title = tk.Label(root, text="Konversi Desimal", font=("Arial", 12, "bold"))
decCon_decimal_title.grid(row=0, column=0, padx=10, pady=10)

decCon_decimal_label = tk.Label(root, text="Desimal:")
decCon_decimal_label.grid(row=1, column=0, padx=10, pady=10)

decCon_decimal_input = tk.Entry(root)
decCon_decimal_input.grid(row=1, column=1, padx=10, pady=10)

decCon_binary_label = tk.Label(root, text="Biner:")
decCon_binary_label.grid(row=2, column=0, padx=10, pady=10)

decCon_binary_output = tk.Label(root, text="")
decCon_binary_output.grid(row=2, column=1, padx=10, pady=10)

decCon_binary_button = tk.Button(root, text="Convert", command=decimal_to_binary)
decCon_binary_button.grid(row=2, column=2, padx=10, pady=10)

decCon_octal_label = tk.Label(root, text="Oktal:")
decCon_octal_label.grid(row=3, column=0, padx=10, pady=10)

decCon_octal_output = tk.Label(root, text="")
decCon_octal_output.grid(row=3, column=1, padx=10, pady=10)

decCon_octal_button = tk.Button(root, text="Convert", command=decimal_to_octal)
decCon_octal_button.grid(row=3, column=2, padx=10, pady=10)

decCon_hexadecimal_label = tk.Label(root, text="Hexadesimal:")
decCon_hexadecimal_label.grid(row=4, column=0, padx=10, pady=10)

decCon_hexadecimal_output = tk.Label(root, text="")
decCon_hexadecimal_output.grid(row=4, column=1, padx=10, pady=10)

decCon_hexadecimal_button = tk.Button(root, text="Convert", command=decimal_to_hexadecimal)
decCon_hexadecimal_button.grid(row=4, column=2, padx=10, pady=10)

#### BINARY CONVERSION ####
binCon_binary_title = tk.Label(root, text="Konversi Biner", font=("Arial", 12, "bold"))
binCon_binary_title.grid(row=5, column=0, padx=10, pady=10)

binCon_binary_label = tk.Label(root, text="Biner:")
binCon_binary_label.grid(row=6, column=0, padx=10, pady=10)

binCon_binary_input = tk.Entry(root)
binCon_binary_input.grid(row=6, column=1, padx=10, pady=10)

binCon_decimal_label = tk.Label(root, text="Desimal:")
binCon_decimal_label.grid(row=7, column=0, padx=10, pady=10)

binCon_decimal_output = tk.Label(root, text="")
binCon_decimal_output.grid(row=7, column=1, padx=10, pady=10)

binCon_decimal_button = tk.Button(root, text="Convert", command=binary_to_decimal)
binCon_decimal_button.grid(row=7, column=2, padx=10, pady=10)

binCon_octal_label = tk.Label(root, text="Oktal:")
binCon_octal_label.grid(row=8, column=0, padx=10, pady=10)

binCon_octal_output = tk.Label(root, text="")
binCon_octal_output.grid(row=8, column=1, padx=10, pady=10)

binCon_octal_button = tk.Button(root, text="Convert", command=binary_to_octal)
binCon_octal_button.grid(row=8, column=2, padx=10, pady=10)

binCon_hexadecimal_label = tk.Label(root, text="Hexadesimal:")
binCon_hexadecimal_label.grid(row=9, column=0, padx=10, pady=10)

binCon_hexadecimal_output = tk.Label(root, text="")
binCon_hexadecimal_output.grid(row=9, column=1, padx=10, pady=10)

binCon_hexadecimal_button = tk.Button(root, text="Convert", command=binary_to_hexadecimal)
binCon_hexadecimal_button.grid(row=9, column=2, padx=10, pady=10)

#### OCTAL CONVERSION ####
octCon_octal_title = tk.Label(root, text="Konversi Oktal", font=("Arial", 12, "bold"))
octCon_octal_title.grid(row=0, column=5, padx=10, pady=10)

octCon_octal_label = tk.Label(root, text="Oktal:")
octCon_octal_label.grid(row=1, column=5, padx=10, pady=10)

octCon_octal_input = tk.Entry(root)
octCon_octal_input.grid(row=1, column=6, padx=10, pady=10)

octCon_decimal_label = tk.Label(root, text="Desimal:")
octCon_decimal_label.grid(row=2, column=5, padx=10, pady=10)

octCon_decimal_output = tk.Label(root, text="")
octCon_decimal_output.grid(row=2, column=6, padx=10, pady=10)

octCon_decimal_button = tk.Button(root, text="Convert", command=octal_to_decimal)
octCon_decimal_button.grid(row=2, column=7, padx=10, pady=10)

octCon_binary_label = tk.Label(root, text="Biner:")
octCon_binary_label.grid(row=3, column=5, padx=10, pady=10)

octCon_binary_output = tk.Label(root, text="")
octCon_binary_output.grid(row=3, column=6, padx=10, pady=10)

octCon_binary_button = tk.Button(root, text="Convert", command=octal_to_binary)
octCon_binary_button.grid(row=3, column=7, padx=10, pady=10)

octCon_hexadecimal_label = tk.Label(root, text="Hexadesimal:")
octCon_hexadecimal_label.grid(row=4, column=5, padx=10, pady=10)

octCon_hexadecimal_output = tk.Label(root, text="")
octCon_hexadecimal_output.grid(row=4, column=6, padx=10, pady=10)

octCon_hexadecimal_button = tk.Button(root, text="Convert", command=octal_to_hexadecimal)
octCon_hexadecimal_button.grid(row=4, column=7, padx=10, pady=10)

#### HEXADECIMAL CONVERSION ####
hexCon_hexadecimal_title = tk.Label(root, text="Konversi Hexadesimal", font=("Arial", 12, "bold"))
hexCon_hexadecimal_title.grid(row=5, column=5, padx=10, pady=10)

hexCon_hexadecimal_label = tk.Label(root, text="Hexadesimal:")
hexCon_hexadecimal_label.grid(row=6, column=5, padx=10, pady=10)

hexCon_hexadecimal_input = tk.Entry(root)
hexCon_hexadecimal_input.grid(row=6, column=6, padx=10, pady=10)

hexCon_decimal_label = tk.Label(root, text="Desimal:")
hexCon_decimal_label.grid(row=7, column=5, padx=10, pady=10)

hexCon_decimal_output = tk.Label(root, text="")
hexCon_decimal_output.grid(row=7, column=6, padx=10, pady=10)

hexCon_decimal_button = tk.Button(root, text="Convert", command=hexadecimal_to_decimal)
hexCon_decimal_button.grid(row=7, column=7, padx=10, pady=10)

hexCon_octal_label = tk.Label(root, text="Oktal:")
hexCon_octal_label.grid(row=8, column=5, padx=10, pady=10)

hexCon_octal_output = tk.Label(root, text="")
hexCon_octal_output.grid(row=8, column=6, padx=10, pady=10)

hexCon_octal_button = tk.Button(root, text="Convert", command=hexadecimal_to_octal)
hexCon_octal_button.grid(row=8, column=7, padx=10, pady=10)

hexCon_binary_label = tk.Label(root, text="Biner:")
hexCon_binary_label.grid(row=9, column=5, padx=10, pady=10)

hexCon_binary_output = tk.Label(root, text="")
hexCon_binary_output.grid(row=9, column=6, padx=10, pady=10)

hexCon_binary_button = tk.Button(root, text="Convert", command=hexadecimal_to_binary)
hexCon_binary_button.grid(row=9, column=7, padx=10, pady=10)

#### STRING TO ASCII CONVERSION ####
string_title = tk.Label(root, text="Konversi String to ASCII", font=("Arial", 12, "bold"))
string_title.grid(row=10, column=0, padx=10, pady=10)

string_label = tk.Label(root, text="String:")
string_label.grid(row=11, column=0, padx=10, pady=10)

string_input = tk.Entry(root)
string_input.grid(row=11, column=1, padx=10, pady=10)

ascii_label = tk.Label(root, text="ASCII:")
ascii_label.grid(row=12, column=0, padx=10, pady=10)

ascii_output = tk.Label(root, text="")
ascii_output.grid(row=12, column=1, padx=10, pady=10)

ascii_button = tk.Button(root, text="Convert", command=string_to_ascii)
ascii_button.grid(row=12, column=2, padx=10, pady=10)

root.mainloop()