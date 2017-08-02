from spark.courses.models import Course
from spark.videos.models import Video

VIDEOS = [
    {
        'course': 'Data Science',
        'url': 'https://www.youtube.com/embed/0XyV91VYrDs',
        'position': 1,
    },
    {
        'course': 'Data Science',
        'url': 'https://www.youtube.com/embed/5GJjlMXjUIE',
        'position': 2,
    },
    {
        'course': 'Data Science',
        'url': 'https://www.youtube.com/embed/ccCblUZFM0w',
        'position': 3,
    },
    {
        'course': 'Deep Learning',
        'url': 'https://www.youtube.com/embed/b99UVkWzYTQ',
        'position': 1,
    },
    {
        'course': 'Deep Learning',
        'url': 'https://www.youtube.com/embed/b4MxnoisnOM',
        'position': 2,
    },
    {
        'course': 'Deep Learning',
        'url': 'https://www.youtube.com/embed/l42lr8AlrHk',
        'position': 3,
    },
    {
        'course': 'Internet of Thing',
        'url': 'https://www.youtube.com/embed/-6_qWZzkAh4',
        'position': 1,
    },
    {
        'course': 'Internet of Thing',
        'url': 'https://www.youtube.com/embed/QSIPNhOiMoE',
        'position': 2,
    },
    {
        'course': 'Internet of Thing',
        'url': 'https://www.youtube.com/embed/ilyHAWUuGmw',
        'position': 3,
    },
    {
        'course': 'Machine Learning',
        'url': 'https://www.youtube.com/embed/cKxRvEZd3Mw',
        'position': 1,
    },
    {
        'course': 'Machine Learning',
        'url': 'https://www.youtube.com/embed/OGxgnH8y2NM',
        'position': 2,
    },
    {
        'course': 'Machine Learning',
        'url': 'https://www.youtube.com/embed/nJKxWbQ1jaw',
        'position': 3,
    },
]


def video_data(idx_course):
    try:
        course = Course.objects.get(name=VIDEOS[idx_course]['course'])
    except Course.DoesNotExist:
        course = Course.objects.create(**VIDEOS[idx_course]['course'])
    return {'course': course,
            'url': VIDEOS[idx_course]['url'],
            'position': VIDEOS[idx_course]['position'],
            }


aux_list = [video_data(i) for i in range(len(VIDEOS))]
obj = [Video(**video) for video in aux_list]
Video.objects.bulk_create(obj)
