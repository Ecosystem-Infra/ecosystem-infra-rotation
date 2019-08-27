'use strict';

const Octokit = require('@octokit/rest');

async function main() {
  const octokit = new Octokit({
    auth: process.env.GITHUB_TOKEN
  });

  const [owner, repo] = process.env.GITHUB_REPOSITORY.split('/');
  const ref = process.env.GITHUB_SHA;

  console.log(owner, repo, ref);

  const deployment = (await octokit.repos.createDeployment({
    owner,
    repo,
    ref,
  })).data;

  console.log(deployment);

  await octokit.repos.createDeploymentStatus({
    owner,
    repo,
    deployment_id: deployment.id,
    state: 'success',
    target_url: 'https://target-dot-ecosystem-infra-rotation.appspot.com/',
    environment_url: 'https://env-dot-ecosystem-infra-rotation.appspot.com/'
  });
}

main().catch(reason => {
  console.error(reason);
  process.exit(1)
});
