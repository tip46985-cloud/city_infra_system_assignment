# City Infrastructure Management System
# Task 1: Vehicle Registration System
# Task 2: Event Management System Enhancement

# -----------------------------
# Task 1: Vehicle Registration
# -----------------------------
class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        """Update the owner of the vehicle."""
        self.owner = new_owner
        print(f"Owner of vehicle {self.registration_number} updated to {self.owner}")


# Demonstration for Task 1
print("=== Vehicle Registration System Demo ===")
vehicle1 = Vehicle("ABC123", "Car", "Alice")
vehicle2 = Vehicle("XYZ789", "Truck", "Bob")

print(f"Vehicle1: {vehicle1.registration_number}, {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle2: {vehicle2.registration_number}, {vehicle2.type}, Owner: {vehicle2.owner}")

# Update owners
vehicle1.update_owner("Charlie")
vehicle2.update_owner("Diana")

print(f"Vehicle1 after update: Owner: {vehicle1.owner}")
print(f"Vehicle2 after update: Owner: {vehicle2.owner}")
print()


# -----------------------------
# Task 2: Event Management
# -----------------------------
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # New attribute

    def add_participant(self):
        """Increase the participant count by one."""
        self.participant_count += 1
        print(f"Participant added to {self.name}. Total: {self.participant_count}")

    def get_participant_count(self):
        """Return the current participant count."""
        return self.participant_count


# Demonstration for Task 2
print("=== Event Management System Demo ===")
event1 = Event("City Marathon", "2025-10-01")
event2 = Event("Music Festival", "2025-11-15")

# Add participants
event1.add_participant()
event1.add_participant()
event1.add_participant()

event2.add_participant()

# Display participant counts
print(f"{event1.name} on {event1.date} has {event1.get_participant_count()} participants.")
print(f"{event2.name} on {event2.date} has {event2.get_participant_count()} participants.")
