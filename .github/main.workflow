workflow "Build & Deploy" {
  on = "push"
  resolves = ["Deploy"]
}

action "Build" {
  uses = "actions/npm@master"
  runs = "./build.sh"
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
  needs = ["Authenticate"]
  runs = "./deploy.sh"
}
