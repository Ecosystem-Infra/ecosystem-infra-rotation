workflow "build & deploy" {
  on = "push"
  resolves = ["deploy"]
}

action "build" {
  uses = "actions/npm@master"
  args = "install"
}

action "filter" {
  uses = "actions/bin/filter@master"
  needs = ["build"]
  args = "branch master"
}

action "secrets" {
  uses = "actions/bin/sh@master"
  args = ["echo \"$SECRETS_JSON\" | base64 --decode > secrets.json"]
  needs = ["filter"]
  secrets = ["SECRETS_JSON"]
}

action "authenticate" {
  uses = "actions/gcloud/auth@master"
  needs = ["secrets"]
  secrets = ["GCLOUD_AUTH"]
}

action "deploy" {
  uses = "actions/gcloud/cli@master"
  args = "./deploy.sh"
  needs = ["authenticate"]
}
