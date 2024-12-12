import requests
from requests.exceptions import RequestException, JSONDecodeError
from .models import Review


class ReviewService:
    @staticmethod
    def fetch_reviews():
        try:
            # Отправляем GET-запрос к внешнему API
            response = requests.get('https://feedbacks1.wb.ru/feedbacks/v2/24971554')
            response.raise_for_status()  # Проверяем статус ответа

            # Преобразуем ответ в JSON
            data = response.json().get('feedbacks', None)
            if data is None:
                raise ValueError("Key 'feedbacks' not found in the response")

            reviews = []
            for item in data:
                try:
                    # Извлекаем данные из каждого отзыва
                    rating = item.get('productValuation')
                    text = item.get('text')
                    pros = item.get('pros')
                    author = item.get('wbUserDetails', {}).get('name')
                    create = item.get('createdDate')

                    # Фильтруем отзывы
                    if rating == 5 and (len(text) >= 20 or len(pros) >= 20):
                        reviews.append({
                            'author': author,
                            'create': create,
                            'text': text,
                            'pros': pros,
                        })
                    if len(reviews) == 10:
                        break
                except (KeyError, TypeError) as e:
                    # Обрабатываем ошибки, если данные в отзыве некорректны
                    print(f"Error processing review item: {e}")
                    continue

            return reviews

        except RequestException as e:
            # Обрабатываем ошибки сети или запроса
            print(f"Request error: {e}")
            return []
        except JSONDecodeError as e:
            # Обрабатываем ошибки декодирования JSON
            print(f"JSON decode error: {e}")
            return []
        except ValueError as e:
            # Обрабатываем ошибки, связанные с отсутствием ключа 'feedbacks'
            print(f"Value error: {e}")
            return []
        except Exception as e:
            # Обрабатываем любые другие исключения
            print(f"Unexpected error: {e}")
            return []

    @staticmethod
    def fetch_and_update_reviews():
        # Получаем новые отзывы
        reviews = ReviewService.fetch_reviews()

        # Удаляем старые отзывы (если нужно)
        Review.objects.all().delete()

        # Сохраняем новые отзывы в базу данных
        for review in reviews:
            Review.objects.create(
                author=review['author'],
                create=review['create'],
                text=review['text'],
                pros=review['pros']
            )
        return len(reviews)
