workflow "Build & Deploy" {
  on = "push"
  resolves = ["Deploy"]
}

action "Build" {
  uses = "actions/npm@master"
  args = "install"
}

action "Filter" {
  uses = "actions/bin/filter@master"
  needs = ["Build"]
  args = "branch master"
}

action "Authenticate" {
  uses = "actions/gcloud/auth@master"
  needs = ["Filter"]
  secrets = ["GCLOUD_AUTH"]
}

action "Deploy" {
  uses = "actions/gcloud/cli@master"
  args = "./deploy.sh"
  needs = ["Authenticate"]
}
