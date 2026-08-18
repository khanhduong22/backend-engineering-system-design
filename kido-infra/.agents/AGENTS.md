# Infrastructure Directives & Automation Standards (kido-infra)

## 1. Automated PoC & Showcase App Provisioning Pipeline
Whenever a new PoC or Showcase API App is created in the study roadmap:
- **Cloudflare DNS:** Add a new record in `terraform/cloudflare_dns.tf` pointing `<poc-name>.kido.app` to Contabo VPS IP.
- **Nginx Proxy Manager:** Configure reverse proxy routing from port 80/443 to container internal port.
- **Dozzle Container Logs:** Ensure container is attached to Docker network monitored by Dozzle log manager.
- **SigNoz APM:** Ensure OTEL exporter env var points to `http://signoz-otel-collector:4318`.

## 2. Infrastructure Safety Rules
- **Never Reset DBs:** Do not run destructive database reset commands without explicit user confirmation.
- **Secrets via SOPS:** Never commit raw API tokens or credentials; use `secrets.enc.json` with SOPS encryption.
