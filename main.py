# main.py

import os

def analyze_log(log_input):
    """
    Accepts either a file path (str) or a list of log lines.
    Returns dict: {'errors': int, 'warnings': int}
    """
    try:
        if isinstance(log_input, str):  # it's a file path
            if not os.path.exists(log_input):
                print(f"⚠️ File not found: {log_input}")
                return None
            with open(log_input, 'r') as f:
                logs = f.readlines()
        elif isinstance(log_input, list):  # already a list of strings
            logs = log_input
        else:
            print("⚠️ Something went wrong: expected str, bytes or os.PathLike object, not", type(log_input))
            return None

        errors = sum(1 for line in logs if "ERROR" in line)
        warnings = sum(1 for line in logs if "WARNING" in line)

        return {'errors': errors, 'warnings': warnings}

    except Exception as e:
        print("⚠️ Something went wrong:", e)
        return None


if __name__ == "__main__":
    print("=== Simple Log Analyzer ===")
    log_path = input("Enter path to log file: ").strip()
    result = analyze_log(log_path)
    if result is not None:
        print(f"Errors: {result['errors']}, Warnings: {result['warnings']}")
    else:
        print("No result could be generated.")
