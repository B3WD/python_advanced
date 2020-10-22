class NameTooShortError(Exception):
    '''Name must be more than 4 characters'''


class MustContainAtSymbolError(Exception):
    '''Email must contain @'''
    pass


class InvalidDomainError(Exception):
    '''Domain must be one of the following: .com, .bg, .org, .net'''
    pass


def check_name(email):
    name_len = 0

    #construct name
    for char in email:
        if char == "@":
            break
        else:
            name_len += 1

    if name_len <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    else:
        return True


def check_symbol_present(email, symbol):
    if symbol in email:
        return True
    else:
        raise MustContainAtSymbolError("Email must contain @")


def check_domain(email):
    valid_domains = {".com", ".bg", ".org", ".net"}
    #check after the "."
    index = email.index(".")
    if email[index::] in valid_domains:
        return True
    else:
        raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")


while True:
    email = input()

    if (check_symbol_present(email, "@") and
        check_name(email) and
        check_domain(email)):
        print("Email is calid")