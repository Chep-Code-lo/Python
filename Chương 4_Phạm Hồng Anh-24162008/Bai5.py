def check_pass(password):
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
def main():
    password = input()
    if check_pass(password):
        print("Mật khẩu bảo mật cao")
    else:
        print("Mật khẩu không bảo mật cao")
if __name__ == "__main__":
    main()