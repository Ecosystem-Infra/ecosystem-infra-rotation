The [automatic import process](https://chromium.googlesource.com/chromium/src/+/master/docs/testing/web_platform_tests.md#automatic-import-process) tries to continuously import changes from [wpt](https://github.com/web-platform-tests/wpt) into [web_tests/external/wpt](https://cs.chromium.org/chromium/src/third_party/blink/web_tests/external/wpt/).

When the importer is persistently failing, please [file an importer bug](https://bugs.chromium.org/p/chromium/issues/entry?components=Blink%3EInfra%3EEcosystem&cc=weizhong@google.com&summary=[WPT%20Import]).

If the import is failing due to specific tests, unblock import by adding them to [TestExpectations](https://cs.chromium.org/chromium/src/third_party/blink/web_tests/TestExpectations), and if necessary clean that up after a successful import. (For manual tests, instead add them to [NeverFixTests](https://cs.chromium.org/chromium/src/third_party/blink/web_tests/NeverFixTests).) This is much preferable to a [manual import](https://chromium.googlesource.com/chromium/src/+/master/docs/testing/web_platform_tests.md#Manual-import) because the importer will also file bugs for regressions, which will not be filed when importing manually.

If the import is failing due to changes in the
[WPT Tools](https://github.com/web-platform-tests/wpt/tree/master/tools)
directory, it's best to create a PR to fix the error in upstream WPT. These are
typically expected to be lint errors (eg: whitespace, mismatch with executable
bits, etc).

If the Rubber-Stamper bot rejects an import, [see this documentation](https://chromium.googlesource.com/chromium/src/+/master/docs/testing/web_platform_tests.md#rubber_stamper-bot).

The importer will cc the current rotation sheriff on import CLs, but you don’t need to do anything unless something breaks.
