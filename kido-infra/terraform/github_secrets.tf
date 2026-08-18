# --- Quản lý Secrets cho các Repositories ---



# 2. Inject Secrets vào repo danang-badminton-hub
resource "github_actions_secret" "badminton_vps_host" {
  repository      = "danang-badminton-hub"
  secret_name     = "VPS_HOST"
  plaintext_value = data.sops_file.secrets.data["shared_vps_host"]
}


# 3. Inject Secrets tương tự vào repo vietnam-market-scraper
resource "github_actions_secret" "scraper_vps_host" {
  repository      = "vietnam-market-scraper"
  secret_name     = "VPS_HOST"
  plaintext_value = data.sops_file.secrets.data["shared_vps_host"]
}

resource "github_actions_secret" "scraper_vapid_public_key" {
  repository      = "vietnam-market-scraper"
  secret_name     = "VAPID_PUBLIC_KEY"
  plaintext_value = data.sops_file.secrets.data["vapid_public_key"]
}

resource "github_actions_secret" "scraper_vapid_private_key" {
  repository      = "vietnam-market-scraper"
  secret_name     = "VAPID_PRIVATE_KEY"
  plaintext_value = data.sops_file.secrets.data["vapid_private_key"]
}

# --- Inject Secrets into repo checkin-app ---
resource "github_actions_secret" "checkin_vps_host" {
  repository      = "checkin-app"
  secret_name     = "VPS_HOST"
  plaintext_value = data.sops_file.secrets.data["shared_vps_host"]
}

resource "github_actions_secret" "checkin_ssh_user" {
  repository      = "checkin-app"
  secret_name     = "SSH_USER"
  plaintext_value = "root"
}

resource "github_actions_secret" "checkin_ssh_private_key" {
  repository      = "checkin-app"
  secret_name     = "SSH_PRIVATE_KEY"
  plaintext_value = file("~/.ssh/id_rsa")
}

# --- Inject Secrets into repo kido-infra ---
resource "github_actions_secret" "infra_vps_host" {
  repository      = "kido-infra"
  secret_name     = "VPS_HOST"
  plaintext_value = data.sops_file.secrets.data["shared_vps_host"]
}

resource "github_actions_secret" "infra_ssh_user" {
  repository      = "kido-infra"
  secret_name     = "SSH_USER"
  plaintext_value = "root"
}

resource "github_actions_secret" "infra_ssh_private_key" {
  repository      = "kido-infra"
  secret_name     = "SSH_PRIVATE_KEY"
  plaintext_value = file("~/.ssh/id_rsa")
}

