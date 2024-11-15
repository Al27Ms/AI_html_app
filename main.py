from openai import OpenAI
from datetime import datetime


# Funkcja do wczytania klucza API z pliku i inicjalizacji klienta OpenAI
def initialize_openai_client(api_key_path="data/API_KEY.txt"):
    try:
        with open(api_key_path, "r") as file:
            api_key = file.read().strip()
        return OpenAI(api_key=api_key)
    except FileNotFoundError:
        print("Błąd: Plik z kluczem API nie został znaleziony.")
        return None


# Funkcja do wczytania treści artykułu z pliku tekstowego
def load_article_content(article_path="data/article.txt"):
    try:
        with open(article_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Błąd: Plik z artykułem nie został znaleziony.")
        return None


# Pierwsze zapytanie: Generowanie krótkiego wstępu do artykułu
def generate_intro(client, article_content):
    prompt_intro = f"""
Przeczytaj poniższy artykuł i wygeneruj bardzo krótki, jedno- lub dwuzdaniowy wstęp. Wstęp powinien podsumowywać główne tematy artykułu i zachęcać do jego przeczytania.

Treść artykułu:
{article_content}
"""

    messages = [{"role": "user", "content": prompt_intro}]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Błąd przy generowaniu wstępu: {e}")
        return None


# Drugie zapytanie: Generowanie pełnego HTML z dodanym spisem treści i wstępem
def generate_html_with_intro(client, article_content, intro_text):
    current_date = datetime.now().strftime("%Y-%m-%d")
    prompt_html = f"""
Jesteś redaktorem odpowiedzialnym za obróbkę poniższego artykułu tekstowego na profesjonalny kod HTML.

Twoje zadanie polega na:
1. Obróbka tekstu na dobrze sformatowany kod HTML, zachowując oryginalną treść artykułu – bez usuwania lub modyfikowania treści.
2. Dodaniu niezbędnych elementów HTML zgodnie z poniższymi wytycznymi.

Instrukcje tworzenia kodu HTML:
1. Struktura artykułu powinna być odpowiednio sformatowana, używając tagów HTML:
    - Tytuł artykułu powinien znajdować się w tagu <h1> (np. <h1>Sztuczna inteligencja: wpływ i wyzwania</h1>).
    - Używaj nagłówków <h2> i <h3> zgodnie z naturalną strukturą treści. Ważne nagłówki głównych sekcji powinny być oznaczone jako <h2>, a nagłówki podsekcji jako <h3>.
    - Paragrafy tekstu umieszczaj w tagach <p>.
2. Na początku artykułu dodaj hashtag (w tagu <p>), który sugeruje temat artykułu (np. #SztucznaInteligencja), a następnie nagłówek <h1> z tytułem artykułu.
3. Pod nagłówkiem <h1> umieść wstęp wygenerowany wcześniej: "{intro_text}"
4. Po wstępie dodaj spis treści (Table of Contents), zawierający odnośniki do wszystkich nagłówków <h2> i <h3>. Każdy wpis w spisie treści powinien być linkiem do odpowiedniej sekcji artykułu, wykorzystując atrybut `id` w każdym nagłówku.
5. W odpowiednich miejscach dodaj miejsca na grafiki, używając tagu <img> z atrybutem `src="image_placeholder.jpg"`. Każdy obraz powinien mieć opis w atrybucie `alt`, który precyzyjnie odzwierciedla temat sekcji (np. dla nagłówka "Rozwój uczenia maszynowego" użyj `alt="Ilustracja przedstawiająca rozwój uczenia maszynowego"`).
6. Na końcu artykułu dodaj następujący podpis:
   <p>Stworzone przez sztuczną inteligencję - model OpenAI GPT, {current_date}.</p>
7. Wygenerowany kod HTML powinien być czytelny i profesjonalnie sformatowany.
8. Dołącz tylko treść pomiędzy tagami <body> i </body>. Nie dodawaj tagów <html>, <head>, ani <body>.

Poniżej znajduje się treść artykułu:
{article_content}
"""

    messages = [{"role": "user", "content": prompt_html}]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Błąd przy generowaniu kodu HTML: {e}")
        return None


# Funkcja do zapisu wygenerowanego HTML do pliku
def save_html_to_file(html_content, output_path="artykul.html"):
    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"Plik HTML został zapisany pomyślnie w {output_path}")
    except Exception as e:
        print(f"Błąd przy zapisie pliku HTML: {e}")


# Główna funkcja wykonująca wszystkie operacje
def main():
    client = initialize_openai_client()
    if client is None:
        return

    article_content = load_article_content()
    if article_content is None:
        return

    # Generowanie wstępu
    intro_text = generate_intro(client, article_content)
    if intro_text is None:
        return

    # Generowanie pełnego HTML z wstępem
    html_content = generate_html_with_intro(client, article_content, intro_text)
    if html_content is not None:
        save_html_to_file(html_content)


# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
