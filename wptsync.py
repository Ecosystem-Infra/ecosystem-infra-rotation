import json
from datetime import datetime
from typing import TypedDict, List

import requests

BUILDBUCKET_HOST = 'cr-buildbucket.appspot.com'
BUILDBUCKET_API = 'buildbucket.v2.Builds'
PRPC_PREFIX = ")]}'"  # Anti-XSS escape before every response
PROJECT, BUCKET = 'infra', 'cron'
BUILD_FIELDS = [
    'createTime',
    'startTime',
    'endTime',
    'status',
    'id',
    'summaryMarkdown',
]


class Build(TypedDict):
    time: str
    duration: str
    result: str
    build: str
    info: str


class Results(TypedDict):
    last_success: str
    recent_failures: int
    builds: List[Build]


def search_builds(builder_name: str, count: int = 50) -> Results:
    """Fetch the latest completed builds for an `infra/cron` builder.

    Arguments:
        builder_name: Builder to fetch builds for.
        count: Number of latest builds to fetch.

    See Also:
        https://source.chromium.org/chromium/_/chromium/infra/luci/luci-go/+/1fbb74377bfb72e37328c737c66eabb1521d8c1f:buildbucket/proto/builds_service.proto;l=175-216
    """
    rpc_url = f'https://{BUILDBUCKET_HOST}/prpc/{BUILDBUCKET_API}/SearchBuilds'
    request_payload = {
        'predicate': {
            'builder': {
                'project': PROJECT,
                'bucket': BUCKET,
                'builder': builder_name,
            },
            # Only fetch completed jobs.
            'status': 'ENDED_MASK',
        },
        'fields': ','.join(f'builds.*.{field}' for field in BUILD_FIELDS),
        'pageSize': count,
    }
    response = requests.post(rpc_url, json=request_payload, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip',
    })
    response.raise_for_status()
    response_payload = json.loads(
        response.text.removeprefix(PRPC_PREFIX).strip())

    last_success, recent_failures, builds = None, 0, []
    # Buildbucket already returns builds newest to oldest.
    for raw_build in response_payload['builds']:
        time = raw_build['createTime']
        start = datetime.fromisoformat(raw_build['startTime'])
        end = datetime.fromisoformat(raw_build['endTime'])
        duration = _format_duration((end - start).total_seconds())
        result = raw_build['status']
        build = (f'https://ci.chromium.org/p/{PROJECT}/builders'
                 f'/{BUCKET}/{builder_name}/b{raw_build["id"]}')
        info = raw_build.get('summaryMarkdown', '')

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
            'info': info,
        })

    result = {
        'last_success': last_success,
        'recent_failures': recent_failures,
        'builds': builds,
    }

    return result


def _format_duration(seconds: float) -> str:
    minutes, seconds = divmod(max(0, seconds), 60)
    hours, minutes = divmod(minutes, 60)
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    if hours:
        return f'{hours} hrs {minutes} mins'
    return f'{minutes} mins {seconds} secs'


def import_status():
    return search_builds('wpt-importer')


def export_status():
    return search_builds('wpt-exporter')
