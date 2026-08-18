# Workspace Rules & AI Agent Directives (AGENTS.md)

## 1. Auto-Update Anki Deck Collection Summary
Whenever any Anki deck, note, or card collection in this workspace is created, modified, re-ordered, cleaned, or deduplicated:
- **Mandatory Action:** ALWAYS run `python3 scripts/summarize_all_be_decks.py` to regenerate `final/DECK_COLLECTION_SUMMARY.md`.
- **User Notification:** Provide a brief summary of the updated deck collection stats to the user after every change.

## 2. High-ROI Backend Engineering Study Order
Always maintain the 9-domain high-ROI study sequence:
1. `01_DesignPatterns_OOP` (GoF + SOLID + OOP + DDD)
2. `02_Redis_Caching` (Pure Redis & Caching)
3. `03_Kafka_EventDriven` (Kafka & Event Streaming)
4. `04_SQL_PostgreSQL_Mastery` (PostgreSQL Internals & SQL)
5. `05_Storage_DDIA` (Distributed Data & DDIA)
6. `06_SystemDesign_Architecture` (Pure System Design & Microservices)
7. `07_Networking_Security` (Networking & Security Protocols)
8. `08_ComputerScience_SWE_optional` (CS Core - Optional Reference)
9. `09_WebDev_GeneralCS_optional` (General Web Dev & API Params - Optional Reference)

## 3. Card UI Master Model v3 Standards
All cards must use `Backend Master Model v3` with:
- Dual Badges (`Category` + `SubCategory`) on top-left.
- Level Badge (`Junior` 🟢, `Mid` 🟡, `Senior` 🔴) on top-right.
- Book Source Citation at bottom footer.
- High-performance zero-lag CSS with lazy JS loading for Mermaid diagrams.

## 4. Mandatory Docker Compose Standard per PoC & Showcase App
Every PoC Module (`pocs/poc01-...`) and Showcase API App (`showcase-apps/app01-...`) MUST:
- Be organized as an independent Standalone GitHub Repository (`github.com/khanhduong22/<module-name>`).
- Contain a dedicated `docker-compose.yml` for unified local & cloud container orchestration (App, Redis, DB, Workers).

## 5. Mandatory CI/CD GitHub Actions Auto-Deploy Standard
Every PoC & Showcase App MUST include a GitHub Actions workflow (`.github/workflows/deploy.yml`) that:
- Automatically builds the Docker image on `push` to `main`.
- Deploys the updated container to Contabo VPS via SSH & Docker Compose.

## 6. Contabo VPS Subdomain Deployment & Monitoring via `kido-infra`
Infrastructure automation for all PoCs and Showcase Apps MUST leverage `kido-infra`:
- **Subdomain Provisioning:** Automated Cloudflare DNS Subdomain (`<module-name>.kido.app`) using Terraform (`kido-infra/terraform/cloudflare_dns.tf`).
- **Nginx Reverse Proxy:** Route traffic through Nginx Proxy Manager to internal container port.
- **Observability & Monitoring:** Live container logs via Dozzle (`kido-infra/common/dozzle_nginx.conf`) + APM metrics via SigNoz (`kido-infra/signoz/docker-compose.yaml`).
