from rest_framework.response import Response
from rest_framework.views import APIView


class UploadWithHawk(APIView):

    def post(self, request):
        print 'got FILES keys: {}'.format(request.FILES.keys())
        return Response({'ok': 'maybe?'})
