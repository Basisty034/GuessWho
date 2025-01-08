import random

# Data karakter
characters = [
    {"name": "Alice", "hint": "She loves reading books and has a curious mind."},
    {"name": "Bob", "hint": "He is a great cook and enjoys biking."},
    {"name": "Charlie", "hint": "He is a computer enthusiast and loves programming."}
]

def print_line():
    """Mencetak garis pemisah."""
    print("=" * 40)

def play_game():
    """Fungsi utama untuk permainan."""
    # Pilih karakter secara acak
    chosen_character = random.choice(characters)

    # Tampilkan sambutan dan petunjuk
    print_line()
    print(" Welcome to the Guess Who Game! ")
    print_line()
    print(f"Here is your hint: {chosen_character['hint']}")
    print_line()

    attempts = 3

    while attempts > 0:
        # Minta tebakan dari pemain
        print(f"You have {attempts} attempt(s) remaining.")
        guess = input("Who am I? ").strip()

        # Periksa jawaban
        if guess.lower() == chosen_character['name'].lower():
            print_line()
            print("🎉 Congratulations! You guessed it right!")
            print(f"I am {chosen_character['name']}!")
            print_line()
            return
        else:
            print("❌ Wrong guess. Try again!")
            attempts -= 1

    # Jika gagal
    print_line()
    print("😞 Sorry, you're out of attempts.")
    print(f"The correct answer was {chosen_character['name']}.")
    print_line()

# Jalankan game
if __name__ == "__main__":
    play_game()
