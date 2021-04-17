def right_justify(s) -> None:
    """Prints the string s with last character on column number 70.

    Args:
        s (str): string to be printed with last character on 70th column.
    """
    str_len = len(s)
    print(s.rjust(70, " "))


