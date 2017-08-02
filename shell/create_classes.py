from spark.courses.models import Course, Classe

CLASSES = [
    {
        'team': 'Data Science',
        'date_initial': '2017-06-01',
        'date_final': '2017-07-01',
        'short_description': 'Data Science is awesome',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quisquam molestiae rerum earum expedita natus repellendus enim in quis atque eaque provident dicta corporis cupiditate totam dolorem, unde laborum cum numquam.',
        'slug': 'data-science',
    },
    {
        'team': 'Deep Learning',
        'date_initial': '2017-06-01',
        'date_final': '2017-07-01',
        'short_description': 'Deep Learning is awesome',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quisquam molestiae rerum earum expedita natus repellendus enim in quis atque eaque provident dicta corporis cupiditate totam dolorem, unde laborum cum numquam.',
        'slug': 'deep-learning',
    },
    {
        'team': 'Internet of Thing',
        'date_initial': '2017-06-07',
        'date_final': '2017-07-07',
        'short_description': 'Internet of Thing is awesome',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quisquam molestiae rerum earum expedita natus repellendus enim in quis atque eaque provident dicta corporis cupiditate totam dolorem, unde laborum cum numquam.',
        'slug': 'internet-of-thing',
    },
    {
        'team': 'Machine Learning',
        'date_initial': '2017-06-07',
        'date_final': '2017-07-07',
        'short_description': 'Machine Learning is awesome',
        'description': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quisquam molestiae rerum earum expedita natus repellendus enim in quis atque eaque provident dicta corporis cupiditate totam dolorem, unde laborum cum numquam.',
        'slug': 'machine-learning',
    },
]


def classe_data(idx_course):
    try:
        course = Course.objects.get(
            name__icontains=CLASSES[idx_course]['team'])
    except Course.DoesNotExist:
        course = Course.objects.create(**CLASSES[idx_course]['team'])
    return {'course': course,
            'team': CLASSES[idx_course]['team'],
            'date_initial': CLASSES[idx_course]['date_initial'],
            'date_final': CLASSES[idx_course]['date_final'],
            'short_description': CLASSES[idx_course]['short_description'],
            'description': CLASSES[idx_course]['description'],
            'slug': CLASSES[idx_course]['slug'],
            }


aux_list = []

# Appending aux_list
for i in range(len(CLASSES)):
    aux_list.append(classe_data(i))

obj = [Classe(**classe) for classe in aux_list]
Classe.objects.bulk_create(obj)
