These are export PRs which the exporter should have merged by now.

Usually this is caused by failing Travis checks. Read the Travis logs to understand the failure.

A common cause of failure is that [when many tests are affected, Travis jobs will time out](https://github.com/web-platform-tests/wpt/issues/7660). The timeout is at around 50 minutes. When this happens, the PR has to be force merged. Link to [#7660](https://github.com/web-platform-tests/wpt/issues/7660) in a comment and ask @stephenmcgruer or @Hexcles to merge the PR.

If the test is flaky, try to reproduce the flakiness locally and if necessary ask the original CL author for help.

If the failure looks unrelated to the code changes, first rebase and force push the branch. This will both bring in any recent fixes to the problem and trigger a new Travis run. If that doesn't fix the problem and other PRs are also affected, [file a wpt infra bug](https://github.com/web-platform-tests/wpt/issues/new?labels=infra).

If there are merge conflicts, try to rebase the branch and force push. If the conflicts are non-trivial, again, ask the original author for help.

Occasionally, the CL being exported has already been reverted in Chromium. Normally reverts are exported just like any other change, but when the first CL is blocked, we can modify the description of the export PR to include the "Change-Id" of the revert and close the PR, to make the exporter skip both. [Example](https://github.com/web-platform-tests/wpt/pull/10438).
