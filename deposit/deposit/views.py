from deposit.models import DepositModel
from deposit.back.calculate import calculate_deposit
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import DepositSerializer
from rest_framework.request import Request

class DepositView(APIView):
    def get(self, request: Request) -> Response:
        depositdata = DepositModel.objects.all()
        return Response(data={'posts':DepositSerializer(depositdata, many=True).data}, status=200)
    
    def post(self, request:Request) -> Response:
        serializer = DepositSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        date=request.data.get('title')
        periods=request.data.get('periods', 0)
        amount=request.data.get('amount', 0)
        rate=request.data.get('rate', 0)

        new_deposit = DepositModel.objects.create(date,
                                                  periods,
                                                  amount,
                                                  rate)

        if not True: #валидация
            return Response("Exception", status=400)
        
        dates_rates = calculate_deposit(date, periods, amount, rate)
        # DepositSerializer(new_deposit).data
        return Response({'dates': dates_rates}, status=200)
