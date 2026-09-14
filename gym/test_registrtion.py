
"""

Tests the Registration functionality.


"""

# Import the system we are testing
from gym_system import GymSystem

# Create a gym system for testing
gym = GymSystem()

# Create test members
member = gym.add_member("Alice Wong", 22, "Premium", "alice@mail.com")
second_member = gym.add_member("Ben Kato", 30, "Basic", "ben@mail.com")

# Create a class with capacity 1 to test full classes
small_class = gym.add_class("Yoga", "Coach Lee", "Mon 6PM", 1)

# Create a normal class for other tests
big_class = gym.add_class("Spin", "Coach Ivy", "Wed 7AM", 5)


# TC1: Test a valid registration
r1 = gym.register_for_class(member.member_id, big_class.class_id)

# Registration should be Active
print("TC1:", "PASS" if r1.status == "Active" else "FAIL")


# TC2: Test registration when class is full
gym.register_for_class(member.member_id, small_class.class_id)

try:
    # Second member should be rejected
    gym.register_for_class(second_member.member_id, small_class.class_id)
    print("TC2: FAIL (full class was not rejected)")

except ValueError:
    # ValueError means the full class was rejected
    print("TC2: PASS")


# TC3: Test duplicate registration
try:
    # Member is already registered for this class
    gym.register_for_class(member.member_id, big_class.class_id)
    print("TC3: FAIL (duplicate was not rejected)")

except ValueError:
    # Duplicate registration was rejected
    print("TC3: PASS")


# TC4: Test an invalid member ID
try:
    # M999 does not exist
    gym.register_for_class("M999", big_class.class_id)
    print("TC4: FAIL (unknown member was not rejected)")

except ValueError:
    # Invalid member was rejected
    print("TC4: PASS")


# TC5: Test cancelling a registration
gym.cancel_registration(r1.registration_id)

# Status should now be Cancelled
print("TC5:", "PASS" if r1.status == "Cancelled" else "FAIL")


# TC6: Test cancelling an already-cancelled registration
try:
    # This registration was already cancelled
    gym.cancel_registration(r1.registration_id)
    print("TC6: FAIL (double-cancel was not rejected)")

except ValueError:
    # Double cancellation was rejected
    print("TC6: PASS")
```
