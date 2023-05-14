import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

# Definir una función para crear un filtro Butterworth de paso bajo
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs # frecuencia de Nyquist
    normal_cutoff = cutoff / nyq # frecuencia de corte normalizada
    b, a = butter(order, normal_cutoff, btype='low', analog=False) # coeficientes del filtro
    return b, a

# Definir una función para aplicar el filtro a los datos
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order) # crear el filtro
    y = lfilter(b, a, data) # filtrar los datos
    return y

# Establecer los parámetros del filtro
order = 6 # orden del filtro
fs = 30.0 # frecuencia de muestreo (Hz)
cutoff = 3.667 # frecuencia de corte (Hz)

# Crear el filtro
b, a = butter_lowpass(cutoff, fs, order)

# Graficar la respuesta en frecuencia del filtro
w, h = freqz(b, a, worN=8000) # calcular la respuesta en frecuencia
plt.subplot(2, 1, 1) # crear una subfigura
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b') # graficar la magnitud en función de la frecuencia
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko') # marcar la frecuencia de corte
plt.axvline(cutoff, color='k') # trazar una línea vertical en la frecuencia de corte
plt.xlim(0, 0.5*fs) # establecer el límite del eje x
plt.title("Respuesta en frecuencia del filtro de paso bajo") # poner el título
plt.xlabel('Frecuencia [Hz]') # poner la etiqueta del eje x
plt.grid() # poner la cuadrícula

# Crear los datos para filtrar
T = 5.0 # duración de la señal (segundos)
n = int(T * fs) # número de muestras
t = np.linspace(0, T, n, endpoint=False) # vector de tiempo
# Señal compuesta por tres senoides de diferente frecuencia y amplitud
data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)

# Filtrar los datos y graficar el resultado
y = butter_lowpass_filter(data, cutoff, fs, order) # aplicar el filtro
plt.subplot(2, 1, 2) # crear otra subfigura
plt.plot(t, data, 'b-', label='datos') # graficar los datos originales
plt.plot(t, y, 'g-', linewidth=2, label='datos filtrados') # graficar los datos filtrados
plt.xlabel('Tiempo [seg]') # poner la etiqueta del eje x
plt.grid() # poner la cuadrícula
plt.legend() # poner la leyenda
plt.subplots_adjust(hspace=0.35) # ajustar el espacio entre las subfiguras
plt.show() # mostrar la figura
