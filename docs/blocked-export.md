These are export PRs which the exporter should have merged by now.

Usually this is caused by failing TaskCluster checks. Read the TaskCluster logs to understand the failure.

A common problem is the TaskCluster stability check failing, which indicates
that a test is flaky. This is very often a problem with the test itself and will
require help from the author, so deflaking these can take some time. To avoid
these PRs from piling up we aim to clear them from the queue and apply a fix in
the background.

Follow these steps (see [#23617](https://github.com/web-platform-tests/wpt/pull/23617) for a recent example):
- copy the "Unstable Results" from the TaskCluster log into the PR for easier
  viewing.
- create a crbug to record the flake, which should point to the PR and be assigned to the CL author.
- reference the new bug in the PR.
- force merge the PR.

Another common cause of failure is that [when many tests are affected, TaskCluster jobs will time out](https://github.com/web-platform-tests/wpt/issues/7660). The timeout is at around 120 minutes. When this happens, the PR has to be force merged. Link to [#7660](https://github.com/web-platform-tests/wpt/issues/7660) in a comment and ask @stephenmcgruer or @Hexcles to merge the PR.

If the failure looks unrelated to the code changes, first rebase and force push the branch. This will both bring in any recent fixes to the problem and trigger a new TaskCluster run. If that doesn't fix the problem and other PRs are also affected, [file a wpt infra bug](https://github.com/web-platform-tests/wpt/issues/new?labels=infra).

If there are merge conflicts, try to rebase the branch and force push. If the conflicts are non-trivial, again, ask the original author for help.

Occasionally, the CL being exported has already been reverted in Chromium. Normally reverts are exported just like any other change, but when the first CL is blocked, we can modify the description of the export PR to include the "Change-Id" of the revert and close the PR, to make the exporter skip both. [Example](https://github.com/web-platform-tests/wpt/pull/10438).
