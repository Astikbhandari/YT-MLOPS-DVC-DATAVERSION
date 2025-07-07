import pandas as pd
import os

# Step 1: Create initial DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

#print("Initial DataFrame:")
#print(df)

# Step 2: Add new row for V2 using .loc
#df.loc[len(df.index)] = ['V2', 20, 'City1']

# Step 3: Add new row for V3 using .loc
#df.loc[len(df.index)] = ['V3', 30, 'City1']

#print("\nDataFrame After Adding V2 and V3:")
#print(df)

# Step 4: Ensure 'data' directory exists
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Step 5: Save DataFrame to CSV inside 'data' directory
file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)

print(f"\nCSV file saved to {file_path}")

