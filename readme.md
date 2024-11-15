# SCOPE - Subdomain Cache Observation, Poisoning & Evaluation


<p align="center">
  <img src="https://github.com/user-attachments/assets/fb2e6570-6f07-4c94-846c-fa09d4e0c47d" alt="image"/>
</p>

**SCOPE** is a Python-based tool designed to identify cache poisoning vulnerabilities in subdomains. It performs the following operations for each subdomain in a given list:

1. **Sends a PURGE request** to clear the cache.
2. **Checks for a specific cache hit** (`X-Cache-Hits: 1`).
3. **Attempts a GET request** with an illegal header to poison the cache.
4. **Verifies if the page is cached** and accessible, indicating a potential vulnerability.

---

## Features 

- **Automated cache poisoning testing** for multiple subdomains.
- **Checks for `X-Cache-Hits: 1`** to identify cache-related vulnerabilities.
- **Easy integration with a list of subdomains** via a `.txt` file.
- **Terminal-based** for efficient usage.

---

## Installation

### Prerequisites

- Python 3.x
- `curl` installed (used for sending HTTP requests)

### Step-by-Step Setup

1. Clone or download the **SCOPE** repository:

    ```bash
    git clone https://github.com/yourusername/scope.git
    cd scope
    ```

2. Install dependencies (if any) and make sure Python 3 is installed:

    ```bash
    pip install -r requirements.txt  # If you have any dependencies listed
    ```

---

## Usage


## Usage
### Step 1: Prepare the Subdomain List
Create a `subdomain.txt` file, and list all the subdomains you want to test (one per line). Example:
```
subdomain1.example.com
subdomain2.example.com
subdomain3.example.com
```
### Step 2: Run the Tool
Execute the script with the path to your `subdomain.txt` file:
```bash
python3 scope.py /path/to/subdomain.txt
```
The tool will process each subdomain in the file and perform the following checks:
- Sends a PURGE request.
- Looks for `X-Cache-Hits: 1` to determine if the subdomain is vulnerable.
- Attempts to poison the cache with an illegal header.
- Verifies if the random path is cached and accessible.
### Output
- For each subdomain, you will receive output like the following:
    ```
    [SCOPE] Testing subdomain1.example.com - Sending PURGE request...
    [SCOPE] X-Cache-Hits: 1 found - Potentially vulnerable. Proceeding with GET request...
    [SCOPE] Vulnerable! Cached page accessible at: https://subdomain1.example.com/random-path
    ```
- If the subdomain is not vulnerable, the output will indicate that no cache poisoning was detected.


