def read_data():
    c = int(input()) #число домов
    households = []

    for _ in range(c):
        #Чтение названия города и числа комнат
        city, n_i = input().split()
        n_i = int(n_i)

        rooms = []

        for __ in range(n_i):
            #Чтение расписания и названия комнаты
            t_ij, s_ij = input().split()
            rooms.append((t_ij, s_ij))

        households.append({"city": city, "rooms": rooms})

    m = int(input()) #число запросов

    queries = []

    for _ in range(m):
        #чтение числа городов и их названия
        query = input().split()
        l = int(query[0])
        cities = query[1:]
        queries.append({"count": l, "cities": cities})

    return households, queries

def find_slots(households, queries):
    results = []

    for query in queries:
        required_cities = query["cities"]
        selected_rooms = []

        city_schedules = []
        for city in required_cities:
            for household in households:
                if household["city"] == city:
                    city_schedules.append(household["rooms"])
                    break

        for hour in range(24):
            temp_selected_rooms = []
            valid = True

            for rooms in city_schedules:
                found = False
                for schedule, name in rooms:
                    if schedule[hour] == ".":
                        temp_selected_rooms.append(name)
                        found = True
                        break
                if not found:
                    valid = False
                    break

            if valid:
                selected_rooms = temp_selected_rooms
                break

        if selected_rooms:
            results.append(f"Yes {' '.join(selected_rooms)}")
        else:
            results.append("No")

    return results

if __name__ == "__main__":
    households, queries = read_data()
    results = find_slots(households, queries)
    print("\n".join(results))
