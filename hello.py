salaries = []

salaries.append(100000)
salaries.append(23000)
salaries.append(30000)
salaries.append(40000)

# salaries.pop()

# salaries.pop(1)


# salaries.remove(100000)
print(salaries)
search = 40000
i = 0
search_index = -1
for salary in salaries:
    if salary == search:
        search_index = i
        break
    i += 1

print(search_index)