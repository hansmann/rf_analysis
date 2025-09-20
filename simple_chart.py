#!/usr/bin/env python3

# School district data: median income vs average teacher salary
district_data = {
    "River Forest SD 90": {"median_income": 135000, "avg_teacher_salary": 85000},
    "Elmhurst CUSD 205": {"median_income": 95000, "avg_teacher_salary": 72000},
    "Downers Grove GSD 58": {"median_income": 105000, "avg_teacher_salary": 78000},
    "Hinsdale CCSD 181": {"median_income": 180000, "avg_teacher_salary": 95000},
    "Oak Park ESD 97": {"median_income": 85000, "avg_teacher_salary": 75000},
    "Lake Forest SD 67": {"median_income": 165000, "avg_teacher_salary": 90000},
    "Glenview CCSD 34": {"median_income": 125000, "avg_teacher_salary": 82000},
    "La Grange SD 102": {"median_income": 140000, "avg_teacher_salary": 88000},
    "Evanston/Skokie SD 65": {"median_income": 90000, "avg_teacher_salary": 70000},
    "Northbrook SD 28": {"median_income": 155000, "avg_teacher_salary": 87000},
    "Berwyn South SD 100": {"median_income": 55000, "avg_teacher_salary": 65000},
    "Elmwood Park CUSD 401": {"median_income": 68000, "avg_teacher_salary": 68000},
    "Naperville CUSD 203": {"median_income": 115000, "avg_teacher_salary": 80000},
    "Wheaton CUSD 200": {"median_income": 88000, "avg_teacher_salary": 73000},
    "Deerfield SD 109": {"median_income": 170000, "avg_teacher_salary": 92000},
    "Oak Brook (Butler 53)": {"median_income": 190000, "avg_teacher_salary": 98000},
    "Park Ridge CCSD 64": {"median_income": 110000, "avg_teacher_salary": 79000}
}

def print_data_table():
    """Print the data in a formatted table."""
    print("Illinois School Districts - Median Income vs Average Teacher Salary")
    print("=" * 80)
    print(f"{'District':<25} {'Median Income':<15} {'Teacher Salary':<15} {'Ratio':<10}")
    print("-" * 80)

    for district, data in district_data.items():
        income = data['median_income']
        salary = data['avg_teacher_salary']
        ratio = salary / income
        print(f"{district:<25} ${income:<14,} ${salary:<14,} {ratio:<10.3f}")

def calculate_statistics():
    """Calculate and print summary statistics."""
    incomes = [data['median_income'] for data in district_data.values()]
    salaries = [data['avg_teacher_salary'] for data in district_data.values()]

    print("\n" + "=" * 50)
    print("SUMMARY STATISTICS")
    print("=" * 50)

    print(f"\nMedian Household Income:")
    print(f"  Min: ${min(incomes):,}")
    print(f"  Max: ${max(incomes):,}")
    print(f"  Average: ${sum(incomes) / len(incomes):,.0f}")

    print(f"\nAverage Teacher Salary:")
    print(f"  Min: ${min(salaries):,}")
    print(f"  Max: ${max(salaries):,}")
    print(f"  Average: ${sum(salaries) / len(salaries):,.0f}")

    # Calculate correlation coefficient
    n = len(incomes)
    sum_x = sum(incomes)
    sum_y = sum(salaries)
    sum_xy = sum(x * y for x, y in zip(incomes, salaries))
    sum_x2 = sum(x * x for x in incomes)
    sum_y2 = sum(y * y for y in salaries)

    correlation = (n * sum_xy - sum_x * sum_y) / ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))**0.5

    print(f"\nCorrelation between Income and Teacher Salary: {correlation:.3f}")

    return incomes, salaries, correlation

def create_simple_chart(incomes, salaries):
    """Create a simple ASCII scatter plot."""
    print("\n" + "=" * 60)
    print("SCATTER PLOT (Income vs Teacher Salary)")
    print("=" * 60)

    # Normalize data for ASCII plot
    min_income, max_income = min(incomes), max(incomes)
    min_salary, max_salary = min(salaries), max(salaries)

    width = 50
    height = 20

    # Create plot grid
    plot = [[' ' for _ in range(width)] for _ in range(height)]

    # Plot points
    for i, (income, salary) in enumerate(zip(incomes, salaries)):
        x = int((income - min_income) / (max_income - min_income) * (width - 1))
        y = int((salary - min_salary) / (max_salary - min_salary) * (height - 1))
        y = height - 1 - y  # Flip y-axis

        if 0 <= x < width and 0 <= y < height:
            plot[y][x] = '*'

    # Print plot
    print(f"Teacher Salary (${min_salary:,} to ${max_salary:,})")
    for row in plot:
        print(''.join(row))
    print(' ' * 25 + f"Income (${min_income:,} to ${max_income:,})")

def save_csv_data():
    """Save data to CSV format."""
    csv_content = "District,Median_Income,Avg_Teacher_Salary\n"
    for district, data in district_data.items():
        csv_content += f'"{district}",{data["median_income"]},{data["avg_teacher_salary"]}\n'

    with open('/Users/willhansmann/code/illinois_districts_data.csv', 'w') as f:
        f.write(csv_content)

    print(f"\nData saved to: /Users/willhansmann/code/illinois_districts_data.csv")

if __name__ == "__main__":
    print_data_table()
    incomes, salaries, correlation = calculate_statistics()
    create_simple_chart(incomes, salaries)
    save_csv_data()

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)