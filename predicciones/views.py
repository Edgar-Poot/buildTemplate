from django.shortcuts import render
from sklearn.linear_model import LinearRegression
import numpy as np

def regresion_template(request):
    # Datos históricos
    X = [2600, 3000, 3200, 3600, 4000] # variable independiente
    y = [550000, 565000, 610000, 680000, 725000] # variable dependiente (el precio dependerá de)

    area_usuario = None
    prediccion = None

    if request.method == "POST":
        area_usuario = float(request.POST.get("area"))

        # Preparar modelo
        modelo = LinearRegression()
        modelo.fit(np.array(X).reshape(-1, 1), y)

        # Predicción
        prediccion = float(modelo.predict(np.array([[area_usuario]]))[0])

    contexto = {
        "X": X,
        "y": y,
        "area_usuario": area_usuario,
        "prediccion": prediccion,
    }

    return render(request, "predicciones/regresion.html", contexto)
