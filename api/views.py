from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from .serializers import CancerSerializer
from rest_framework import status
import os
from django.conf import settings
# Construct the absolute file path within the Docker container
file_path = os.path.join(settings.BASE_DIR, 'cancer.csv')
# Load the dataset
data = pd.read_csv(file_path)
x = data.iloc[:, :-1]
y = data.iloc[:, -1]
model = DecisionTreeClassifier()
model.fit(x, y)
@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        serializer = CancerSerializer(data=request.data)
        if serializer.is_valid():
            input_data = tuple(serializer.validated_data.values())
            input_numpy = np.asarray(input_data).reshape(1, -1)
            out = model.predict(input_numpy)
            # Handle the case where 'out' is not assigned in all execution paths
            prediction = "Affected by Cancer" if out == 1 else "You are Safe"
            return Response({'prediction': prediction}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
