# Практическая работа №1 – Модуль 04 Design Principles  
**Курс:** Application Design Patterns  
**Тема:** Система управления транспортными средствами  

---

## 1. Введение
В данном проекте реализована **система управления транспортными средствами** с использованием принципов **объектно-ориентированного программирования**.  
Задача заключалась в построении иерархии классов для различных видов транспорта и применении **наследования, полиморфизма и композиции**.  

---

## 2. Структура классов
- **Vehicle (базовый класс)**  
  Атрибуты: `make`, `model`, `year`  
  Методы: `engine_start()`, `engine_stop()`  

- **Car (производный класс)**  
  Дополнительные атрибуты: `doors`, `transmission`  

- **Motorcycle (производный класс)**  
  Дополнительные атрибуты: `body_type`, `has_storage_box`  

- **Garage (композиция)**  
  Хранит список транспортных средств.  
  Методы: `add_vehicle()`, `remove_vehicle()`, `list_vehicles()`  

- **Fleet (композиция)**  
  Хранит список гаражей.  
  Методы: `add_garage()`, `remove_garage()`, `search_vehicle()`  

---

## 3. Пример выполнения программы
Garage 'Downtown Garage' with 2 vehicles.

Car: 2020 Toyota Camry | 4 doors, Automatic transmission

Motorcycle: 2021 Yamaha R15 | Sport, no storage box

Garage 'Airport Garage' with 2 vehicles.

Car: 2019 Honda Civic | 4 doors, Manual transmission

Motorcycle: 2018 Harley-Davidson Street 750 | Cruiser, with storage box

Search results for 'Honda':
Found in Airport Garage: Car: 2019 Honda Civic | 4 doors, Manual transmission

After removal:
Garage 'Downtown Garage' with 1 vehicles.
Fleet with 1 garages.


---

## 4. Заключение
В данной работе была реализована система управления транспортом, которая продемонстрировала:  
- **Наследование**: классы `Car` и `Motorcycle` расширяют `Vehicle`.  
- **Полиморфизм**: разные реализации метода `__str__()` для каждого типа транспорта.  
- **Композиция**: `Garage` управляет транспортными средствами, а `Fleet` — гаражами.  

