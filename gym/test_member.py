"""
test_member.py — Owner: MEMBER A
Runs the exact test cases from the Test Plan for the Member class.
Run with: python test_member.py
"""

from gym_system import GymSystem
from member import Member

gym = GymSystem()

# TC1: Normal case, valid new member
m1 = gym.add_member("Alice Wong", 22, "Premium", "alice@mail.com")
print("TC1:", "PASS" if m1.member_id == "M001" else "FAIL")

# TC2: Duplicate contact should be rejected
try:
    gym.add_member("Someone Else", 30, "Basic", "alice@mail.com")
    print("TC2: FAIL (duplicate was not rejected)")
except ValueError:
    print("TC2: PASS")


# TC5: Search by partial name, case-insensitive
results = gym.search_member("ali")
print("TC5:", "PASS" if len(results) == 1 else "FAIL")

# TC6: Search with no matches
results = gym.search_member("zzz")
print("TC6:", "PASS" if results == [] else "FAIL")

# Extra: to_row / from_row round trip works correctly
rebuilt = Member.from_row(m1.to_row())
print("Round-trip:", "PASS" if rebuilt.member_id == m1.member_id and rebuilt.age == m1.age else "FAIL")
