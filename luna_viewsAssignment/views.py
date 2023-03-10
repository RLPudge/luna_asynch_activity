from django.shortcuts import render
from django.http import HttpResponse


def mission(request):
    content = {
        'content': 'The University is a private non-stock non-profit non-sectarian educational foundation with a three-fold function - instruction, research, and community service - offering responsive and alternative programs supportive of national development and standards of global excellence.',
    }
    return render(request, 'mission.html', content)


def vision(request):
    content = {
        'content': 'In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentrations of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration.',
    }
    return render(request, 'vision.html', content)


def objectives(request):
    contentList = [
        "Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions.",
        "Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market.",
        "Exhibit leadership and teamwork, and commitment to their respective local or global organizations.",
    ]
    return render(request, 'objectives.html', {'contentList': contentList})
