# -*- coding: utf-8 -*-
"""Videos 2025-I.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o7KqahKX4s0DQlJ0dKnwXJaPTziZGpVw
"""

import streamlit as st
import pandas as pd

# Datos directamente en el código
datos = [
    {"FECHA": "04/03/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1ycqt5ItXi92Ie7f6SdNW_ySvW54l-o3k/view?usp=sharing"},
    {"FECHA": "05/03/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/1xBvz3IEsfdzI1lVT-QGvUdBnw4myk6Dh/view?usp=sharing"},
    {"FECHA": "06/03/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1jdgtCbthjby2gSNg-dtm0SRBVS_AOeGZ/view?usp=sharing"},
    {"FECHA": "07/03/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1xPrNTa0vZWdqRJztG0X11WuVUmoUWLFS/view?usp=sharing"},
    {"FECHA": "08/03/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/1YJqV5aT77JF53dF_1N_8E6FW4sCUjPE7/view?usp=sharing"},
    {"FECHA": "13/03/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1T4QP9V6uzhgiSGkauzCDgMCHbRqsNp9L/view?usp=sharing"},
    {"FECHA": "14/03/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1PpNFYmt1IcLxF_eqj0xcI8b5AKDP_J2H/view?usp=sharing"},
    {"FECHA": "18/03/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1A5ZbcVODnC_2yNHlFeg0iH-uta4MrBEq/view?usp=sharing"},
    {"FECHA": "21/03/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1lmvb0KFkd9BlqC9CJ1hvsNJciDwx-Fm_/view?usp=sharing"},
    {"FECHA": "27/03/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1xS7s9cuWvXpySwYrGCd-uc5UXB3McCIG/view?usp=sharing"},
    {"FECHA": "03/04/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1pHp8T7vAJFPSfnW5D0M8sBdFsn1JiwiM/view?usp=sharing"},
    {"FECHA": "04/04/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1h70vzWmZysixfHI9OuxDOT2MI0N2ZeYV/view?usp=sharing"},
    {"FECHA": "04/04/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1h70vzWmZysixfHI9OuxDOT2MI0N2ZeYV/view?usp=sharing"},
    {"FECHA": "05/04/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/1UefyTapRDf8FnmVYLMDcuT8-BQGKBhge/view?usp=sharing"},
    {"FECHA": "08/04/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1xYrZZSEIdyLuWzZdiyAjw-kxFseAHiRs/view?usp=sharing"},
    {"FECHA": "09/04/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/1U6cWnDgAAJSdRu-ArcU3-fSlB48axPm8/view?usp=sharing"},
    {"FECHA": "10/04/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1YHxH9OQ-av91Sb_EAqTsw0osNwcqI_T5/view?usp=sharing"},
    {"FECHA": "11/04/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1i3xoix5KkYgRS3-1QXmVUdCieqeKRdJn/view?usp=sharing"},
    {"FECHA": "12/04/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/1G6jmlksReW5KUe2Rrpi5EAmfPEUM9U_i/view?usp=sharing"},
    {"FECHA": "22/04/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1rSc3e5UOTiLj4zE4UoeimUPKJZRyVIzS/view?usp=sharing"},
    {"FECHA": "23/04/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/1Il4e63_0xX9eOPPhCoNN3uqaXbUXeeMg/view?usp=sharing"},
    {"FECHA": "24/04/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1FUhdYh9xGo5BwUqj0ZjQM5JDbv8q9_p0/view?usp=sharing"},
    {"FECHA": "25/04/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/113gbdovgNNVr2PCBNIoBbGN61CFJZ1hH/view?usp=sharing"},
    {"FECHA": "26/04/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/12kCwe1xAyORXXo4Wf269TGgxgiGN11i1/view?usp=sharing"},
    {"FECHA": "29/04/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1OxSXHfkE-v2u5Vr1BZjGOr0dMJNZmWbW/view?usp=sharing"},
    {"FECHA": "30/04/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/11iAExV9LHt0OMrxv3yO-KII86gsnF6hr/view?usp=sharing"},
    {"FECHA": "02/05/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/19xbHIwGrBvDrFDhITeFcnUQB_gKSJNeu/view?usp=sharing"},
    {"FECHA": "03/05/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/1H1L2VPuBf9amvuf08yKVjy6-o5drG_0d/view?usp=sharing"},
    {"FECHA": "06/05/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1xF4iQLTt84VoEWh7Mi0E9rkrhOLg7Pw9/view?usp=sharing"},
    {"FECHA": "07/05/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/1p2aD-aBCJ38LbGNcTLvEfG8Z51N-B7at/view?usp=sharing"},
    {"FECHA": "08/05/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1-mWum62fjAA0bV9in5JuA3O_URWSK8b1/view?usp=sharing"},
    {"FECHA": "09/05/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1NLLy7BXy6OhAm4EaT8hn_awxPSyWAQBz/view?usp=sharing"},
    {"FECHA": "10/05/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/1tzpgHPw_mJJny7LnH2t5j9SAj2n-ki4K/view?usp=sharing"},
    {"FECHA": "13/05/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1bbb70DuEUU-2sg5JFHQYuxwUHhMhO9tW/view?usp=sharing"},
    {"FECHA": "14/05/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/1kx3-G7oZr3XK46D_rELJRjiWpTvO42wU/view?usp=sharing"},
    {"FECHA": "16/05/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1aq3zpOoEaeHOvOLcIyPuv3_QWDEejgNb/view?usp=sharing"},
    {"FECHA": "17/05/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/1CRV1oVXFN-NN7n9pmVBp30rDGx24jyx-/view?usp=sharing"},
    {"FECHA": "20/05/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1A9Dt1r-X3R7Nokm1GJHTQrGNnutJEAzG/view?usp=sharing"},
    {"FECHA": "21/05/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/1Z6-HpQYvGfEm7MMM3WXqPvpdHp6m7v8D/view?usp=sharing"},
    {"FECHA": "22/05/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1iybvVILbvhuRpZKhTBJdK8D3v9ytfBFI/view?usp=sharing"},
    {"FECHA": "23/05/2025", "GRUPO": 101, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1I73RpRQoYADEdvzPnuEUUfLqPMxKvfxk/view?usp=sharing"},
    {"FECHA": "24/05/2025", "GRUPO": 204, "UCA": "ESTADÍSTICA DESCRIPTIVA", "LIGA": "https://drive.google.com/file/d/1G5xxjz8bcrwBpLf8TPRbOZPdvCt519TJ/view?usp=sharing"},
    {"FECHA": "27/05/2025", "GRUPO": 102, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1IlQdBEVohI8XZmwlOBwen1fQzl9WFf--/view?usp=sharing"},
    {"FECHA": "28/05/2025", "GRUPO": 207, "UCA": "SISTEMAS CONTABLES DE INFORMACIÓN FINANCIERA", "LIGA": "https://drive.google.com/file/d/1mI_ZY7CA7jn7tY4v7mPP0cPBpN1Rk98I/view?usp=sharing"},
    {"FECHA": "29/05/2025", "GRUPO": 103, "UCA": "MÉTODOS CUANTITATIVOS", "LIGA": "https://drive.google.com/file/d/1yGIVy_Lh0IFT77FkroY0QZ72R5yzgkRN/view?usp=sharing"},

]

# Convertir a DataFrame para facilitar el filtrado
df = pd.DataFrame(datos)
st.image("UNRC.png", caption="Universidad Nacional Rosario Castellanos", width=550)
st.title("Repositorio de Videos de Clase")
st.write("Selecciona tu grupo, fecha y materia para ver el video.")

# Menús de selección
grupo = st.selectbox("Selecciona tu grupo", sorted(df["GRUPO"].unique()))
fechas_filtradas = df[df["GRUPO"] == grupo]["FECHA"].unique()
fecha = st.selectbox("Selecciona la fecha", fechas_filtradas)

ucas_filtradas = df[(df["GRUPO"] == grupo) & (df["FECHA"] == fecha)]["UCA"].unique()
uca = st.selectbox("Selecciona la materia", ucas_filtradas)

# Filtrar resultados
video = df[(df["GRUPO"] == grupo) & (df["FECHA"] == fecha) & (df["UCA"] == uca)]

if not video.empty:
    liga = video.iloc[0]["LIGA"]
    st.success("¡Video encontrado!")

    # Convertir el enlace para previsualizar en iframe
    if "drive.google.com/file/d/" in liga:
        video_id = liga.split("/d/")[1].split("/")[0]
        embed_url = f"https://drive.google.com/file/d/{video_id}/preview"
        st.components.v1.iframe(embed_url, height=480)
    else:
        st.write(f"[Ver video en una nueva pestaña]({liga})")
else:
    st.warning("No se encontró un video con esos criterios.")