"""
==========================================================================
 STUDENT INFORMATION MANAGEMENT SYSTEM (SIMS)
 Console-Based Program | Python 3
--------------------------------------------------------------------------
 Course : ITE 260 - Computer Programming 1 (Period 2 Project Milestone)
 School : PHINMA - Cagayan de Oro College, College of Information Technology
 Group  : Group 3 - "Academic Weapon"
 Users  : Registrar (primary user)
          Teacher (can view and search student records only)
          IT Freshmen Students (secondary users)
--------------------------------------------------------------------------
 HOW THE CODE IS ORGANIZED (independent code sections)
   SECTION 1 - Constants, scalar variables, and the record layout
   SECTION 2 - Data manipulation functions (work on the students list)
   SECTION 3 - Computation and validation functions (no printing/input)
   SECTION 4 - Terminal interface functions (all input() and print())
   SECTION 5 - Feature functions and menu control loops (while / for)
   SECTION 6 - Program entry point
==========================================================================
"""

# ==========================================================================
# SECTION 1: CONSTANTS, SCALAR VARIABLES, AND RECORD LAYOUT
# ==========================================================================

# --- Registrar account (str variables; numbers only, per system requirement) ---
REGISTRAR_USERNAME = "1001"
REGISTRAR_PASSWORD = "2026"

# --- Teacher account (str variables; numbers only, same rule as the Registrar) ---
TEACHER_USERNAME = "2001"
TEACHER_PASSWORD = "5050"

# --- System rules (int / str / list variables used in expressions) ---
MAX_LOGIN_ATTEMPTS = 3            # int: tries allowed per login
PIN_LENGTH = 4                    # int: a student PIN has exactly 4 digits
CONTACT_LENGTH = 11               # int: mobile number length (e.g., 09171234567)
CONTACT_PREFIX = "09"             # str: mobile numbers must start with this
MIN_ID_LENGTH = 4                 # int: shortest allowed Student ID
MAX_ID_LENGTH = 12                # int: longest allowed Student ID
MAX_NAME_LENGTH = 40              # int: longest allowed full name
MAX_SECTION_LENGTH = 16           # int: longest allowed section code
ALLOWED_COURSES = ["BSIT"]        # list: the system covers IT students only
ALLOWED_YEAR_LEVELS = [1]         # list: the system covers freshmen only
MAX_PLACE_LENGTH = 40             # int: longest allowed birth place
MIN_ADDRESS_LENGTH = 5            # int: shortest allowed home address
MAX_ADDRESS_LENGTH = 80           # int: longest allowed home address
MIN_BIRTH_YEAR = 1960             # int: earliest accepted birth year
MAX_BIRTH_YEAR = 2012             # int: latest accepted birth year
DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   # list: days per month (non-leap year)
NOT_PROVIDED = "Not provided"     # str: shown when a field has no saved information
LINE_WIDTH = 80                   # int: width of separator lines
LABEL_WIDTH = 32                  # int: width of the field names in the detail display

# --- Position of each field inside ONE student record (a list) ---
# A record looks like:
#   [student_id, name, course, year_level, section, contact, pin,
#    birth_date, birth_place, address, guardian_name, guardian_contact]
# (the new fields were added at the END, so the old positions did not change)
ID_POS = 0
NAME_POS = 1
COURSE_POS = 2
YEAR_POS = 3
SECTION_POS = 4
CONTACT_POS = 5
PIN_POS = 6
BIRTHDATE_POS = 7
BIRTHPLACE_POS = 8
ADDRESS_POS = 9
GUARDIAN_POS = 10
GUARDIAN_CONTACT_POS = 11


# ==========================================================================
# SECTION 2: DATA MANIPULATION FUNCTIONS
# These functions only read or change the students list.
# ==========================================================================

def load_sample_records():
    """Return a list of pre-loaded sample records (a list of lists)."""
    records = [
        ["022627007249", "Lyka Rosalada", "BSIT", 1, "COC-FC1-BSIT1-03", "09525689155", "1111",
         "03/26/2008", "Cagayan de Oro", "Macasandig, Aluba",
         "Jenifer Rosalada", "09558073236"],
        ["02232400074", "Jana Greizl S. Factura", "BSIT", 1, "COC-FC1-BSIT1-02", "09489932976", "2222",
         "01/13/2003", "Talakag Bukidnon", "San Isidro Talakag Bukidnon",
         "Grace Factura", "09489932976"],
        ["022627002498", "Sarah Jane Ranido", "BSIT", 1, "COC-FC1-BSIT1-03", "09103497152", "3333",
         "11/18/2007", "Talisayan, Misamis Oriental", "Opol, Igpit",
         "Thelma Loquero", "09700535565"],
        ["022627016424", "Clark Lewis T. Maagad", "BSIT", 1, "COC-FC1-BSIT1-03", "09979064487", "4444",
         "07/24/2007", "Cebu City", "Zone 2 Colanda Iponan",
         "Inin T. Maagad", "09531671316"],
        ["022425011734", "King Ralph C. Reyes", "BSIT", 1, "COC-FC1-BSIT1-03", "09658758827", "5555",
         "04/06/2008", "Cagayan de Oro", "Zone 8 upper Bulua",
         "Normalis C. Reyes", "09756414593"],
        ["022627016574", "Janie Boy O. Nabong", "BSIT", 1, "COC-FC1-BSIT1-03", "09242055046", "6666",
         "11/21/2007", "Cagayan de Oro City", "Lower Midkiwa, Bayanga, Cdoc",
         "Wilma O. Nabong", "09531336236"],
    ]
    return records


def create_student_record(student_id, name, course, year_level, section, contact, pin,
                          birth_date, birth_place, address, guardian_name, guardian_contact):
    """Build and return one student record as a list (see the record layout above)."""
    return [student_id, name, course, year_level, section, contact, pin,
            birth_date, birth_place, address, guardian_name, guardian_contact]


def add_student(students, record):
    """Append a new record to the students list."""
    students.append(record)


def find_student_index(students, student_id):
    """Return the list position of the given Student ID, or -1 if not found."""
    for i in range(len(students)):
        if students[i][ID_POS] == student_id:
            return i
    return -1


def search_students(students, keyword):
    """Return a new list of records whose ID or name contains the keyword."""
    results = []
    key = keyword.lower()
    for record in students:
        if key in record[ID_POS].lower() or key in record[NAME_POS].lower():
            results.append(record)
    return results


def update_student(students, index, name, course, year_level, section, contact, pin,
                   birth_date, birth_place, address, guardian_name, guardian_contact):
    """Overwrite the fields of the record at the given index (ID stays the same)."""
    students[index][NAME_POS] = name
    students[index][COURSE_POS] = course
    students[index][YEAR_POS] = year_level
    students[index][SECTION_POS] = section
    students[index][CONTACT_POS] = contact
    students[index][PIN_POS] = pin
    students[index][BIRTHDATE_POS] = birth_date
    students[index][BIRTHPLACE_POS] = birth_place
    students[index][ADDRESS_POS] = address
    students[index][GUARDIAN_POS] = guardian_name
    students[index][GUARDIAN_CONTACT_POS] = guardian_contact


def update_contact(students, index, contact):
    """Change only the contact number of the record at the given index."""
    students[index][CONTACT_POS] = contact


def update_guardian_contact(students, index, guardian_contact):
    """Change only the Parent/Guardian contact number of the record at the given index."""
    students[index][GUARDIAN_CONTACT_POS] = guardian_contact


def get_field(record, position):
    """
    Return the saved text of one field, or "Not provided" when the field is
    missing or empty (so displaying a record never causes an error).
    """
    if position >= len(record):
        return NOT_PROVIDED
    value = str(record[position]).strip()
    if value == "":
        return NOT_PROVIDED
    return value


def get_unique_sections(students):
    """Return a list of the different sections found in the students list."""
    sections = []
    for record in students:
        if record[SECTION_POS] not in sections:
            sections.append(record[SECTION_POS])
    return sections


def count_in_section(students, section):
    """Return how many students belong to the given section."""
    count = 0
    for record in students:
        if record[SECTION_POS] == section:
            count = count + 1
    return count


# ==========================================================================
# SECTION 3: COMPUTATION AND VALIDATION FUNCTIONS
# These functions only calculate or check values. They never print or ask
# for input; they take parameters and return a result.
# ==========================================================================

def compute_percentage(part, total):
    """Return part as a percentage of total (0.0 when total is zero)."""
    if total == 0:
        return 0.0
    return (part / total) * 100


def attempts_left(max_attempts, used_attempts):
    """Return how many login attempts are still available."""
    return max_attempts - used_attempts


def is_whole_number(text):
    """True if text is made only of the digits 0-9 (and is not empty)."""
    return text.isascii() and text.isdigit()


def is_valid_student_id(student_id):
    """Student ID: 4-12 digits, numbers only."""
    return (len(student_id) >= MIN_ID_LENGTH
            and len(student_id) <= MAX_ID_LENGTH
            and is_whole_number(student_id))


def is_valid_name(name):
    """Name: 2-40 characters, letters plus space . - ' only, at least one letter."""
    if len(name) < 2 or len(name) > MAX_NAME_LENGTH:
        return False
    has_letter = False
    for ch in name:
        if ch.isalpha():
            has_letter = True
        elif ch not in " .-'":
            return False
    return has_letter


def is_valid_section(section):
    """Section: 2-16 characters, no spaces."""
    return (len(section) >= 2
            and len(section) <= MAX_SECTION_LENGTH
            and " " not in section)


def is_valid_contact(contact):
    """Contact: exactly 11 digits and starts with 09."""
    return (len(contact) == CONTACT_LENGTH
            and is_whole_number(contact)
            and contact.startswith(CONTACT_PREFIX))


def is_valid_pin(pin):
    """PIN: exactly 4 digits."""
    return len(pin) == PIN_LENGTH and is_whole_number(pin)


def has_letter(text):
    """True if text contains at least one letter."""
    for ch in text:
        if ch.isalpha():
            return True
    return False


def is_leap_year(year):
    """True if the year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month, year):
    """Return how many days the given month (1-12) has in the given year."""
    days = DAYS_IN_MONTH[month - 1]
    if month == 2 and is_leap_year(year):
        days = 29
    return days


def is_valid_birth_date(birth_date):
    """Birth date: MM/DD/YYYY, a real calendar date, year from 1960 to 2012."""
    if len(birth_date) != 10 or birth_date[2] != "/" or birth_date[5] != "/":
        return False
    month_text = birth_date[0:2]
    day_text = birth_date[3:5]
    year_text = birth_date[6:10]
    if not (is_whole_number(month_text) and is_whole_number(day_text)
            and is_whole_number(year_text)):
        return False
    month = int(month_text)
    day = int(day_text)
    year = int(year_text)
    if year < MIN_BIRTH_YEAR or year > MAX_BIRTH_YEAR:
        return False
    if month < 1 or month > 12:
        return False
    return day >= 1 and day <= days_in_month(month, year)


def is_valid_birth_place(place):
    """Birth place: 2-40 characters with at least one letter."""
    return len(place) >= 2 and len(place) <= MAX_PLACE_LENGTH and has_letter(place)


def is_valid_address(address):
    """Home address: 5-80 characters with at least one letter."""
    return (len(address) >= MIN_ADDRESS_LENGTH
            and len(address) <= MAX_ADDRESS_LENGTH
            and has_letter(address))


# ==========================================================================
# SECTION 4: TERMINAL INTERFACE FUNCTIONS
# All screen output and keyboard input is handled here.
# ==========================================================================

def print_line(char="-"):
    """Print a separator line."""
    print(char * LINE_WIDTH)


def print_title(title):
    """Print a boxed screen title."""
    print()
    print_line("=")
    print(title.center(LINE_WIDTH))
    print_line("=")


def pause():
    """Wait for the user so results can be read before the menu returns."""
    input("\nPress Enter to return to the menu...")


def show_start_menu():
    """Display the first screen where the user picks a role."""
    print_title("STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("[1] Registrar")
    print("[2] IT Freshman Student")
    print("[3] Teacher")
    print("[0] Exit System")


def show_registrar_menu():
    """Display the Registrar menu (as written in the proposal)."""
    print_title("STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("Registrar Menu")
    print("[1] Add Student Record")
    print("[2] View Student Records")
    print("[3] Search Student Record")
    print("[4] Update Student Record")
    print("[0] Exit")


def show_teacher_menu():
    """Display the Teacher menu (the Teacher can only view and search records)."""
    print_title("STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("Teacher Menu")
    print("[1] View Student Records")
    print("[2] Search Student Record")
    print("[0] Exit")


def show_student_logged_in_menu(status_text):
    """Display the menu a student sees after a successful login."""
    print_title("STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("Student Menu")
    print(f"Status: {status_text}")
    print("[1] View Student Record")
    print("[2] Update Student Record")
    print("[0] Exit")


def read_menu_choice(low, high):
    """Keep asking until the user enters a whole number from low to high."""
    while True:
        text = input(f"Select Option [{low}-{high}]: ").strip()
        if text == "":
            print("\n[ERROR] Input cannot be empty. Please enter a number.")
        elif not is_whole_number(text):
            print("\n[ERROR] Invalid input. Please enter numbers only.")
        elif int(text) < low or int(text) > high:
            print(f"\n[ERROR] Option out of range. Choose from {low} to {high}.")
        else:
            return int(text)


def ask_yes_no(question):
    """Ask a Y/N question and return True for Y, False for N."""
    while True:
        answer = input(f"{question} (Y/N): ").strip().upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("\n[ERROR] Please type Y or N only.")


def read_text(label, default=""):
    """
    Read one line of text. If a default value is given, the user can press
    Enter to keep it; otherwise an empty entry is returned as "".
    """
    if default != "":
        text = input(f"{label} [{default}]: ").strip()
        if text == "":
            return default
        return text
    return input(f"{label}: ").strip()


def prompt_new_student_id(students):
    """Ask for a Student ID that is valid and not yet used."""
    while True:
        student_id = read_text("Student ID")
        if not is_valid_student_id(student_id):
            print(f"\n[ERROR] Invalid Student ID. Use {MIN_ID_LENGTH}-{MAX_ID_LENGTH} "
                  "characters with no spaces.")
        elif find_student_index(students, student_id) != -1:
            print("\n[ERROR] Student ID already exists. Enter a different ID.")
        else:
            return student_id


def prompt_name(default="", label="Student Name"):
    """Ask for a valid full name (Enter keeps the default, if any)."""
    while True:
        name = read_text(label, default)
        if is_valid_name(name):
            return name
        print(f"\n[ERROR] Invalid name. Use letters, spaces, . - ' only "
              f"(2-{MAX_NAME_LENGTH} characters).")


def prompt_birth_date(default=""):
    """Ask for a valid birth date in MM/DD/YYYY format (Enter keeps the default, if any)."""
    while True:
        birth_date = read_text("Birth Date (MM/DD/YYYY)", default)
        if is_valid_birth_date(birth_date):
            return birth_date
        print(f"\n[ERROR] Invalid birth date. Use MM/DD/YYYY with a real date "
              f"(e.g., 03/14/2008), year {MIN_BIRTH_YEAR}-{MAX_BIRTH_YEAR}.")


def prompt_birth_place(default=""):
    """Ask for a valid birth place (Enter keeps the default, if any)."""
    while True:
        birth_place = read_text("Birth Place", default)
        if is_valid_birth_place(birth_place):
            return birth_place
        print(f"\n[ERROR] Invalid birth place. Use 2-{MAX_PLACE_LENGTH} characters "
              "with at least one letter.")


def prompt_address(default=""):
    """Ask for a valid home address (Enter keeps the default, if any)."""
    while True:
        address = read_text("Home Address", default)
        if is_valid_address(address):
            return address
        print(f"\n[ERROR] Invalid home address. Use {MIN_ADDRESS_LENGTH}-{MAX_ADDRESS_LENGTH} "
              "characters with at least one letter.")


def prompt_section(default=""):
    """Ask for a valid section code (converted to UPPER CASE)."""
    while True:
        section = read_text("Section", default).upper()
        if is_valid_section(section):
            return section
        print(f"\n[ERROR] Invalid section. Use 2-{MAX_SECTION_LENGTH} characters "
              "with no spaces (e.g., COC-FC1-BSIT1-01).")


def prompt_contact(default="", label="Contact Number"):
    """Ask for a valid mobile number (Enter keeps the default, if any)."""
    while True:
        contact = read_text(label, default)
        if is_valid_contact(contact):
            return contact
        print(f"\n[ERROR] Invalid contact number. Enter {CONTACT_LENGTH} digits "
              f"starting with {CONTACT_PREFIX} (e.g., 09171234567).")


def prompt_pin(current_pin=""):
    """
    Ask for a 4-digit PIN. When current_pin is given (update mode), the user
    can press Enter to keep it. The current PIN is never displayed.
    """
    while True:
        if current_pin != "":
            pin = input(f"New {PIN_LENGTH}-digit PIN (press Enter to keep current): ").strip()
            if pin == "":
                return current_pin
        else:
            pin = input(f"{PIN_LENGTH}-digit PIN for the student: ").strip()
        if is_valid_pin(pin):
            return pin
        print(f"\n[ERROR] Invalid PIN. Enter exactly {PIN_LENGTH} digits.")


def print_detail_line(label, value):
    """Print one 'Label : value' line with the labels lined up."""
    print(f"  {label:<{LABEL_WIDTH}}: {value}")


def display_record_detail(record, show_section=True):
    """
    Print the COMPLETE record as labelled lines (the PIN is never shown).
    A field with no saved information is displayed as "Not provided".
    """
    print_detail_line("Student ID", record[ID_POS])
    print_detail_line("Student Name", get_field(record, NAME_POS))
    print_detail_line("Course", get_field(record, COURSE_POS))
    print_detail_line("Year Level", get_field(record, YEAR_POS))
    if show_section:
        print_detail_line("Section", get_field(record, SECTION_POS))
    print_detail_line("Birth Date", get_field(record, BIRTHDATE_POS))
    print_detail_line("Birth Place", get_field(record, BIRTHPLACE_POS))
    print_detail_line("Home Address", get_field(record, ADDRESS_POS))
    print_detail_line("Contact Number", get_field(record, CONTACT_POS))
    print_detail_line("Parent/Guardian Name", get_field(record, GUARDIAN_POS))
    print_detail_line("Parent/Guardian Contact Number", get_field(record, GUARDIAN_CONTACT_POS))


def display_record_table(records):
    """Print a list of records as a numbered table using a for loop."""
    print(f"{'No.':<4}{'Student ID':<13}{'Name':<24}{'Course':<7}{'Yr':<3}"
          f"{'Section':<17}{'Contact':<12}")
    print_line()
    for i in range(len(records)):
        r = records[i]
        print(f"{i + 1:<4}{r[ID_POS]:<13}{r[NAME_POS]:<24.23}{r[COURSE_POS]:<7}"
              f"{r[YEAR_POS]:<3}{r[SECTION_POS]:<17}{r[CONTACT_POS]:<12}")


def ask_record_to_open(records):
    """
    Ask which listed student to open. Returns that student's record, or None
    if the user presses Enter to skip. Only IDs found in 'records' are accepted,
    so the information shown always belongs to the chosen student.
    """
    while True:
        student_id = input("Enter a Student ID from the list to view the complete "
                           "information (Enter to skip): ").strip()
        if student_id == "":
            return None
        index = find_student_index(records, student_id)
        if index != -1:
            return records[index]
        print("\n[ERROR] That Student ID is not in the list above.")


def show_complete_information(record):
    """Show one student's complete information on its own screen."""
    print_title("COMPLETE STUDENT INFORMATION")
    display_record_detail(record)


# ==========================================================================
# SECTION 5: FEATURE FUNCTIONS AND MENU CONTROL LOOPS
# ==========================================================================

# ---------------------------- Login features ------------------------------

def registrar_login():
    """Registrar login. Returns True if successful, False after too many tries."""
    print_title("REGISTRAR LOGIN")
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Username: ").strip()
        if not is_whole_number(username):
            print("\n[ERROR] Numbers only. Please try again.")
            continue
        password = input("Password: ").strip()
        if not is_whole_number(password):
            print("\n[ERROR] Numbers only. Please try again.")
            continue
        attempts = attempts + 1
        if username == REGISTRAR_USERNAME and password == REGISTRAR_PASSWORD:
            print("\n[SUCCESS] Login successful. Welcome, Registrar!")
            return True
        remaining = attempts_left(MAX_LOGIN_ATTEMPTS, attempts)
        if remaining > 0:
            print(f"\n[ERROR] Incorrect username or password. Attempts left: {remaining}")
        else:
            print("\n[ERROR] Too many failed attempts. Returning to the main screen.")
    return False


def teacher_login():
    """Teacher login. Returns True if successful, False after too many tries."""
    print_title("TEACHER LOGIN")
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Username: ").strip()
        if not is_whole_number(username):
            print("\n[ERROR] Numbers only. Please try again.")
            continue
        password = input("Password: ").strip()
        if not is_whole_number(password):
            print("\n[ERROR] Numbers only. Please try again.")
            continue
        attempts = attempts + 1
        if username == TEACHER_USERNAME and password == TEACHER_PASSWORD:
            print("\n[SUCCESS] Login successful. Welcome, Teacher!")
            return True
        remaining = attempts_left(MAX_LOGIN_ATTEMPTS, attempts)
        if remaining > 0:
            print(f"\n[ERROR] Incorrect username or password. Attempts left: {remaining}")
        else:
            print("\n[ERROR] Too many failed attempts. Returning to the main screen.")
    return False


def student_login(students):
    """Student login (Student ID + PIN). Returns the Student ID, or "" if it failed."""
    print_title("STUDENT LOGIN")
    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        student_id = input("Student ID: ").strip()
        if not is_whole_number(student_id):
            print("\n[ERROR] Numbers only. Please try again.")
            continue
        pin = input("PIN: ").strip()
        if not is_whole_number(pin):
            print("\n[ERROR] Numbers only. Please try again.")
            continue
        attempts = attempts + 1
        index = find_student_index(students, student_id)
        if index != -1 and students[index][PIN_POS] == pin:
            print(f"\n[SUCCESS] Login successful. Welcome, {students[index][NAME_POS]}!")
            return student_id
        remaining = attempts_left(MAX_LOGIN_ATTEMPTS, attempts)
        if remaining > 0:
            print(f"\n[ERROR] Incorrect Student ID or PIN. Attempts left: {remaining}")
        else:
            print("\n[ERROR] Too many failed attempts. Returning to the main screen.")
    return ""


# -------------------------- Registrar features ----------------------------

def add_student_record(students):
    """Registrar option 1: enter a new student and save it to the list."""
    print_title("ADD STUDENT RECORD")
    print("Enter the student's information. Press Enter to accept a value in [brackets].\n")
    student_id = prompt_new_student_id(students)
    name = prompt_name()
    course = ALLOWED_COURSES[0]           # course is always BSIT; no prompt needed
    year_level = ALLOWED_YEAR_LEVELS[0]   # system covers freshmen only; no prompt needed
    birth_date = prompt_birth_date()
    birth_place = prompt_birth_place()
    address = prompt_address()
    contact = prompt_contact()
    guardian_name = prompt_name("", "Parent/Guardian Name")
    guardian_contact = prompt_contact("", "Parent/Guardian Contact Number")
    section = prompt_section()
    pin = prompt_pin()

    new_record = create_student_record(student_id, name, course, year_level,
                                       section, contact, pin, birth_date,
                                       birth_place, address, guardian_name,
                                       guardian_contact)
    print("\nPlease review the new record:")
    display_record_detail(new_record)
    if ask_yes_no("Save this record?"):
        add_student(students, new_record)
        print(f"\n[SUCCESS] Record saved for {name}. Total students: {len(students)}")
    else:
        print("\n[INFO] Record was not saved.")
    pause()


def view_student_records(students):
    """
    Registrar option 2 (also Teacher option 1): list all records, show a section
    summary, then let the user open one student's complete information.
    """
    print_title("STUDENT RECORDS")
    if len(students) == 0:
        print("\n[INFO] No student records found.")
    else:
        display_record_table(students)
        print_line()
        total = len(students)
        print(f"Total students: {total}")
        print("Students per section:")
        for section in get_unique_sections(students):
            count = count_in_section(students, section)
            percent = compute_percentage(count, total)
            print(f"  {section:<18}{count:>3} student(s)  ({percent:.1f}%)")
        print()
        record = ask_record_to_open(students)
        if record is not None:
            show_complete_information(record)
    pause()


def search_student_record(students):
    """
    Registrar option 3 (also Teacher option 2): search by Student ID or name
    (partial match allowed) and show the complete information of the student.
    """
    print_title("SEARCH STUDENT RECORD")
    keyword = input("Enter Student ID or name to search: ").strip()
    if keyword == "":
        print("\n[ERROR] Nothing entered. Search cancelled.")
    else:
        results = search_students(students, keyword)
        if len(results) == 0:
            print(f"\n[ERROR] No student record matches '{keyword}'.")
        else:
            print(f"\n[SUCCESS] {len(results)} record(s) found for '{keyword}':\n")
            if len(results) == 1:
                display_record_detail(results[0])
            else:
                display_record_table(results)
                print_line()
                record = ask_record_to_open(results)
                if record is not None:
                    show_complete_information(record)
    pause()


def update_student_record(students):
    """Registrar option 4: change the information of an existing student."""
    print_title("UPDATE STUDENT RECORD")
    student_id = input("Enter the Student ID to update: ").strip()
    index = find_student_index(students, student_id)
    if index == -1:
        print(f"\n[ERROR] Student ID '{student_id}' not found.")
        pause()
        return

    record = students[index]
    print("\nCurrent record:")
    display_record_detail(record)
    print("\nPress Enter to keep a current value. (The Student ID cannot be changed.)\n")
    name = prompt_name(record[NAME_POS])
    course = ALLOWED_COURSES[0]           # course is always BSIT; no prompt needed
    year_level = record[YEAR_POS]         # system covers freshmen only; no prompt needed
    birth_date = prompt_birth_date(record[BIRTHDATE_POS])
    birth_place = prompt_birth_place(record[BIRTHPLACE_POS])
    address = prompt_address(record[ADDRESS_POS])
    contact = prompt_contact(record[CONTACT_POS])
    guardian_name = prompt_name(record[GUARDIAN_POS], "Parent/Guardian Name")
    guardian_contact = prompt_contact(record[GUARDIAN_CONTACT_POS],
                                      "Parent/Guardian Contact Number")
    section = prompt_section(record[SECTION_POS])
    pin = prompt_pin(record[PIN_POS])

    updated = create_student_record(record[ID_POS], name, course, year_level,
                                    section, contact, pin, birth_date,
                                    birth_place, address, guardian_name,
                                    guardian_contact)
    print("\nPlease review the updated record:")
    display_record_detail(updated)
    if ask_yes_no("Save these changes?"):
        update_student(students, index, name, course, year_level, section, contact, pin,
                       birth_date, birth_place, address, guardian_name, guardian_contact)
        print("\n[SUCCESS] Student record updated.")
    else:
        print("\n[INFO] No changes were saved.")
    pause()


# --------------------------- Student features -----------------------------

def view_my_record(students, student_id):
    """Logged-in menu option 1: the student's own complete record."""
    print_title("MY STUDENT RECORD")
    index = find_student_index(students, student_id)
    if index == -1:
        print("\n[ERROR] Record not found.")
    else:
        display_record_detail(students[index])
    pause()


def update_my_contact(students, student_id):
    """
    Logged-in menu option 2 (Update Student Record): let the student change only
    their own contact number and their Parent/Guardian contact number.
    """
    print_title("UPDATE MY CONTACT INFORMATION")
    index = find_student_index(students, student_id)
    if index == -1:
        print("\n[ERROR] Record not found.")
    else:
        current = students[index][CONTACT_POS]
        current_guardian = students[index][GUARDIAN_CONTACT_POS]
        print(f"Current contact number                 : {get_field(students[index], CONTACT_POS)}")
        print(f"Current Parent/Guardian contact number : {get_field(students[index], GUARDIAN_CONTACT_POS)}")
        print("\nPress Enter to keep a current value.\n")
        new_contact = prompt_contact(current)
        new_guardian_contact = prompt_contact(current_guardian,
                                              "Parent/Guardian Contact Number")
        if new_contact == current and new_guardian_contact == current_guardian:
            print("\n[INFO] Contact information unchanged.")
        elif ask_yes_no("Save these contact changes?"):
            update_contact(students, index, new_contact)
            update_guardian_contact(students, index, new_guardian_contact)
            print("\n[SUCCESS] Contact information updated.")
        else:
            print("\n[INFO] Update cancelled.")
    pause()


# ---------------------------- Menu control loops --------------------------

def registrar_menu_loop(students):
    """Registrar menu: repeats (while loop) until the Registrar chooses 0."""
    running = True
    while running:
        show_registrar_menu()
        choice = read_menu_choice(0, 4)
        if choice == 1:
            add_student_record(students)
        elif choice == 2:
            view_student_records(students)
        elif choice == 3:
            search_student_record(students)
        elif choice == 4:
            update_student_record(students)
        else:
            print("\n[INFO] Registrar logged out.")
            running = False


def teacher_menu_loop(students):
    """
    Teacher menu: repeats (while loop) until the Teacher chooses 0.
    The Teacher has read-only access: [1] View Student Records,
    [2] Search Student Record. The Teacher cannot add or change records.
    """
    running = True
    while running:
        show_teacher_menu()
        choice = read_menu_choice(0, 2)
        if choice == 1:
            view_student_records(students)
        elif choice == 2:
            search_student_record(students)
        else:
            print("\n[INFO] Teacher logged out.")
            running = False


def student_menu_loop(students):
    """
    Student session: choosing IT Freshman Student on the start screen opens
    the Student Login directly. After a successful login the logged-in menu
    repeats (while loop) until the student chooses 0:
    [1] View Student Record, [2] Update Student Record, [0] Exit.
    """
    current_student_id = student_login(students)   # "" means the login failed
    running = current_student_id != ""
    while running:
        index = find_student_index(students, current_student_id)
        status_text = f"Logged in as {students[index][NAME_POS]}"
        show_student_logged_in_menu(status_text)
        choice = read_menu_choice(0, 2)

        if choice == 1:
            view_my_record(students, current_student_id)
        elif choice == 2:
            update_my_contact(students, current_student_id)
        else:
            print("\n[INFO] Student logged out.")
            running = False


# ==========================================================================
# SECTION 6: PROGRAM ENTRY POINT
# ==========================================================================

def main():
    """Start SIMS: load the records, then loop on the start screen."""
    students = load_sample_records()     # the list that stores all records in memory
    running = True
    while running:
        show_start_menu()
        choice = read_menu_choice(0, 3)
        if choice == 1:
            if registrar_login():
                registrar_menu_loop(students)
        elif choice == 2:
            student_menu_loop(students)
        elif choice == 3:
            if teacher_login():
                teacher_menu_loop(students)
        else:
            running = False
    print("\nThank you for using the Student Information Management System. Goodbye!")


if __name__ == "__main__":
    main()
