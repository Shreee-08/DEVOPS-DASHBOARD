def analyze_log(log_input):
    """Analyze log data from a file path or a list of log lines."""
    try:
        if isinstance(log_input, list):  # Case 1: test passes a list
            lines = log_input
        else:  # Case 2: user provides a file path
            with open(log_input, "r", encoding="utf-8") as f:
                lines = f.readlines()
    except FileNotFoundError:
        print(f"⚠️ File not found: {log_input}")
        return {"errors": 0, "warnings": 0}
    except OSError as e:  # narrower than Exception
        print(f"⚠️ OS error: {e}")
        return {"errors": 0, "warnings": 0}

    errors = sum(1 for line in lines if "ERROR" in line)
    warnings = sum(1 for line in lines if "WARNING" in line)

    # Write summary to log_summary.txt
    with open("log_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Errors={errors}\nWarnings={warnings}\n")

    return {"errors": errors, "warnings": warnings}


if __name__ == "__main__":
    user_input_path = input("Enter log file path: ").strip()
    result = analyze_log(user_input_path)
    print(f"✅ Analysis complete: {result}")
