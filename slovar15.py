# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

# У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру находить все номера определённого друга
n = int(input())
c = {}
t = []
for i in range(n):
    phone, name = input().lower().split()
    c.setdefault(phone, name)
c1 = {}
for phone, name in c.items():
    c1.setdefault(name,[]).append(phone)
m = int(input())
for y in range(m):
    a = input().lower()
    print(*c1.get(a, ["абонент не найден"]))
