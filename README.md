# AI_html_app

# Generowanie artykułów i kodu HTML z użyciem OpenAI GPT

Ten projekt służy do generowania profesjonalnie sformatowanego kodu HTML na podstawie artykułu tekstowego. Wykorzystuje API OpenAI GPT-3.5 do generowania wstępu, konwersji artykułu do HTML oraz generowania pliku HTML z zawartością artykułu, w tym spisem treści, obrazkami i stopką.

## Zawartość projektu
  I. Main.py
1. **initialize_openai_client**: Funkcja do wczytania klucza API z pliku i inicjalizacji klienta OpenAI.
2. **load_article_content**: Funkcja wczytująca treść artykułu z pliku tekstowego.
3. **generate_intro**: Funkcja generująca wstęp do artykułu przy użyciu modelu GPT-3.5.
4. **generate_html_with_intro**: Funkcja generująca pełny kod HTML artykułu, w tym wstęp, spis treści i obrazy.
5. **save_html_to_file**: Funkcja zapisująca wygenerowany HTML do pliku.
6. **main**: Główna funkcja realizująca cały proces: wczytanie danych, generowanie wstępu, konwersja na HTML i zapis pliku.
   
  II. Pliki
1. **data/API_KEY.txt**: Plik z kluczem API OpenAI.
2. **szablon.html**: Plik z szablonem gotowym do użycia po wygenerowaniu kodu HTML.
3. **artykul.html**: Plik z przykładem wcześniej wygenerowanego pliku.
4. **podglad.html**: Plik gotowego artykułu.
## Wymagania

- Python 3.x
- Biblioteka `openai` do komunikacji z API OpenAI.
- Pliki wejściowe (klucz API oraz artykuł w formacie tekstowym).
  
## Instrukcja uruchomienia
Ustawienie klucza API:

Utwórz plik **data/API_KEY.txt** i umieść w nim swój klucz API OpenAI.
Przygotowanie artykułu:

Utwórz plik **data/article.txt** zawierający artykuł tekstowy, który chcesz przekształcić na HTML. (Przykładowy artykuł jest w: data/article.txt)
Uruchomienie programu:

Aby uruchomić skrypt i wygenerować plik HTML, uruchom **main.py**.

Wynik:

Po zakończeniu skryptu wygenerowany plik HTML zostanie zapisany w katalogu roboczym jako **artykul.html**.
