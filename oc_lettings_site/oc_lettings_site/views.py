from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """Return HomePage to navigate to Profiles or Lettings"""
    return render(request, 'oc_lettings_site/index.html')


def handler404(request, exception):
    """Handle 404 with custom page"""
    return render(request, 'oc_lettings_site/404.html', status=404)


def handler500(request):
    """Handle 500 with custom page"""
    return render(request, 'oc_lettings_site/500.html', status=500)
