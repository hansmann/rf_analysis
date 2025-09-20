#!/usr/bin/env python3

# Real Illinois School District Data
# Sources: US Census Bureau 2023 ACS, Illinois Report Card

real_data = [
    {"district": "River Forest SD 90", "income": 148711, "salary": 77630},
    {"district": "Hinsdale CCSD 181", "income": 250001, "salary": 94341},
    {"district": "Oak Park ESD 97", "income": 108026, "salary": 81158},
    {"district": "Evanston/Skokie SD 65", "income": 95766, "salary": 70608},
    {"district": "Naperville CUSD 203", "income": 150937, "salary": 57260},
    {"district": "Wheaton CUSD 200", "income": 119566, "salary": 73947},
    {"district": "Deerfield SD 109", "income": 189705, "salary": 85000},
    {"district": "Oak Brook (Butler 53)", "income": 171123, "salary": 86720},
    {"district": "Park Ridge CCSD 64", "income": 138059, "salary": 80500},
    {"district": "Downers Grove GSD 58", "income": 119649, "salary": 58515}
]

def calculate_correlation(x_values, y_values):
    """Calculate Pearson correlation coefficient."""
    n = len(x_values)
    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x * x for x in x_values)
    sum_y2 = sum(y * y for y in y_values)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))**0.5

    return numerator / denominator if denominator != 0 else 0

def analyze_data():
    """Analyze the real district data."""
    print("REAL ILLINOIS SCHOOL DISTRICT DATA ANALYSIS")
    print("=" * 60)
    print("Sources: US Census Bureau 2023 ACS, Illinois Report Card")
    print()

    # Extract data
    incomes = [d["income"] for d in real_data]
    salaries = [d["salary"] for d in real_data]

    # Print table
    print(f"{'District':<25} {'Income':<12} {'Salary':<12} {'Ratio':<8}")
    print("-" * 60)
    for d in sorted(real_data, key=lambda x: x["income"], reverse=True):
        ratio = d["salary"] / d["income"]
        print(f"{d['district']:<25} ${d['income']:<11,} ${d['salary']:<11,} {ratio:<8.3f}")

    # Calculate statistics
    print(f"\nSUMMARY STATISTICS (n={len(real_data)})")
    print("-" * 30)
    print(f"Median Income:")
    print(f"  Range: ${min(incomes):,} - ${max(incomes):,}")
    print(f"  Average: ${sum(incomes) / len(incomes):,.0f}")
    print(f"  Median: ${sorted(incomes)[len(incomes)//2]:,}")

    print(f"\nTeacher Salary:")
    print(f"  Range: ${min(salaries):,} - ${max(salaries):,}")
    print(f"  Average: ${sum(salaries) / len(salaries):,.0f}")
    print(f"  Median: ${sorted(salaries)[len(salaries)//2]:,}")

    # Calculate correlation
    correlation = calculate_correlation(incomes, salaries)
    print(f"\nCorrelation (Income vs Salary): {correlation:.3f}")

    if correlation > 0.7:
        strength = "Strong positive"
    elif correlation > 0.3:
        strength = "Moderate positive"
    elif correlation > -0.3:
        strength = "Weak"
    elif correlation > -0.7:
        strength = "Moderate negative"
    else:
        strength = "Strong negative"

    print(f"Correlation strength: {strength}")

    # Notable findings
    print(f"\nNOTABLE FINDINGS:")
    print("-" * 20)

    highest_income = max(real_data, key=lambda x: x["income"])
    highest_salary = max(real_data, key=lambda x: x["salary"])
    lowest_ratio = min(real_data, key=lambda x: x["salary"]/x["income"])
    highest_ratio = max(real_data, key=lambda x: x["salary"]/x["income"])

    print(f"• Highest income: {highest_income['district']} (${highest_income['income']:,})")
    print(f"• Highest salary: {highest_salary['district']} (${highest_salary['salary']:,})")
    print(f"• Lowest salary/income ratio: {lowest_ratio['district']} ({lowest_ratio['salary']/lowest_ratio['income']:.3f})")
    print(f"• Highest salary/income ratio: {highest_ratio['district']} ({highest_ratio['salary']/highest_ratio['income']:.3f})")

    # State comparison
    illinois_median_income = 81702  # 2023 state median
    illinois_avg_teacher_salary = 75978  # approximate state average

    print(f"\nSTATE COMPARISON:")
    print("-" * 20)
    print(f"Illinois median income: ${illinois_median_income:,}")
    print(f"Illinois avg teacher salary: ~${illinois_avg_teacher_salary:,}")
    print(f"These districts avg income: ${sum(incomes) / len(incomes):,.0f} ({(sum(incomes) / len(incomes)) / illinois_median_income:.1f}x state)")
    print(f"These districts avg salary: ${sum(salaries) / len(salaries):,.0f} ({(sum(salaries) / len(salaries)) / illinois_avg_teacher_salary:.1f}x state)")

if __name__ == "__main__":
    analyze_data()