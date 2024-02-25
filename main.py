from hash_table.main import main as run_hash_table_app
from binary_search.main import main as run_binary_search_app
from algorithmic_efficiency.main import main as run_algorithmic_efficiency_app


def main():
    try:
        print("Which app do you want to run? \n (1) Hash table \n (2) Binary seach \n (3) Algorithmic efficiency \n (q) Quit \n")
        action = input()

        if action == "1":
            run_hash_table_app()

        elif action == "2":
            run_binary_search_app()

        elif action == "3":
            run_algorithmic_efficiency_app()

        elif action == "q":
            print("\nGood bye!")
            return
        else:
            print("\033[91mI don't understand that command\033[0m")

    except KeyboardInterrupt:
        print("\nGood bye!")
        return


if __name__ == "__main__":
    main()
