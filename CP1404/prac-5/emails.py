def extract_name(email):
    """Extracts the name from an email address."""
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name

emails = {}
while True:
    email = input('Email: ')
    if email == '':
        break
    name = extract_name(email)
    prompt = f'Is your name {name}? (Y/n) '
    choice = input(prompt).lower()
    if choice in ('', 'y'):
        emails[email] = name
    else:
        name = input('Name: ').title()
        emails[email] = name

for email, name in emails.items():
    print(f'{name} ({email})')


