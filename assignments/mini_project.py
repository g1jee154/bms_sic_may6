import pandas as pd

file_name = "marks.xlsx"     
df = pd.read_excel(file_name)

student_column = df.columns[0]

chapter_columns = df.columns[1:]


chapter_stats = pd.DataFrame({
    "Highest Marks": df[chapter_columns].max(),
    "Lowest Marks": df[chapter_columns].min(),
    "Average Marks": df[chapter_columns].mean().round(2)
})


df["Total"] = df[chapter_columns].sum(axis=1)
df["Average"] = df[chapter_columns].mean(axis=1).round(2)

overall_stats = {
    "Overall Highest Mark": df[chapter_columns].max().max(),
    "Overall Lowest Mark": df[chapter_columns].min().min(),
    "Overall Average Mark": round(df[chapter_columns].stack().mean(), 2),
    "Highest Total": df["Total"].max(),
    "Lowest Total": df["Total"].min(),
    "Average Total": round(df["Total"].mean(), 2)
}

overall_df = pd.DataFrame(
    overall_stats.items(),
    columns=["Statistic", "Value"]
)
print("\n========== CHAPTER-WISE STATISTICS ==========\n")
print(chapter_stats)

print("\n========== STUDENT TOTALS ==========\n")
print(df[[student_column, "Total", "Average"]])

print("\n========== OVERALL STATISTICS ==========\n")
print(overall_df)

output_file = "Marks_Analysis.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    chapter_stats.to_excel(writer, sheet_name="Chapter Statistics")
    df.to_excel(writer, sheet_name="Student Statistics", index=False)
    overall_df.to_excel(writer, sheet_name="Overall Statistics", index=False)

print(f"\nAnalysis completed successfully!")
print(f"Results saved to: {output_file}")