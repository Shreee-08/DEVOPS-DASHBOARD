import os
import requests


def analyze_log(log_input):
    """Analyze log data from a file path or a list of log lines."""
    try:
        if isinstance(log_input, list):
            lines = log_input
        else:
            with open(log_input, "r", encoding="utf-8") as f:
                lines = f.readlines()
    except FileNotFoundError:
        print(f"⚠️ File not found: {log_input}")
        return {"errors": 0, "warnings": 0}
    except OSError as e:
        print(f"⚠️ OS error: {e}")
        return {"errors": 0, "warnings": 0}

    # Count errors and warnings
    errors = sum(1 for line in lines if "ERROR" in line)
    warnings = sum(1 for line in lines if "WARNING" in line)

    # Write summary
    with open("log_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Errors={errors}\nWarnings={warnings}\n")

    # Push metrics to Prometheus Pushgateway (if configured)
    pushgateway_url = os.getenv("PUSHGATEWAY_URL")
    if pushgateway_url:
        try:
            payload = (
                f"# TYPE log_errors gauge\nlog_errors {errors}\n"
                f"# TYPE log_warnings gauge\nlog_warnings {warnings}\n"
            )
            response = requests.post(
                f"{pushgateway_url}/metrics/job/log_analyzer",
                data=payload,
                timeout=5,
            )
            if response.status_code in [200, 202]:
                print("✅ Metrics pushed to Prometheus Pushgateway successfully.")
            else:
                print(f"⚠️ Pushgateway responded with {response.status_code}")
        except (OSError, ValueError, requests.RequestException) as e:
            print(f"⚠️ Something went wrong: {e}")

    return {"errors": errors, "warnings": warnings}


if __name__ == "__main__":
    user_input_path = input("Enter log file path: ").strip()
    result = analyze_log(user_input_path)
    print(f"✅ Analysis complete: {result}")
