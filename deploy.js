'use strict';

const Octokit = require('@octokit/rest');
const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN
});

const [owner, repo] = process.env.GITHUB_REPOSITORY.split('/');
const ref = process.env.GITHUB_REF;

async function main() {
  const deployment = (await octokit.repos.createDeployment({
    owner,
    repo,
    ref,
    required_contexts: [], // ignore failing checks and statuses
    environment: 'staging',
  })).data;

  console.log(deployment);

  await octokit.repos.createDeploymentStatus({
    owner,
    repo,
    deployment_id: deployment.id,
    state: 'success',
    environment_url: 'https://019df89ad-dot-ecosystem-infra-rotation.appspot.com/',
    log_url: 'https://github.com/foolip/ecosystem-infra-rotation/actions',
  });
}

main().catch(reason => {
  console.error(reason);
  process.exit(1)
});
