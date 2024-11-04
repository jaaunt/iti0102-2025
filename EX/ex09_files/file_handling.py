"""Files."""

import csv


def mesh_two_list_to_csv_file(list1: list, list2: list, filename: str):
    """
    Merge two lists together into a CSV file, as if one list is on the left side and other on the right.

    Both lists have the same number of rows. Make two lists into one without disarranging any row or column.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item1, item2 in zip(list1, list2):  # zip kombineerib kaks listi ja paneb paaridena uutele ridadele
            writer.writerow([item1, item2])


def replace_vowels_in_file(input_file: str, output_file: str):
    """
    Replace all vowels in the text with an asterisk (*).

    This function finds all vowels (AEIOUaeiou) in the input text and replaces them with an asterisk (*).
    """
    with open(input_file, 'r') as file:
        text = file.read()

    vowels = "AEIOUaeiou"  # taishaalikud
    modified_text = ''.join(['*' if char in vowels else char for char in text])  # kui taishaalik ss * otherwise lic taht

    with open(output_file, 'w') as file:
        file.write(modified_text)


def reverse_rows_in_csv_file(input_file: str, output_file: str):
    """
    Reverse the order of rows in a CSV file.

    This function reads the content of an input CSV file and writes it to an
    output CSV file with the rows in reverse order.
    """
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)  # loeb koik read listiks

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reversed(rows))  # read tagurpidi


def swap_header_and_row_in_csv_file(header: list, row: list):
    """
    Swap the header row with a data row in a CSV file.

    This function takes a header row and a data row, swaps their positions,
    and writes them to a CSV file. If the data row is longer, it pads the header
    row with empty strings to match the length. The name of the output file should be "swapped_file.csv".
    """
    with open('swapped_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)  # kirjutab row esimesena
        writer.writerow(header)  # kirjutab headeri parast seda

if __name__ == '__main__':
    mesh_two_list_to_csv_file(['data1', 'data2'], ['data3', 'data4'], 'mesh_two_list_to_csv_file.csv')

    with open('mesh_two_list_to_csv_file.csv', 'r') as file:
        reader = csv.reader(file)
        output = [row for row in reader]
        for row in output:
            print(','.join(row))
    # data1,data3
    # data2,data4
    print('\n')

    with open('replace_vowels_in_file_input.txt', 'w') as file:
        file.write('Hello World')

    replace_vowels_in_file('replace_vowels_in_file_input.txt', 'replace_vowels_in_file_output.txt')

    with open('replace_vowels_in_file_output.txt', 'r') as file:
        print(file.read() + "\n")
    # "H*ll* W*rld"

    with open('reverse_rows_in_csv_file_input.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['1', '2', '3'])
        writer.writerow(['4', '5', '6'])

    reverse_rows_in_csv_file('reverse_rows_in_csv_file_input.csv', 'reverse_rows_in_csv_file_output.csv')
    with open('reverse_rows_in_csv_file_output.csv', 'r') as file:
        print(file.read())
    # 4,5,6
    # 1,2,3

    swap_header_and_row_in_csv_file(['A', 'B', 'C'], [1, 2, 3, 4])
    with open('swapped_file.csv', 'r') as file:
        print(file.read())
    # 1,2,3,4
    # A,B,C,
    import os

    os.remove('mesh_two_list_to_csv_file.csv')
    os.remove('replace_vowels_in_file_input.txt')
    os.remove('replace_vowels_in_file_output.txt')
    os.remove('reverse_rows_in_csv_file_input.csv')
    os.remove('reverse_rows_in_csv_file_output.csv')
    os.remove('swapped_file.csv')
