from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DataSerializer
from .models import Data

import base64
from PIL import Image
import sys, io


from fastai.vision.all import *
from fastai import *
# from fastai.vision.widgets import * 

class DataAPIView(APIView):
    # print(request.GET.get('pred'))
    # serializer_class = DataSerializer
    # queryset = Data.objects.all()
    path = Path()
    print(path)

    def post(self, request, format=None):
        print(request.data['select'])
        imagestr = str(request.data['img'])
        x = imagestr[22:]
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(x, "utf-8"))))
        img.save("1.jpg","JPEG")
        img = PILImage.create("1.jpg")
        # try:
        if request.data['select']=="olma":
            print("olma>>>")
            learn_inf_grape = load_learner(self.path/'grape.pkl', cpu=True)

            pred, pred_idx, probs = learn_inf_apple.predict(img)
        elif request.data['select']=="uzum":
            print("uzum>>>")
            learn_inf_apple = load_learner(self.path/'apple.pkl', cpu=True)

            pred, pred_idx, probs = learn_inf_grape.predict(img)

        # except:
        #     pred="error"
        
        print(pred)
        
        # objData = CustomUser.objects.filter(following=None).order_by('id')
        # paginator = LimitOffsetPagination()
        # result_page = self.paginate_queryset(objData, request)
        # serializer = serializers.UserTreeSerializer(result_page, many=True)
        ret="{}".format(pred)
        return Response(ret)
