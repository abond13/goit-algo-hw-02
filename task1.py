import queue
import time
import random
import string
import keyboard

class request:
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return f"Заявка {self.id}"

def generate_request(req_queue, req_id):
    """
    Створити нову заявку
    Додати заявку до черги
    """
    new_req = request(req_id)
    req_queue.put(new_req)
    print(f"Додана \"{new_req}\"")
    print(f"Довжина черги: [{req_queue.qsize()*'*'}]")
    time.sleep(0.5)

def process_request(req_queue):
    """
    Якщо черга не пуста:
        Видалити заявку з черги
        Обробити заявку
    Інакше:
        Вивести повідомлення, що черга пуста
    """
    if not req_queue.empty():
        curr_req = req_queue.get()
        print(f"Оброблена \"{curr_req}\"")
        print(f"Довжина черги: [{req_queue.qsize()*'*'}]")
        time.sleep(3)
    else:
        print("Черга пуста")

def random_string():
    result = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    result += '-' + ''.join(random.choice(string.digits) for _ in range(4))
    return result

def main():
    """
    Поки користувач не вийде з програми:
        Виконати generate_request() для створення нових заявок
        Виконати process_request() для обробки заявок
    """
    req_queue = queue.Queue()
    
    try:
        while True:
            if random.choice([False, True]):
                generate_request(req_queue, random_string())
            if random.choice([False, True]):
                process_request(req_queue)
    except KeyboardInterrupt:
        pass
        
if __name__ == "__main__":
    main()