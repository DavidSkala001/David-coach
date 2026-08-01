from config import load_config
from coach import Coach


def main():

    config = load_config()

    coach = Coach()

    print()

    print("David Coach v0.1")

    print()

    print("Configuration loaded")

    print(f"Athlete ID: {config.athlete_id}")

    print()

    recommendation = coach.recommendation()

    print("Today's recommendation")

    print(recommendation["title"])

    print(recommendation["duration"])

    print(recommendation["power"])

    print()

    print(recommendation["reason"])


if __name__ == "__main__":
    main()
