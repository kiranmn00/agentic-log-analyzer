from analyzer import analyze_log, generate_report

with open("sample_logs/sync_error.txt", "r") as file:

    log_text = file.read()

analysis = analyze_log(log_text)

report = generate_report(analysis)

print(report)

with open("output/sample_analysis.txt", "w") as file:

    file.write(report)
