import pandas as pd
from datetime import datetime

# Create a random DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create the tiprank folder if it doesn't exist
if not os.path.exists('tiprank'):
    os.makedirs('tiprank')


# Create CSV filename with current date and time
csv_filename = f"tiprank/data_{current_datetime}.csv"
  
# Dump dataframe to CSV
df.to_csv(csv_filename, index=False)

print(f"DataFrame dumped to {csv_filename}")
