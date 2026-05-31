def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
       
        merged[key] = merged.get(key, 0) + value
    return merged

if __name__ == "__main__":
    d1 = {'math': 90, 'science': 85, 'history': 70}
    d2 = {'science': 10, 'history': 15, 'art': 88}
    
    print(f"Dictionary 1: {d1}")
    print(f"Dictionary 2: {d2}")
    print(f"Merged Dictionary: {merge_dictionaries(d1, d2)}")