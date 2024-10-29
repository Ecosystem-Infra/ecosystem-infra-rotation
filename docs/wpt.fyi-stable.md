Runs for stable Chrome, Firefox and Safari should happen at least daily.

If this check fails, file an issue on [wpt.fyi](https://github.com/web-platform-tests/wpt.fyi) if all runs are affected, or [wpt](https://github.com/web-platform-tests/wpt) with the [infra label](https://github.com/web-platform-tests/wpt/labels/infra) if only some runs are missing. To check for issues on recent runs go to [wpt.fyi/status](https://wpt.fyi/status), select the `Invalid runs` tab, and then click on `Show error`. If the issue is with the WPT CI, then it's best to file an issue in the wpt repo, even in the case of all engines being affected.

Contact points for the underlying runner infrastructure:
* Chrome - [@past](https://github.com/past) (Taskcluster)
* Firefox - [@jgraham](http://github.com/jgraham) (Taskcluster)
* Safari - [@gsnedders](https://github.com/gsnedders) (Azure Pipelines)
