import os


def main():
    nombre = os.getenv("USERNAME")
    language = os.getenv("LANGUAGE")
    print(f"¡Hola, {nombre} desde GitHub!, tu lenguaje es {language}.")


if __name__ == "__main__":
    main()