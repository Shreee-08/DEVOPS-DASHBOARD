import os

def analyze_log(file_path):
    """Analyze log file for errors and warnings and return summary."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"⚠️ File not found: {file_path}")
        return {"errors": 0, "warnings": 0}
    except Exception as e:  # catch-all as fallback
        print(f"⚠️ Something went wrong: {e}")
        return {"errors": 0, "warnings": 0}

    errors = sum(1 for line in lines if "ERROR" in line)
    warnings = sum(1 for line in lines if "WARNING" in line)

    # Write summary to log_summary.txt
    summary_file = "log_summary.txt"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(f"Errors={errors}\nWarnings={warnings}\n")
    return {"errors": errors, "warnings": warnings}

if __name__ == "__main__":
    file_path = input("Enter log file path: ").strip()
    result = analyze_log(file_path)
    print(f"✅ Analysis complete: {result}")
