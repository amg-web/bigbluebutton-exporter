# BigBlueButton Exporter
Prometheus exporter for BigBlueButton.
On a HTTP `/metrics` request, the exporter will query the BigBlueButton's API for data which it then aggregates and exposes as Prometheus metrics.

![GitHub](https://img.shields.io/github/license/greenstatic/bigbluebutton-exporter)

Default port: 9688
Default bind IP: 0.0.0.0

## Documentation
Available at: [https://bigbluebutton-exporter.greenstatic.dev](https://bigbluebutton-exporter.greenstatic.dev)

## Grafana Dashboard Screenshots

![](docs/assets/img_grafana_dashboard_all_servers.png)

![](docs/assets/img_grafana_dashboard_server_instance.png)

## Metrics
See: [Exporter User Guide - Metrics](https://bigbluebutton-exporter.greenstatic.dev/exporter-user-guide/#metrics).

## Environment Variables
See: [Exporter User Guide - Environment Variables](https://bigbluebutton-exporter.greenstatic.dev/exporter-user-guide/#environment-variables).

## CHANGELOG
18.05.2026
- Python and dependencies updated
- add ENV variable FQDN (API_BASE_URL still can be used instead)
- Grafana Dashboard is compatible with newer Grafana versions
- Records count by API uses limit key and get data from totalElements tag
- Add possibbility to count ended meetings by counting number of files (it will be dropped if server migrated without status dir)
- node exporter mounts filter items added for clener result.
- grafana provisioning folder
- grafans security env vars
- bbb-exporter is bulding localy instead of pulling from docker hub (anyway it's very fast)
- other minor changes