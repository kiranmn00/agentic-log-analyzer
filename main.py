from analyzer import analyze_log

with open("sample_logs/sync_error.txt") as f:
    log = f.read()

result = analyze_log(log)

print(result)
