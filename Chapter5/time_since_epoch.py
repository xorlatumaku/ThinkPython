# Date: 06/05/2025
# Program to display time since epoch
from time import time

# Get current timestamp (seconds since epoch)
now = time()

# Constants for time conversions
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
SECONDS_PER_DAY = SECONDS_PER_HOUR * HOURS_PER_DAY

# Calculate days since epoch
days_since_epoch = int(now // SECONDS_PER_DAY)

# Calculate remaining seconds after removing complete days
remaining_seconds = int(now % SECONDS_PER_DAY)

# Calculate hours, minutes, and seconds
hours = remaining_seconds // SECONDS_PER_HOUR
remaining_seconds = remaining_seconds % SECONDS_PER_HOUR

minutes = remaining_seconds // SECONDS_PER_MINUTE
seconds = remaining_seconds % SECONDS_PER_MINUTE

# Print results
print(f"Days since epoch: {days_since_epoch}")
print(f"Current time (UTC): {hours:02d}:{minutes:02d}:{seconds:02d}")
