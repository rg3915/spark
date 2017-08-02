from spark.courses.models import Course

course_list = [
    {
        'name': 'Data Science',
        'slug': 'data-science',
        'photo': 'https://raw.githubusercontent.com/rg3915/spark/master/spark/img/data-science.jpeg'
    },
    {
        'name': 'Deep Learning',
        'slug': 'deep-learning',
        'photo': 'https://raw.githubusercontent.com/rg3915/spark/master/spark/img/deep-learning.jpg'
    },
    {
        'name': 'Internet of Thing',
        'slug': 'internet-of-things',
        'photo': 'https://raw.githubusercontent.com/rg3915/spark/master/spark/img/iot.jpg'
    },
    {
        'name': 'Machine Learning',
        'slug': 'machine-learning',
        'photo': 'https://raw.githubusercontent.com/rg3915/spark/master/spark/img/machine-learning.jpg'
    },
]

obj = [Course(**name) for name in course_list]
Course.objects.bulk_create(obj)
