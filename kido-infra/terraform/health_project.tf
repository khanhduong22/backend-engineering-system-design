# --- Personal Health Record (PHR) Project ---

resource "github_repository" "health" {
  name        = "health"
  description = "Personal Health Record (PHR) Dashboard & AI Vision OCR Services"
  visibility  = "private"
  auto_init   = false
}

resource "github_actions_secret" "health_vps_ip" {
  repository      = github_repository.health.name
  secret_name     = "VPS_IP"
  plaintext_value = data.sops_file.secrets.data["shared_vps_host"]
}

resource "github_actions_secret" "health_ssh_user" {
  repository      = github_repository.health.name
  secret_name     = "SSH_USER"
  plaintext_value = "root"
}

resource "github_actions_secret" "health_ssh_private_key" {
  repository      = github_repository.health.name
  secret_name     = "SSH_PRIVATE_KEY"
  plaintext_value = file("~/.ssh/id_rsa")
}
