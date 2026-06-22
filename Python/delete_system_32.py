import os

# WARNING: This code will delete your System32 folder, rendering your computer unusable.
# Do not run this unless you’re 100% sure you want to do this.
# This is irreversible and will require a complete reinstall of your operating system.

print("WARNING: If you lose this game, it will delete System32 and brick your computer.")
print("Only run this on a machine you don’t care about!")

game_lost = True 

if game_lost:
    confirmation = input("You lost the game! Type 'yes' to delete System32 and brick your computer: ")
    if confirmation.lower() == 'yes':
        # Delete System32 (needs admin privileges)
        os.system('rmdir /s /q C:\\Windows\\System32')
        print("System32 deleted. Your computer will soon become unusable.")
    else:
        print("Smart move. System32 is safe for now.")
else:
    print("You won the game! System32 is safe.")