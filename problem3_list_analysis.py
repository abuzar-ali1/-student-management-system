def analyze_list(numbers):
    if not numbers:
        return None
    
    maximum = max(numbers)
    minimum = min(numbers)
    avg = sum(numbers) / len(numbers)
    
    # List comprehension to find numbers above average
    above_avg = [num for num in numbers if num > avg]
    
    return {
        "Maximum": maximum,
        "Minimum": minimum,
        "Average": avg,
        "Above Average": above_avg
    }

if __name__ == "__main__":
    sample_list = [10, 25, 30, 45, 50, 15]
    print(f"Analyzing list: {sample_list}\n")
    
    results = analyze_list(sample_list)
    for key, value in results.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")