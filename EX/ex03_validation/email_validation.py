"""Email validation."""


def has_at_symbol(email: str) -> bool:
    """Check if email includes a @ symbol."""
    if "@" in email:
        return True
    return False


def is_valid_username(email: str) -> bool:
    """Check if email has a valid username."""
    username = email.rsplit("@", 1)[0]  # compared to .split .rsplit splitib viimase @ juurest ("@", 1) makes sure see splitib ainult uhest kohast
    for char in username:
        if not (char.isalnum() or char == "."):
            return False
    return True


def find_domain(email: str) -> str:
    """Find the emails domain name."""
    domain = email.rsplit("@", 1)[1]
    return domain


def is_valid_domain(email: str) -> bool:
    """Check if email has a valid domain."""
    domain = find_domain(email)

    before_dot = domain.rsplit(".", 1)[0]
    after_dot = domain.rsplit(".", 1)[1]
    if domain.count(".") != 1:
        return False
    if not (3 <= len(before_dot) <= 10 and before_dot.isalpha()):
        return False
    if not (2 <= len(after_dot) <= 5 and after_dot.isalpha()):
        return False
    return True


def is_valid_email_address(email: str) -> bool:
    """Check if email has a valid email address."""
    return is_valid_username(email) and is_valid_domain(email) and has_at_symbol(email)


def create_email_address(domain: str, username: str) -> str:
    """Create a new email address."""
    email = f"{username}@{domain}"
    if is_valid_email_address(email):
        return email
    else:
        return "Cannot create a valid email address using the given parameters!"


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com", "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!
