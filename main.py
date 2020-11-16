def main(message):
    """
    A basic function to print a message to console.
    :param message: A message as a string
    :return: Whether the message was able to be printed
    """
    try:
        print(message)
    except:
        return False
    return True


if __name__ == '__main__':
    main("Hello World")