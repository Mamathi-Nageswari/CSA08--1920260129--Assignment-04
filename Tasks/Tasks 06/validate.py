"""fest.validate - parse a line and check the e-mail using string methods only."""


class BadRegistration(Exception):
    """Raised when a registration line cannot be accepted."""


def valid_email(email):
    if email.count("@") != 1 or " " in email:
        return False
    user, domain = email.split("@")
    return bool(user) and "." in domain and not domain.startswith(".") and not domain.endswith(".")


def parse(line):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 5:
        raise BadRegistration(f"expected 5 fields, found {len(parts)}")
    reg, name, dept, email, events = parts
    if not (reg.isdigit() and len(reg) == 9):
        raise BadRegistration(f"bad register number {reg!r}")
    if not valid_email(email):
        raise BadRegistration(f"invalid e-mail {email!r}")
    events = [e.strip() for e in events.split(";") if e.strip()]
    if not events:
        raise BadRegistration("no events chosen")
    return {"reg": reg, "name": name, "dept": dept, "email": email.lower(), "events": events}
