#!/usr/bin/env python3
import json
import sys

import mechanicalsoup

BASE_URL = 'https://ci.chromium.org'
IMPORT_URL = BASE_URL + '/p/infra/builders/luci.infra.cron/wpt-importer?limit=200'
EXPORT_URL = BASE_URL + '/p/infra/builders/luci.infra.cron/wpt-exporter?limit=200'


def scrape_buildbot(url, browser=mechanicalsoup.StatefulBrowser()):
    browser.open(url)
    rows = browser.get_current_page().select('div.main table.info tr')

    builds = []
    recent_failures = 0
    last_success = None
    # Skip the table header.
    for row in rows[1:]:
        columns = row.select('td')

        time = columns[0].get_text().strip()
        duration = columns[1].get_text().strip()
        # revision
        result = columns[3].get_text().strip()
        build = BASE_URL + columns[4].a['href']
        info = columns[5].get_text().strip()
        if result == 'Success':
            last_success = last_success or time
        else:
            if not last_success:
                recent_failures += 1

        builds.append({
            'time': time,
            'duration': duration,
            'result': result,
            'build': build,
            'info': info
        })

    result = {
        'last_success': last_success,
        'recent_failures': recent_failures,
        'builds': builds,
    }

    return result


def scrape_buildbot_to_file(browser, url, result_filename):
    result = scrape_buildbot(url, browser=browser)
    with open(result_filename, 'w') as f:
        json.dump(result, f, indent=2, sort_keys=True)


def main():
    import_result = sys.argv[1]
    export_result = sys.argv[2]
    browser = mechanicalsoup.StatefulBrowser()
    scrape_buildbot_to_file(browser, IMPORT_URL, import_result)
    scrape_buildbot_to_file(browser, EXPORT_URL, export_result)


if __name__ == "__main__":
    main()
