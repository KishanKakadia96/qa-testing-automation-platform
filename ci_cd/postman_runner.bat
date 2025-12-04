cd "$(dirname "$0")/../testing/postman"
mkdir -p ../../api_automation/reports

echo "🏃 Running Postman Collections..."
newman run collections/*.json \
  -e environments/QA-Testing.postman_environment.json \
  --reporters html,cli \
  --reporter-html-export ../../api_automation/reports/postman_report.html

echo "Report: ../../api_automation/reports/postman_report.html"
