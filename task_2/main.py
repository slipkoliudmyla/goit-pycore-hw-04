

def get_cats_info(path):

    try:
        with open(path, encoding="utf-8") as file:
            cats_info =[]
            for cat in file:
                parts = cat.strip().split(",")
                if len(parts) == 3:
                    cat_id = parts[0]
                    cat_name = parts[1]
                    cat_age = parts[2]
                    cat_dict = {"id": cat_id, "name": cat_name, "age": cat_age}
                    cats_info.append(cat_dict)
        return cats_info
    except FileNotFoundError:
        print("Галя, ну шо хорошого як в хаті нема кота")
        return []
    
cats = get_cats_info("cats_file.txt")
print(cats)