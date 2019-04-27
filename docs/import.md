The [automatic import process](https://chromium.googlesource.com/chromium/src/+/master/docs/testing/web_platform_tests.md#automatic-import-process) tries to continuously import changes from [wpt](https://github.com/web-platform-tests/wpt) into [web_tests/external/wpt](https://cs.chromium.org/chromium/src/third_party/blink/web_tests/external/wpt/).

When the importer is persistently failing, please [file an importer bug](https://bugs.chromium.org/p/chromium/issues/entry?components=Blink%3EInfra%3EEcosystem&cc=robertma@chromium.org&summary=[WPT%20Import]) and add it to the
[wpt-importer failures](https://docs.google.com/spreadsheets/d/19y9DUuYspuYU_hUZ-fYc10ibTHfMyTx55HLZfuwSNDQ/edit?usp=sharing) sheet.

If the import is failing due to specific tests, unblock import by adding them to [TestExpectations](https://cs.chromium.org/chromium/src/third_party/blink/web_tests/TestExpectations), and if necessary clean that up after a successful import. (For manual tests, instead add them to [NeverFixTests](https://cs.chromium.org/chromium/src/third_party/blink/web_tests/NeverFixTests).) This is much preferable to a [manual import](https://chromium.googlesource.com/chromium/src/+/master/docs/testing/web_platform_tests.md#Manual-import) because the importer will also file bugs for regressions, which will not be filed when importing manually.

If the import is failing due to changes in the
[WPT Tools](https://github.com/web-platform-tests/wpt/tree/master/tools)
directory, it's best to create a PR to fix the error in upstream WPT. These are
typically expected to be lint errors (eg: whitespace, mismatch with executable
bits, etc).


When you're on rotation, the importer will add your as a TBR reviewer for import CLs, but you don’t need to review the CLs if there’s no sign of trouble.
