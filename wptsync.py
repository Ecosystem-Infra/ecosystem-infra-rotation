import mechanicalsoup

BASE_URL = 'https://ci.chromium.org'
IMPORT_URL = BASE_URL + '/p/infra/builders/luci.infra.cron/wpt-importer?limit=50'
EXPORT_URL = BASE_URL + '/p/infra/builders/luci.infra.cron/wpt-exporter?limit=50'


def scrape_buildbot(url):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    rows = browser.get_current_page().select('div.main table.info tr')

    builds = []
    recent_failures = 0
    last_success = None
    # Skip the table header.
    for row in rows[1:]:
        columns = row.select('td')

        time = columns[0].get_text().strip()
        # columns[1] is end time
        duration = columns[2].get_text().strip()
        # columns[3] is commit
        result = columns[4].get_text().strip()
        build = BASE_URL + columns[5].a['href']
        info = columns[6].get_text().strip()
        if result == 'SUCCESS':
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


def import_status():
    return scrape_buildbot(IMPORT_URL)


def export_status():
    return scrape_buildbot(EXPORT_URL)
