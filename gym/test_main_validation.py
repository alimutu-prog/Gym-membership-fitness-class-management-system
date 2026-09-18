

from unittest.mock import patch
import main

# TC1: Invalid case, out-of-range menu number, then valid
with patch("builtins.input", side_effect=["99", "3"]):
    result = main.get_menu_choice("Choice: ", ["1", "2", "3"])
print("TC1:", "PASS" if result == "3" else "FAIL")

# TC2: Invalid case, non-numeric menu input, then valid
with patch("builtins.input", side_effect=["abc", "1"]):
    result = main.get_menu_choice("Choice: ", ["1", "2", "3"])
print("TC2:", "PASS" if result == "1" else "FAIL")

# TC3: Invalid case, empty input, then valid
with patch("builtins.input", side_effect=["", "Alice"]):
    result = main.get_nonempty_string("Enter name: ")
print("TC3:", "PASS" if result == "Alice" else "FAIL")

# Extra: get_valid_int rejects letters and negatives before accepting
with patch("builtins.input", side_effect=["abc", "-5", "25"]):
    result = main.get_valid_int("Enter age: ", min_value=1)
print("Extra (get_valid_int):", "PASS" if result == 25 else "FAIL")

# TC4 (Exit flow)
print("TC4: see live demo — choosing option 11 in main.py auto-saves and exits cleanly")
