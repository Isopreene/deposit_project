from rest_framework.exceptions import ValidationError

from depositapp.models import DepositModel
from depositapp.back.calculate import calculate_deposit
from rest_framework.views import APIView
from rest_framework.response import Response
from depositapp.serializers import DepositSerializer
from rest_framework.request import Request


class DepositView(APIView):

    # def get(self, request: Request) -> Response:
    #     depositdata = DepositModel.objects.all()
    #     return Response(
    #         data={'posts': DepositSerializer(depositdata, many=True).data},
    #         status=200)

    def post(self, request: Request) -> Response:
        serializer = DepositSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({"error": e.detail}, status=400)
        date = serializer.data['date']
        periods = serializer.data['periods']
        amount = serializer.data['amount']
        rate = serializer.data['rate']
        dates_rates = calculate_deposit(date, periods, amount, rate)
        # DepositSerializer(new_deposit).data
        return Response({'info':dates_rates},
                        status=200)