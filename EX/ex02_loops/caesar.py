"""Caesar cipher."""


def encode(message: str, shift: int) -> str:
    """
    Encode a message using a Caesar cipher.

    Presume the message is already lowercase.
    For each letter of the message, shift it forward in the alphabet by shift amount.
    If the character isn't a letter, keep it the same.

    For example, shift = 3 then a => d, b => e, z => c (see explanation below)

    Shift:    0 1 2 3
    Alphabet:       A B C D E F G H I J
    Result:   A B C D E F G H I J

    Examples:
    1. encode('i like turtles', 6) == 'o roqk zaxzrky'
    2. encode('example', 1) == 'fybnqmf'
    3. encode('the quick brown fox jumps over the lazy dog.', 7) == 'aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.'

    :param message: message to be encoded
    :param shift: shift for encoding
    :return: encoded message
    """
    encoded_message = []

    for char in message:
        if char.isalpha():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encoded_message.append(new_char)  # lisab uue tahe hulka
        # ord annab tahele numbrilise vaartuse
        # -ord('a') paneb a 0- pohisesse susteemi kus a on 0 ning otsitakse tahe char kaugust a-st naiteks c puhul on see 2
        # + shift liidab nihke orginaal tahe kaugusele a-st nt char on c ss ord(c) - ord('a') = 2 kui shift on 3 ss kokku nihe a-st on 2+3=5
        # % 26 teeb kindlaks et see jaab tahestikku nt kui esimesest tehtest on y mis on 24 ja shift 3 ss 27 % 26 on 1 ja uus taht on ss b
        # + ord('a') viib tagasi samasse nummerdamis susteemi mis enne
        # chr() muudab leitud numbri tagasi taheks

        else:
            encoded_message.append(char)  # kui nr voi tuhik jatab samaks ja lisab uue sona hulka

    return ''.join(encoded_message)  # ''.join paneb koik leitud tahed tuhikud ja nr kokku ilma ' markide ja komadeta


if __name__ == '__main__':
    print(encode("i like turtles", 6))  # -> o roqk zaxzrky
    print(encode("o roqk zaxzrky", 20))  # -> i like turtles
    print(encode("example", 1))  # -> fybnqmf
    print(encode("don't change", 0))  # -> don't change
    print(encode('the quick brown fox jumps over the lazy dog.', 7))  # -> aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.
