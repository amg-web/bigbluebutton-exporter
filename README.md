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
19.05.2026
- bbb-exporter Python and dependencies updated
- bbb-exporter new ENV variable FQDN (API_BASE_URL still can be used instead)
- bbb-exporter use sha256 by default, can be change to any  supported by BBB type
- bbb-exporter count records by API uses limit key and get data from **totalElements** tag
- bbb-exporter add possibility to count ended meetings by counting number of files (it will be dropped if server migrated without status dir)
- bbb-exporter is building locally instead of pulling from docker hub (anyway it's very fast)
- node exporter mounts and NIC filter items added for cleaner result
- Grafana provisioning folder
- Grafana security env vars
- Grafana Dashboards v2 are compatible with Grafana 13 (actual version on the moment update)
- Grafana automatic datasource provisioning
- other minor changes