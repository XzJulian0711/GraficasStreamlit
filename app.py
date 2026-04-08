import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Dashboard de graficas")
#Marketing y ventas----------------------------------------------------------------------
# Menú lateral
st.sidebar.title("Mejoras realizadas")

st.sidebar.markdown("### 1. Marketing y Ventas (scatter)")
st.sidebar.markdown("""
- **Original:** título genérico, bordes gruesos de colores llamativos
- **Mejora:** barras comparativas ordenadas, etiquetas de valor, diseño limpio
""")
st.header("Marketing y Ventas")
df1 = pd.read_csv("datos/marketing_ventas.csv")
df1 = df1.sort_values(by='Inversion_Marketing_USD').reset_index(drop=True)
x = np.arange(len(df1))
width = 0.4

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(x - width/2, df1['Inversion_Marketing_USD'], width, label='Inversión Marketing',
           color='red', edgecolor='yellow', linewidth=2)
    ax.bar(x + width/2, df1['Ventas_Generadas_USD'], width, label='Ventas Generadas',
           color='blue', edgecolor='yellow', linewidth=2)
    ax.set_facecolor('white')
    fig.patch.set_edgecolor('green')
    fig.patch.set_linewidth(4)
    ax.set_title("Datos de la empresa 2024")
    ax.set_xlabel("Índice")
    ax.set_ylabel("Ventas ($)")
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Mejorada")
    fig, ax = plt.subplots(figsize=(6, 4))
    bars1 = ax.bar(x - width/2, df1['Inversion_Marketing_USD'], width,
                   label='Inversión Marketing', color='tomato')
    bars2 = ax.bar(x + width/2, df1['Ventas_Generadas_USD'], width,
                   label='Ventas Generadas', color='royalblue')
    for bar in bars1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 500, f'{int(h)}', ha='center', fontsize=7)
    for bar in bars2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 500, f'{int(h)}', ha='center', fontsize=7)
    ax.set_title("Relación entre Inversión en Marketing y Ventas", fontsize=11)
    ax.set_xlabel("Registros de datos")
    ax.set_ylabel("Valor en dólares ($)")
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)



# Presupuesto departamentos-----------------------------------------------------------
# Menu lateral
st.sidebar.markdown("### 2. Presupuesto Departamentos")
st.sidebar.markdown("""
- **Original:** gráfico circular con un solo color rosado, difícil distinguir secciones
- **Mejora:** paleta cualitativa Set3, cada departamento con color distinto
""")
st.header("Presupuesto por Departamento")
df2 = pd.read_csv("datos/presupuesto_departamentos.csv")
df2 = df2.sort_values(by='Presupuesto_Porcentaje', ascending=False)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original")
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(df2['Presupuesto_Porcentaje'], labels=df2['Departamento'],
           autopct='%1.1f%%', colors=['#F08080']*len(df2),
           startangle=140, wedgeprops=dict(edgecolor='gray', linewidth=1.5))
    ax.set_title('Gráfico Circular', fontweight='bold', fontsize=13)
    st.pyplot(fig)

with col2:
    st.subheader("Mejorada")
    colores = plt.cm.Set3.colors[:len(df2)]
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts, autotexts = ax.pie(
        df2['Presupuesto_Porcentaje'], labels=df2['Departamento'],
        autopct='%1.1f%%', colors=colores, startangle=140,
        pctdistance=0.75, wedgeprops=dict(edgecolor='white', linewidth=2))
    for text in texts:
        text.set_fontsize(11)
    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_fontweight('bold')
    ax.set_title('Distribución de Presupuesto por Departamento',
                 fontsize=12, fontweight='bold', pad=20)
    plt.tight_layout()
    st.pyplot(fig)
    
# Satisfaccion de clientes
# Menu lateral
st.sidebar.markdown("### 3. Satisfacción del Cliente")
st.sidebar.markdown("""
- **Original:** eje X hasta 3 sin justificación, un solo color verde
- **Mejora:** rojo para insatisfacción, verde para satisfacción, eje limitado a -2/+2
""")
st.header("Satisfacción del Cliente")
df3 = pd.read_csv("datos/satisfaccion_cliente.csv")
categorias = df3["Categoria"].tolist()
valores = df3["Puntuacion"].tolist()
y = np.arange(len(categorias))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(y, valores, color='green', edgecolor='black', linewidth=2)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(categorias)
    ax.set_xlim(-2, 3)
    ax.set_xlabel("Score")
    ax.set_title("Encuesta", color='purple', fontweight='bold')
    ax.yaxis.grid(True, linestyle='--', color='red', alpha=0.5)
    st.pyplot(fig)

with col2:
    st.subheader("Mejorada")
    positivos = [v if v > 0 else 0 for v in valores]
    negativos = [v if v < 0 else 0 for v in valores]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(y, negativos, color="#e74c3c", label="Insatisfacción")
    ax.barh(y, positivos, color="#2ecc71", label="Satisfacción")
    ax.axvline(0, color='black', linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(categorias)
    ax.set_xlabel("Nivel de satisfacción (-2 Muy insatisfecho | +2 Muy satisfecho)")
    ax.set_title("Encuesta de Satisfacción del Cliente")
    ax.set_xlim(-2, 2)
    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.grid(axis='x', linestyle='--', alpha=0.4)
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)


# Temperatura diaria
# Menu lateral
st.sidebar.markdown("### 4. Temperatura Diaria")
st.sidebar.markdown("""
- **Original:** fondo amarillo, colores arcoíris sin significado claro
- **Mejora:** gradiente coolwarm (azul=frío, rojo=calor), bordes limpios y valores encima
""")
st.header("Temperatura Diaria")
df4 = pd.read_csv("datos/temperatura_diaria.csv")
df4.columns = df4.columns.str.strip().str.lower()
dias = df4.iloc[:, 0]
temps = df4.iloc[:, 1]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original")
    fig, ax = plt.subplots(figsize=(6, 4))
    colores_orig = plt.cm.rainbow(np.linspace(0, 1, len(dias)))
    ax.bar(dias, temps, color=colores_orig)
    ax.set_facecolor('#FFFFF0')
    ax.set_title('TEMP_DAILY_AVG_DATASET_v2.3')
    ax.set_xlabel('Dia del mes')
    ax.set_ylabel('Valores')
    st.pyplot(fig)

with col2:
    st.subheader("Mejorada")
    fig, ax = plt.subplots(figsize=(6, 4))
    width = 0.9
    for i, temp in enumerate(temps):
        gradient = np.linspace(1, 0, 256).reshape(-1, 1)
        ax.imshow(gradient, extent=(i - width/2, i + width/2, 0, temp),
                  cmap="coolwarm", aspect="auto", zorder=1)
        ax.add_patch(plt.Rectangle((i - width/2, 0), width, temp,
                                   fill=False, edgecolor="black", linewidth=1, zorder=2))
        ax.text(i, temp + 0.3, f"{temp:.1f}", ha="center", fontsize=7)
    ax.set_xlim(-0.5, len(dias) - 0.5)
    ax.set_xticks(range(len(dias)))
    ax.set_xticklabels(dias)
    ax.set_ylim(0, max(temps) + 3)
    ax.set_title("Temperatura promedio diaria", fontsize=12)
    ax.set_xlabel("Día del mes")
    ax.set_ylabel("Temperatura")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    st.pyplot(fig)

# Ventas trimestrales
# Menu lateral
st.sidebar.markdown("### 5. Marketing y Ventas")
st.sidebar.markdown("""
- **Original:** colores rojos/naranjas similares, difícil distinguir trimestres
- **Mejora:** paleta de verdes progresivos, se añadió anotación del mejor producto
""")
st.header("Ventas Trimestrales")
df5 = pd.read_csv("datos/ventas_trimestrales.csv")
df_pivot = df5.pivot(index='Producto', columns='Trimestre', values='Ventas').reset_index()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Original")
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.arange(len(df_pivot['Producto']))
    width = 0.2
    ax.bar(x - 1.5*width, df_pivot['Q1 2024'], width, label='Q1 2024', color='red')
    ax.bar(x - 0.5*width, df_pivot['Q2 2024'], width, label='Q2 2024', color='tomato')
    ax.bar(x + 0.5*width, df_pivot['Q3 2024'], width, label='Q3 2024', color='orange')
    ax.bar(x + 1.5*width, df_pivot['Q4 2024'], width, label='Q4 2024', color='gold')
    ax.set_title('Gráfico de Barras')
    ax.set_xlabel('Productos')
    ax.set_ylabel('ventas')
    ax.set_xticks(x)
    ax.set_xticklabels(df_pivot['Producto'])
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("Mejorada")
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.arange(len(df_pivot['Producto']))
    width = 0.2
    colors = ["#E8F5E9", "#C8E6C9", "#81C784", "#2E7D32"]
    ax.bar(x - 1.5*width, df_pivot['Q1 2024'], width, label='Q1 2024', color=colors[0])
    ax.bar(x - 0.5*width, df_pivot['Q2 2024'], width, label='Q2 2024', color=colors[1])
    ax.bar(x + 0.5*width, df_pivot['Q3 2024'], width, label='Q3 2024', color=colors[2])
    ax.bar(x + 1.5*width, df_pivot['Q4 2024'], width, label='Q4 2024', color=colors[3])
    ax.set_title('Ventas Trimestrales 2024\nComparación por producto', fontsize=11, fontweight='bold')
    ax.set_xlabel('Producto', fontsize=9)
    ax.set_ylabel('Ventas', fontsize=9)
    ax.set_xticks(x)
    ax.set_xticklabels(df_pivot['Producto'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4)
    ax.legend(title="Trimestre")
    df_pivot['Total'] = df_pivot[['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']].sum(axis=1)
    mejor = df_pivot.loc[df_pivot['Total'].idxmax()]
    indice = df_pivot['Total'].idxmax()
    ax.annotate(f"Mejor desempeño:\n{mejor['Producto']}",
                xy=(indice + 1.5*width, mejor['Q4 2024']),
                xytext=(indice + 1.5*width, mejor['Q4 2024'] + 5000),
                arrowprops=dict(arrowstyle='->', lw=1.5),
                ha='center', fontsize=9, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
