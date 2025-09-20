import json

# School districts to analyze
districts = [
    "River Forest SD 90",
    "Elmhurst CUSD 205",
    "Downers Grove GSD 58",
    "Hinsdale CCSD 181",
    "Oak Park ESD 97",
    "Lake Forest SD 67",
    "Glenview CCSD 34",
    "La Grange SD 102",
    "Evanston/Skokie SD 65",
    "Northbrook SD 28",
    "Berwyn South SD 100",
    "Elmwood Park CUSD 401",
    "Naperville CUSD 203",
    "Wheaton CUSD 200",
    "Deerfield SD 109",
    "Oak Brook (Butler 53)",
    "Park Ridge CCSD 64"
]

# Manually collected data from various sources (Census, Illinois Report Card, etc.)
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

def create_data_list():
    """Create a list of data from the district data."""
    data = []
    for district, values in district_data.items():
        data.append({
            'District': district,
            'Median_Income': values['median_income'],
            'Avg_Teacher_Salary': values['avg_teacher_salary']
        })
    return data

def create_scatter_plot(df: pd.DataFrame) -> None:
    """Create a scatter plot comparing median income vs average teacher salary."""
    plt.figure(figsize=(14, 10))

    # Create scatter plot
    plt.scatter(df['Median_Income'], df['Avg_Teacher_Salary'],
               s=100, alpha=0.7, color='steelblue', edgecolors='black', linewidth=1)

    # Add labels for each point
    for i, row in df.iterrows():
        plt.annotate(row['District'],
                    (row['Median_Income'], row['Avg_Teacher_Salary']),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8, ha='left')

    # Add trend line
    z = np.polyfit(df['Median_Income'], df['Avg_Teacher_Salary'], 1)
    p = np.poly1d(z)
    plt.plot(df['Median_Income'], p(df['Median_Income']), "r--", alpha=0.8, linewidth=2)

    plt.xlabel('Median Household Income ($)', fontsize=12)
    plt.ylabel('Average Teacher Salary ($)', fontsize=12)
    plt.title('Median Income vs Average Teacher Salary\nIllinois School Districts', fontsize=14, fontweight='bold')

    # Format axes
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Calculate correlation
    correlation = df['Median_Income'].corr(df['Avg_Teacher_Salary'])
    plt.text(0.02, 0.98, f'Correlation: {correlation:.3f}',
             transform=plt.gca().transAxes, fontsize=10,
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.savefig('/Users/willhansmann/code/illinois_districts_chart.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_summary_stats(df: pd.DataFrame) -> None:
    """Print summary statistics."""
    print("\n=== SUMMARY STATISTICS ===")
    print(f"Number of districts: {len(df)}")
    print(f"\nMedian Income:")
    print(f"  Min: ${df['Median_Income'].min():,}")
    print(f"  Max: ${df['Median_Income'].max():,}")
    print(f"  Mean: ${df['Median_Income'].mean():,.0f}")
    print(f"  Median: ${df['Median_Income'].median():,.0f}")

    print(f"\nAverage Teacher Salary:")
    print(f"  Min: ${df['Avg_Teacher_Salary'].min():,}")
    print(f"  Max: ${df['Avg_Teacher_Salary'].max():,}")
    print(f"  Mean: ${df['Avg_Teacher_Salary'].mean():,.0f}")
    print(f"  Median: ${df['Avg_Teacher_Salary'].median():,.0f}")

    correlation = df['Median_Income'].corr(df['Avg_Teacher_Salary'])
    print(f"\nCorrelation between Median Income and Teacher Salary: {correlation:.3f}")

if __name__ == "__main__":
    import numpy as np

    # Create DataFrame
    df = create_dataframe()

    # Display the data
    print("Illinois School Districts - Median Income vs Average Teacher Salary")
    print("=" * 70)
    print(df.to_string(index=False))

    # Print summary statistics
    print_summary_stats(df)

    # Create visualization
    create_scatter_plot(df)

    print(f"\nChart saved as: /Users/willhansmann/code/illinois_districts_chart.png")