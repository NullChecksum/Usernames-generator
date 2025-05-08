import itertools

def generate_usernames(name=None, surname=None, birth_year=None):
    if not name and not surname:
        return []

    name = name.lower() if name else ""
    surname = surname.lower() if surname else ""

    symbols = ["", ".", "_", "-"]
    base_patterns = set()

    name_parts = [name, name[:3], name[0]] if name else []
    surname_parts = [surname, surname[:3], surname[0]] if surname else []

    for np in name_parts:
        for sp in surname_parts:
            for sym in symbols:
                base_patterns.add(f"{np}{sym}{sp}")
                base_patterns.add(f"{sp}{sym}{np}")

    if name and surname:
        base_patterns.update([
            f"{surname}{name}",
            f"{name}{surname}",
            f"{surname[:3]}{name}",
            f"{name[:3]}{surname}",
            f"{surname[0]}{name}",
            f"{name}{surname[0]}",
            f"{name[0]}{surname}",
            f"{name[:3]}{surname[:3]}",
            f"{surname[:3]}_{name[:3]}"
        ])
    elif name:
        base_patterns.update([
            f"{name}",
            f"{name}_user"
        ])
    elif surname:
        base_patterns.update([
            f"{surname}",
            f"{surname}_user"
        ])

    if birth_year:
        suffixes = [str(birth_year), str(birth_year)[-2:]]
    else:
        suffixes = [str(y) for y in range(1970, 2027)] + [str(y)[-2:] for y in range(1970, 2027)]

    usernames = set()
    for base in base_patterns:
        usernames.add(base)
        for s1 in suffixes:
            usernames.add(f"{base}{s1}")
            for s2 in ["", s1]:
                usernames.add(f"{base}{s1}{s2}")

    return sorted(usernames)


def output_usernames(usernames, save_to_file=False, as_email=False, email_domain=None, file_prefix="output"):
    final_output = usernames
    if as_email and email_domain:
        final_output = [f"{u}@{email_domain}" for u in usernames]

    for u in final_output:
        print(u)

    if save_to_file:
        filename = f"{file_prefix}.txt"
        with open(filename, 'w') as f:
            for u in final_output:
                f.write(u + "\n")
        print(f"\nOutput saved to '{filename}'")


def process_single():
    name = input("First name: ").strip()
    surname = input("Last name: ").strip()
    birth = input("Birth year (optional): ").strip()
    birth_year = int(birth) if birth.isdigit() else None

    usernames = generate_usernames(name or None, surname or None, birth_year)

    save = input("Do you want to save to TXT file? (y/n): ").strip().lower() == "y"
    as_email = input("Do you want to generate emails? (y/n): ").strip().lower() == "y"
    domain = input("Enter email domain (e.g. gmail.com): ").strip() if as_email else None

    print(f"\nGenerated {len(usernames)} usernames:\n")
    output_usernames(usernames, save_to_file=save, as_email=as_email, email_domain=domain, file_prefix=f"{name}_{surname or 'user'}")


def process_list(filename):
    try:
        with open(filename, 'r') as f:
            for i, line in enumerate(f, start=1):
                parts = [x.strip() for x in line.strip().split(",")]
                name = parts[0] if len(parts) > 0 and parts[0] else None
                surname = parts[1] if len(parts) > 1 and parts[1] else None
                birth_year = int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else None

                print(f"\nUser {i}: {name or ''} {surname or ''}")
                usernames = generate_usernames(name, surname, birth_year)

                save = input("Save output to file for this user? (y/n): ").strip().lower() == "y"
                as_email = input("Generate emails for this user? (y/n): ").strip().lower() == "y"
                domain = input("Email domain (e.g. gmail.com): ").strip() if as_email else None

                output_usernames(usernames, save_to_file=save, as_email=as_email, email_domain=domain, file_prefix=f"{name}_{surname or 'user'}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")


mode = input("Generate for a single user or from list? (single/list): ").strip().lower()
if mode == "list":
    file_path = input("Enter filename (e.g. users.txt): ").strip()
    process_list(file_path)
else:
    process_single()
