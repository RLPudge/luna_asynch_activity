from django.shortcuts import render
from django.http import HttpResponse


def mission(request):
    mission = 'Our Mission: The University is a private non-stock non-profit non-sectarian educational foundation with a three-fold function - instruction, research, and community service - offering responsive and alternative programs supportive of national development and standards of global excellence.',

    return HttpResponse(mission)


def vision(request):
    vision = 'Our Vision: In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentrations of talent, excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration.'

    return HttpResponse(vision)


def objectives(request):
    objectives = "Our Objectives: Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions.\nEmbark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market.\nExhibit leadership and teamwork, and commitment to their respective local or global organizations.\n",

    return HttpResponse(objectives)
