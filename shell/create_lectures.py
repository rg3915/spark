from spark.courses.models import Course
from spark.lectures.models import Lecture

LECTURES = [
    {
        'title': 'Introdução',
        'course': 'data-science',
        'slug': 'data-science-introducao',
        'description': 'Mussum Ipsum, cacilds vidis litro abertis. Sapien in monti palavris qui num significa nadis i pareci latim. Não sou faixa preta cumpadi, sou preto inteiris, inteiris.',
        'url': 'https://www.youtube.com/embed/0XyV91VYrDs',
        'position': 1,
    },
    {
        'title': 'Leitura 1',
        'course': 'data-science',
        'slug': 'data-science-leitura1',
        'description': 'Manduma pindureta quium dia nois paga. Praesent malesuada urna nisi, quis volutpat erat hendrerit non. Nam vulputate dapibus.',
        'url': 'https://www.youtube.com/embed/5GJjlMXjUIE',
        'position': 2,
    },
    {
        'title': 'Leitura 2',
        'course': 'data-science',
        'slug': 'data-science-leitura2',
        'description': 'Si u mundo tá muito paradis? Toma um mé que o mundo vai girarzis! Copo furadis é disculpa de bebadis, arcu quam euismod magna.',
        'url': 'https://www.youtube.com/embed/ccCblUZFM0w',
        'position': 3,
    },
    {
        'title': 'Leitura 3',
        'course': 'data-science',
        'slug': 'data-science-leitura3',
        'description': 'Casamentiss faiz malandris se pirulitá. Todo mundo vê os porris que eu tomo, mas ninguém vê os tombis que eu levo!',
        'url': '',
        'position': 4,
    },
    {
        'title': 'Leitura 4',
        'course': 'data-science',
        'slug': 'data-science-leitura4',
        'description': 'Diuretics paradis num copo é motivis de denguis. Paisis, filhis, espiritis santis. Atirei o pau no gatis, per gatis num morreus.',
        'url': '',
        'position': 5,
    },
    {
        'title': 'Introdução',
        'course': 'deep-learning',
        'slug': 'deep-learning-introducao',
        'description': 'Vehicula non. Ut sed ex eros. Vivamus sit amet nibh non tellus tristique interdum.',
        'url': 'https://www.youtube.com/embed/b99UVkWzYTQ',
        'position': 1,
    },
    {
        'title': 'Leitura 1',
        'course': 'deep-learning',
        'slug': 'deep-learning-leitura1',
        'description': 'Cevadis im ampola pa arma uma pindureta. Viva Forevis aptent taciti sociosqu ad litora torquent.',
        'url': 'https://www.youtube.com/embed/b4MxnoisnOM',
        'position': 2,
    },
    {
        'title': 'Leitura 2',
        'course': 'deep-learning',
        'slug': 'deep-learning-leitura2',
        'description': 'Leite de capivaris, leite de mula manquis sem cabeça. Posuere libero varius. Nullam a nisl ut ante blandit hendrerit. Aenean sit amet nisi.',
        'url': 'https://www.youtube.com/embed/l42lr8AlrHk',
        'position': 3,
    },
    {
        'title': 'Leitura 3',
        'course': 'deep-learning',
        'slug': 'deep-learning-leitura3',
        'description': 'Pra lá , depois divoltis porris, paradis. Mé faiz elementum girarzis, nisi eros vermeio. Quem manda na minha terra sou euzis! Interagi no mé, cursus quis, vehicula ac nisi.',
        'url': '',
        'position': 4,
    },
    {
        'title': 'Leitura 4',
        'course': 'deep-learning',
        'slug': 'deep-learning-leitura4',
        'description': 'A ordem dos tratores não altera o pão duris. Per aumento de cachacis, eu reclamis.',
        'url': '',
        'position': 5,
    },
    {
        'title': 'Introdução',
        'course': 'internet-of-things',
        'slug': 'internet-of-things-introducao',
        'description': 'Admodum accumsan disputationi eu sit. Vide electram sadipscing et per. Em pé sem cair, deitado sem dormir, sentado sem cochilar e fazendo pose.',
        'url': 'https://www.youtube.com/embed/-6_qWZzkAh4',
        'position': 1,
    },
    {
        'title': 'Leitura 1',
        'course': 'internet-of-things',
        'slug': 'internet-of-things-leitura1',
        'description': 'Mussum Ipsum, cacilds vidis litro abertis. Sapien in monti palavris qui num significa nadis i pareci latim. Não sou faixa preta cumpadi, sou preto inteiris, inteiris.',
        'url': 'https://www.youtube.com/embed/QSIPNhOiMoE',
        'position': 2,
    },
    {
        'title': 'Leitura 2',
        'course': 'internet-of-things',
        'slug': 'internet-of-things-leitura2',
        'description': 'Manduma pindureta quium dia nois paga. Praesent malesuada urna nisi, quis volutpat erat hendrerit non. Nam vulputate dapibus.',
        'url': 'https://www.youtube.com/embed/ilyHAWUuGmw',
        'position': 3,
    },
    {
        'title': 'Leitura 3',
        'course': 'internet-of-things',
        'slug': 'internet-of-things-leitura3',
        'description': 'Si u mundo tá muito paradis? Toma um mé que o mundo vai girarzis! Copo furadis é disculpa de bebadis, arcu quam euismod magna.',
        'url': '',
        'position': 4,
    },
    {
        'title': 'Leitura 4',
        'course': 'internet-of-things',
        'slug': 'internet-of-things-leitura4',
        'description': 'Casamentiss faiz malandris se pirulitá. Todo mundo vê os porris que eu tomo, mas ninguém vê os tombis que eu levo!',
        'url': '',
        'position': 5,
    },
    {
        'title': 'Introdução',
        'course': 'machine-learning',
        'slug': 'machine-learning-introducao',
        'description': 'Diuretics paradis num copo é motivis de denguis. Paisis, filhis, espiritis santis. Atirei o pau no gatis, per gatis num morreus.',
        'url': 'https://www.youtube.com/embed/cKxRvEZd3Mw',
        'position': 1,
    },
    {
        'title': 'Leitura 1',
        'course': 'machine-learning',
        'slug': 'machine-learning-leitura1',
        'description': 'Vehicula non. Ut sed ex eros. Vivamus sit amet nibh non tellus tristique interdum.',
        'url': 'https://www.youtube.com/embed/OGxgnH8y2NM',
        'position': 2,
    },
    {
        'title': 'Leitura 2',
        'course': 'machine-learning',
        'slug': 'machine-learning-leitura2',
        'description': 'Cevadis im ampola pa arma uma pindureta. Viva Forevis aptent taciti sociosqu ad litora torquent.',
        'url': 'https://www.youtube.com/embed/nJKxWbQ1jaw',
        'position': 3,
    },
    {
        'title': 'Leitura 3',
        'course': 'machine-learning',
        'slug': 'machine-learning-leitura3',
        'description': 'Leite de capivaris, leite de mula manquis sem cabeça. Posuere libero varius. Nullam a nisl ut ante blandit hendrerit. Aenean sit amet nisi.',
        'url': '',
        'position': 4,
    },
    {
        'title': 'Leitura 4',
        'course': 'machine-learning',
        'slug': 'machine-learning-leitura4',
        'description': 'Pra lá , depois divoltis porris, paradis. Mé faiz elementum girarzis, nisi eros vermeio. Quem manda na minha terra sou euzis! Interagi no mé, cursus quis, vehicula ac nisi.',
        'url': '',
        'position': 5,
    },
]


def lecture_data(idx_course):
    try:
        course = Course.objects.get(slug=LECTURES[idx_course]['course'])
    except Course.DoesNotExist:
        pass
    return {'course': course,
            'title': LECTURES[idx_course]['title'],
            'slug': LECTURES[idx_course]['slug'],
            'description': LECTURES[idx_course]['description'],
            'url': LECTURES[idx_course]['url'],
            'position': LECTURES[idx_course]['position'],
            }


aux_list = [lecture_data(i) for i in range(len(LECTURES))]
obj = [Lecture(**lecture) for lecture in aux_list]
Lecture.objects.bulk_create(obj)
