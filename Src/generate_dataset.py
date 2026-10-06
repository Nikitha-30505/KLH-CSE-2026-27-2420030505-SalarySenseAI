import pandas as pd
import random

random.seed(42)

job_titles = [
    "Software Engineer", "Data Analyst", "Data Scientist",
    "HR Manager", "Project Manager", "Marketing Executive",
    "Sales Executive", "Business Analyst", "Accountant",
    "Network Engineer", "UI/UX Designer", "DevOps Engineer"
]

education_levels = [
    "High School",
    "Bachelor's",
    "Master's",
    "PhD"
]

industries = [
    "IT",
    "Finance",
    "Healthcare",
    "Education",
    "Retail",
    "Manufacturing"
]

locations = [
    "Hyderabad",
    "Bangalore",
    "Chennai",
    "Mumbai",
    "Pune",
    "Delhi"
]

company_sizes = [
    "Small",
    "Medium",
    "Large"
]

gender = ["Male", "Female"]

education_bonus = {
    "High School": 0,
    "Bachelor's": 5000,
    "Master's": 12000,
    "PhD": 22000
}

company_bonus = {
    "Small": 0,
    "Medium": 8000,
    "Large": 18000
}

industry_bonus = {
    "IT": 15000,
    "Finance": 12000,
    "Healthcare": 9000,
    "Education": 4000,
    "Retail": 5000,
    "Manufacturing": 7000
}

job_bonus = {
    "Software Engineer": 15000,
    "Data Analyst": 12000,
    "Data Scientist": 25000,
    "HR Manager": 10000,
    "Project Manager": 20000,
    "Marketing Executive": 7000,
    "Sales Executive": 8000,
    "Business Analyst": 15000,
    "Accountant": 9000,
    "Network Engineer": 12000,
    "UI/UX Designer": 13000,
    "DevOps Engineer": 22000
}

records = []

for _ in range(5000):

    age = random.randint(21, 60)

    exp = random.randint(0, min(25, age - 20))

    edu = random.choice(education_levels)

    job = random.choice(job_titles)

    ind = random.choice(industries)

    loc = random.choice(locations)

    comp = random.choice(company_sizes)

    gen = random.choice(gender)

    salary = (
        25000
        + exp * 4500
        + education_bonus[edu]
        + company_bonus[comp]
        + industry_bonus[ind]
        + job_bonus[job]
        + random.randint(-5000, 5000)
    )

    salary = max(30000, salary)

    records.append([
        age,
        gen,
        edu,
        job,
        exp,
        ind,
        loc,
        comp,
        salary
    ])

df = pd.DataFrame(records, columns=[
    "Age",
    "Gender",
    "Education_Level",
    "Job_Title",
    "Years_of_Experience",
    "Industry",
    "Location",
    "Company_Size",
    "Salary"
])

df.to_csv("dataset/salary_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("\nShape:", df.shape)