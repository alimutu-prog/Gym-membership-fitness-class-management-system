

from gym_system import GymSystem

gym = GymSystem()

# TC1: Normal case, valid class
c1 = gym.add_class("Yoga", "Coach Lee", "Mon 6PM", 1)
print("TC1:", "PASS" if c1.class_id == "C001" else "FAIL")

# TC2: Invalid case, zero capacity
try:
    gym.add_class("Bad Class", "X", "Y", 0)
    print("TC2: FAIL (zero capacity was not rejected)")
except ValueError:
    print("TC2: PASS")

# TC3: Edge case, class exactly at capacity -> is_full() True
c1.add_registration()
print("TC3:", "PASS" if c1.is_full() else "FAIL")

# TC4: Normal case, class below capacity -> is_full() False
c2 = gym.add_class("Spin", "Coach Ivy", "Wed 7AM", 5)
c2.add_registration()
c2.add_registration()
print("TC4:", "PASS" if not c2.is_full() else "FAIL")

# TC5: Edge case, cancelling frees a spot
c1.remove_registration()
print("TC5:", "PASS" if not c1.is_full() else "FAIL")
