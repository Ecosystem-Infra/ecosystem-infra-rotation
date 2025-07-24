The [automatic import process](https://chromium.googlesource.com/chromium/src/+/master/docs/testing/web_platform_tests.md#automatic-import-process) tries to continuously import changes from [wpt](https://github.com/web-platform-tests/wpt) into [web_tests/external/wpt](https://cs.chromium.org/chromium/src/third_party/blink/web_tests/external/wpt/).
When the [rubber stamper] cannot approve a CL, the importer will cc the
current rotation gardener to do so.

[rubber stamper]: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/testing/web_platform_tests.md#rubber_stamper-bot

When the importer fails, consult the logs from the "Import changes from WPT to
Chromium" step.
The most common failure mode is malformed or incomplete expectations for new
test failures.
In that case, you will need to restore one of the [abandoned CLs] and fix the
expectations yourself:

```sh
git new-branch import-wpt
git cl patch https://crrev.com/c/$CL_NUMBER/1
# <update expectations, as described below>
git add third_party/blink/web_tests
git commit -m "Fix expectations"
git cl upload --dry-run
```

Guidelines for updating [the expectations]:
* If a test fails with a consistent text diff,
  1. If the diff contains ["All subtests passed"][all-pass] on all builders,
     delete all `*-expected.txt` associated with the test.
     The test runner expects no subtest failures when `*-expected.txt` is
     absent.
  1. Otherwise, add or update an `*-expected.txt` file in the same directory
     as the test file.
     The easiest way to do this in your local checkout is by [running the
     test(s)][run tests] with `run_wpt_tests.py --reset-results $TEST_NAMES`.
* Otherwise, add an entry to [`TestExpectations` under the `unblock
  wpt-importer` comment][TestExpectations]. The importer will file bugs later
  automatically, so there's no need to file and add them yourself.
* Tests are almost never platform-specific, so any platform-specific
  expectations created are likely by happenstance and can be cleaned up into
  one of the more robust forms above.
* You can remove expectations for unrelated tests that shouldn't be affected,
  but are flaky/failing on trunk.

Once uploaded, send the CL to one or more [committers] for review.

[all-pass]: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/testing/writing_web_tests.md#Text-Test-Baselines
[run tests]: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/testing/run_web_platform_tests.md
[committers]: https://www.chromium.org/getting-involved/become-a-committer/
[TestExpectations]: https://chromium.googlesource.com/chromium/src/+/3e74d537/third_party/blink/web_tests/TestExpectations#2712
[the expectations]: https://chromium.googlesource.com/chromium/src/+/HEAD/docs/testing/web_test_expectations.md
[abandoned CLs]: https://chromium-review.googlesource.com/q/status:abandoned+owner:wpt-autoroller@chops-service-accounts.iam.gserviceaccount.com

Sometimes, tests will land upstream that depend on a new API in
[WPT Tools](https://github.com/web-platform-tests/wpt/tree/master/tools).
Because [tooling changes] are rolled into Chromium separately, such tests may
fail with "not defined" or similar once imported.
For this case, rather than adding failure expectations, run [the
`roll_wpt.py` script][roll script] in a local checkout to make the tooling
changes available on trunk.
If the tooling change is not backward compatible, you may need to roll the
tooling in the same CL as the tests (e.g.,
https://crbug.com/381282548#comment2).

[tooling changes]: https://chromium-review.googlesource.com/q/subject:%22Roll+wpt+tooling%22
[roll script]: https://chromium.googlesource.com/chromium/src/+/HEAD/third_party/wpt_tools/roll_wpt.py

For other persistent failures, please [file an importer bug](https://bugs.chromium.org/p/chromium/issues/entry?components=Blink%3EInfra&summary=[WPT%20Import]).
