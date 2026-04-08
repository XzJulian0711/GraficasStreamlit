import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Visualizaciones", layout="wide")

# ── SIDEBAR ─────────────────────────────────────────────────────────────
st.sidebar.title("Panel de Control")

modo = st.sidebar.radio("Tipo de Visualización:", ["Estáticas (Matplotlib)", "Interactivas (Plotly)"])

st.sidebar.markdown("---")

opcion = st.sidebar.selectbox("Selecciona una Visualización:", [
    "1. Ventas Trimestrales",
    "2. Temperatura Diaria",
    "3. Satisfacción del Cliente",
    "4. Marketing y Ventas",
    "5. Presupuesto Departamentos"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### Visualizaciones Interactivas")
st.sidebar.markdown("**Características:**")
st.sidebar.markdown("- Hover para detalles\n- Zoom y Pan\n- Descarga de imágenes\n- Exploración de datos")

st.sidebar.markdown("---")
st.sidebar.markdown("### Principios Aplicados")
st.sidebar.markdown("Unidad 1: Fundamentos")
st.sidebar.markdown("Unidad 2: Teoría del Color")
st.sidebar.markdown("Unidad 3: Diseño Gráfico")

# ── TÍTULO ───────────────────────────────────────────────────────────────
st.title("Visualizaciones Corregidas - Soluciones")
st.caption(f"Modo actual: {modo}")

# ── CARGAR DATOS ─────────────────────────────────────────────────────────
df1 = pd.read_csv("datos/marketing_ventas.csv").sort_values(by='Inversion_Marketing_USD').reset_index(drop=True)
df2 = pd.read_csv("datos/presupuesto_departamentos.csv").sort_values(by='Presupuesto_Porcentaje', ascending=False)
df3 = pd.read_csv("datos/satisfaccion_cliente.csv")
df4 = pd.read_csv("datos/temperatura_diaria.csv")
df4.columns = df4.columns.str.strip().str.lower()
df5 = pd.read_csv("datos/ventas_trimestrales.csv")
df_pivot = df5.pivot(index='Producto', columns='Trimestre', values='Ventas').reset_index()

# ════════════════════════════════════════════════════════════════════════
# 1. VENTAS TRIMESTRALES
# ════════════════════════════════════════════════════════════════════════
if opcion == "1. Ventas Trimestrales":
    st.header("Visualización 1: Ventas Trimestrales")
    col_graf, col_info = st.columns([3, 1])

    with col_info:
        st.markdown("### Mejoras Implementadas")
        st.markdown("**Unidad 2: Teoría del Color**")
        st.markdown("- Paleta de verdes progresivos\n- Jerarquía visual por trimestre")
        st.markdown("**Unidad 3: Diseño Gráfico**")
        st.markdown("- Anotación del mejor producto\n- Bordes y grillas limpias")
        st.markdown("**Unidad 1: Fundamentos**")
        st.markdown("- Título descriptivo\n- Etiquetas de ejes claras")
        if st.button("Ver datos", key="v1"):
            st.dataframe(df5)

    with col_graf:
        x = np.arange(len(df_pivot['Producto']))
        width = 0.2
        colors_orig = ["red", "tomato", "orange", "gold"]
        colors_mejor = ["#E8F5E9", "#C8E6C9", "#81C784", "#2E7D32"]
        trimestres = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']

        if modo == "Estáticas (Matplotlib)":
            st.subheader("Versión Original")
            fig, ax = plt.subplots(figsize=(8, 4))
            for i, (t, c) in enumerate(zip(trimestres, colors_orig)):
                ax.bar(x + (i-1.5)*width, df_pivot[t], width, label=t, color=c)
            ax.set_title('Gráfico de Barras')
            ax.set_xlabel('Productos')
            ax.set_ylabel('ventas')
            ax.set_xticks(x)
            ax.set_xticklabels(df_pivot['Producto'])
            ax.legend()
            st.pyplot(fig)

            st.subheader("Versión Mejorada")
            fig, ax = plt.subplots(figsize=(8, 4))
            for i, (t, c) in enumerate(zip(trimestres, colors_mejor)):
                ax.bar(x + (i-1.5)*width, df_pivot[t], width, label=t, color=c)
            df_pivot['Total'] = df_pivot[trimestres].sum(axis=1)
            mejor = df_pivot.loc[df_pivot['Total'].idxmax()]
            indice = df_pivot['Total'].idxmax()
            ax.annotate(f"Mejor desempeño:\n{mejor['Producto']}",
                        xy=(indice + 1.5*width, mejor['Q4 2024']),
                        xytext=(indice + 1.5*width, mejor['Q4 2024'] + 5000),
                        arrowprops=dict(arrowstyle='->', lw=1.5),
                        ha='center', fontsize=9, fontweight='bold')
            ax.set_title('Ventas Trimestrales 2024', fontweight='bold')
            ax.set_xlabel('Producto')
            ax.set_ylabel('Ventas')
            ax.set_xticks(x)
            ax.set_xticklabels(df_pivot['Producto'])
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.yaxis.grid(True, linestyle='--', alpha=0.4)
            ax.legend(title="Trimestre")
            plt.tight_layout()
            st.pyplot(fig)

        else:
            st.subheader("Versión Interactiva")
            fig = go.Figure()
            for t, c in zip(trimestres, colors_mejor):
                fig.add_trace(go.Bar(name=t, x=df_pivot['Producto'], y=df_pivot[t]))
            fig.update_layout(barmode='group', title='Ventas Trimestrales 2024',
                              xaxis_title='Producto', yaxis_title='Ventas',
                              plot_bgcolor='white')
            fig.update_yaxes(gridcolor='lightgray', gridwidth=0.5)
            st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════
# 2. TEMPERATURA DIARIA
# ════════════════════════════════════════════════════════════════════════
elif opcion == "2. Temperatura Diaria":
    st.header("Visualización 2: Temperatura Diaria")
    col_graf, col_info = st.columns([3, 1])
    dias = df4.iloc[:, 0]
    temps = df4.iloc[:, 1]

    with col_info:
        st.markdown("### Mejoras Implementadas")
        st.markdown("**Unidad 2: Teoría del Color**")
        st.markdown("- Gradiente coolwarm (azul=frío, rojo=calor)\n- Color con significado físico")
        st.markdown("**Unidad 3: Diseño Gráfico**")
        st.markdown("- Fondo limpio\n- Valores encima de cada barra")
        st.markdown("**Unidad 1: Fundamentos**")
        st.markdown("- Título descriptivo\n- Grilla sutil")
        if st.button("Ver datos", key="v2"):
            st.dataframe(df4)

    with col_graf:
        if modo == "Estáticas (Matplotlib)":
            st.subheader("Versión Original")
            fig, ax = plt.subplots(figsize=(10, 4))
            colores_orig = plt.cm.rainbow(np.linspace(0, 1, len(dias)))
            ax.bar(dias, temps, color=colores_orig)
            ax.set_facecolor('#FFFFF0')
            ax.set_title('TEMP_DAILY_AVG_DATASET_v2.3')
            ax.set_xlabel('Dia del mes')
            ax.set_ylabel('Valores')
            st.pyplot(fig)

            st.subheader("Versión Mejorada")
            fig, ax = plt.subplots(figsize=(10, 4))
            width = 0.9
            for i, temp in enumerate(temps):
                gradient = np.linspace(1, 0, 256).reshape(-1, 1)
                ax.imshow(gradient, extent=(i-width/2, i+width/2, 0, temp),
                          cmap="coolwarm", aspect="auto", zorder=1)
                ax.add_patch(plt.Rectangle((i-width/2, 0), width, temp,
                                           fill=False, edgecolor="black", linewidth=1, zorder=2))
                ax.text(i, temp+0.3, f"{temp:.1f}", ha="center", fontsize=7)
            ax.set_xlim(-0.5, len(dias)-0.5)
            ax.set_xticks(range(len(dias)))
            ax.set_xticklabels(dias)
            ax.set_ylim(0, max(temps)+3)
            ax.set_title("Temperatura promedio diaria", fontsize=12)
            ax.set_xlabel("Día del mes")
            ax.set_ylabel("Temperatura")
            ax.grid(axis="y", linestyle="--", alpha=0.4)
            plt.tight_layout()
            st.pyplot(fig)

        else:
            st.subheader("Versión Interactiva")
            colores_plot = temps.tolist()
            fig = go.Figure(go.Bar(
                x=dias, y=temps,
                marker=dict(color=colores_plot, colorscale='RdBu_r',
                            showscale=True, colorbar=dict(title="°C")),
                text=[f"{t:.1f}°C" for t in temps],
                textposition='outside'
            ))
            fig.update_layout(title="Temperatura promedio diaria",
                              xaxis_title="Día del mes", yaxis_title="Temperatura (°C)",
                              plot_bgcolor='white')
            fig.update_yaxes(gridcolor='lightgray')
            st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════
# 3. SATISFACCIÓN DEL CLIENTE
# ════════════════════════════════════════════════════════════════════════
elif opcion == "3. Satisfacción del Cliente":
    st.header("Visualización 3: Satisfacción del Cliente")
    col_graf, col_info = st.columns([3, 1])
    categorias = df3["Categoria"].tolist()
    valores = df3["Puntuacion"].tolist()
    y = np.arange(len(categorias))

    with col_info:
        st.markdown("### Mejoras Implementadas")
        st.markdown("**Unidad 2: Teoría del Color**")
        st.markdown("- Paleta divergente Rojo/Azul\n- Rojo negativo, azul positivo")
        st.markdown("**Unidad 3: Diseño Gráfico**")
        st.markdown("- Línea de referencia en 0\n- Escala simétrica\n- Etiquetas de valores")
        st.markdown("**Unidad 1: Fundamentos**")
        st.markdown("- Ordenamiento por valor")
        if st.button("Ver datos", key="v3"):
            st.dataframe(df3)

    with col_graf:
        if modo == "Estáticas (Matplotlib)":
            st.subheader("Versión Original")
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.barh(y, valores, color='green', edgecolor='black', linewidth=2)
            ax.axvline(0, color='black', linewidth=1)
            ax.set_yticks(y)
            ax.set_yticklabels(categorias)
            ax.set_xlim(-2, 3)
            ax.set_xlabel("Score")
            ax.set_title("Encuesta", color='purple', fontweight='bold')
            ax.yaxis.grid(True, linestyle='--', color='red', alpha=0.5)
            st.pyplot(fig)

            st.subheader("Versión Mejorada")
            positivos = [v if v > 0 else 0 for v in valores]
            negativos = [v if v < 0 else 0 for v in valores]
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.barh(y, negativos, color="#e74c3c", label="Insatisfacción")
            ax.barh(y, positivos, color="#2ecc71", label="Satisfacción")
            ax.axvline(0, color='black', linewidth=1)
            ax.set_yticks(y)
            ax.set_yticklabels(categorias)
            ax.set_xlabel("Nivel de satisfacción (-2 a +2)")
            ax.set_title("Encuesta de Satisfacción del Cliente")
            ax.set_xlim(-2, 2)
            ax.set_xticks([-2, -1, 0, 1, 2])
            ax.grid(axis='x', linestyle='--', alpha=0.4)
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)

        else:
            st.subheader("Versión Interactiva")
            df3_sorted = df3.sort_values('Puntuacion')
            colors_plotly = ['#e74c3c' if v < 0 else '#2980b9' for v in df3_sorted['Puntuacion']]
            fig = go.Figure(go.Bar(
                x=df3_sorted['Puntuacion'],
                y=df3_sorted['Categoria'],
                orientation='h',
                marker_color=colors_plotly,
                text=[f"{v:.1f}" for v in df3_sorted['Puntuacion']],
                textposition='outside'
            ))
            max_val = max(abs(v) for v in valores)
            fig.add_vline(x=0, line_color='black', line_width=1)
            fig.update_layout(
                title=f"{df3_sorted.loc[df3_sorted['Puntuacion'].idxmin(), 'Categoria']} es el mayor desafío<br><sub>Escala: -2 (Muy insatisfecho) a +2 (Muy satisfecho)</sub>",
                xaxis=dict(range=[-2, 2], tickvals=[-2, -1, 0, 1, 2]),
                plot_bgcolor='white', xaxis_title="Nivel de satisfacción"
            )
            fig.update_xaxes(gridcolor='lightgray')
            st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════
# 4. MARKETING Y VENTAS
# ════════════════════════════════════════════════════════════════════════
elif opcion == "4. Marketing y Ventas":
    st.header("Visualización 4: Marketing y Ventas")
    col_graf, col_info = st.columns([3, 1])
    x = np.arange(len(df1))
    width = 0.4

    with col_info:
        st.markdown("### Mejoras Implementadas")
        st.markdown("**Unidad 2: Teoría del Color**")
        st.markdown("- Colores diferenciados sin bordes llamativos\n- Paleta profesional")
        st.markdown("**Unidad 3: Diseño Gráfico**")
        st.markdown("- Etiquetas de valor en cada barra\n- Grilla sutil")
        st.markdown("**Unidad 1: Fundamentos**")
        st.markdown("- Datos ordenados por inversión\n- Título claro")
        if st.button("Ver datos", key="v4"):
            st.dataframe(df1)

    with col_graf:
        if modo == "Estáticas (Matplotlib)":
            st.subheader("Versión Original")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(x - width/2, df1['Inversion_Marketing_USD'], width,
                   color='red', edgecolor='yellow', linewidth=2, label='Inversión Marketing')
            ax.bar(x + width/2, df1['Ventas_Generadas_USD'], width,
                   color='blue', edgecolor='yellow', linewidth=2, label='Ventas Generadas')
            ax.set_title("Datos de la empresa 2024")
            ax.set_xlabel("Índice")
            ax.set_ylabel("Ventas ($)")
            ax.legend()
            st.pyplot(fig)

            st.subheader("Versión Mejorada")
            fig, ax = plt.subplots(figsize=(10, 4))
            bars1 = ax.bar(x - width/2, df1['Inversion_Marketing_USD'], width,
                           label='Inversión Marketing', color='tomato')
            bars2 = ax.bar(x + width/2, df1['Ventas_Generadas_USD'], width,
                           label='Ventas Generadas', color='royalblue')
            for bar in bars1:
                h = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, h+500, f'{int(h)}', ha='center', fontsize=7)
            for bar in bars2:
                h = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, h+500, f'{int(h)}', ha='center', fontsize=7)
            ax.set_title("Relación entre Inversión en Marketing y Ventas", fontsize=11)
            ax.set_xlabel("Registros de datos")
            ax.set_ylabel("Valor en dólares ($)")
            ax.grid(axis='y', linestyle='--', alpha=0.5)
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)

        else:
            st.subheader("Versión Interactiva")
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Inversión Marketing', x=list(range(len(df1))),
                                 y=df1['Inversion_Marketing_USD'], marker_color='tomato'))
            fig.add_trace(go.Bar(name='Ventas Generadas', x=list(range(len(df1))),
                                 y=df1['Ventas_Generadas_USD'], marker_color='royalblue'))
            fig.update_layout(barmode='group', title="Relación entre Inversión en Marketing y Ventas",
                              xaxis_title="Registros de datos", yaxis_title="Valor en dólares ($)",
                              plot_bgcolor='white')
            fig.update_yaxes(gridcolor='lightgray', gridwidth=0.5)
            st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════
# 5. PRESUPUESTO DEPARTAMENTOS
# ════════════════════════════════════════════════════════════════════════
elif opcion == "5. Presupuesto Departamentos":
    st.header("Visualización 5: Presupuesto por Departamento")
    col_graf, col_info = st.columns([3, 1])

    with col_info:
        st.markdown("### Mejoras Implementadas")
        st.markdown("**Unidad 2: Teoría del Color**")
        st.markdown("- Paleta cualitativa Set3\n- Cada departamento con color único")
        st.markdown("**Unidad 3: Diseño Gráfico**")
        st.markdown("- Bordes blancos entre secciones\n- Porcentajes legibles")
        st.markdown("**Unidad 1: Fundamentos**")
        st.markdown("- Título descriptivo\n- Orden de mayor a menor")
        if st.button("Ver datos", key="v5"):
            st.dataframe(df2)

    with col_graf:
        if modo == "Estáticas (Matplotlib)":
            st.subheader("Versión Original")
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(df2['Presupuesto_Porcentaje'], labels=df2['Departamento'],
                   autopct='%1.1f%%', colors=['#F08080']*len(df2),
                   startangle=140, wedgeprops=dict(edgecolor='gray', linewidth=1.5))
            ax.set_title('Gráfico Circular', fontweight='bold', fontsize=13)
            st.pyplot(fig)

            st.subheader("Versión Mejorada")
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

        else:
            st.subheader("Versión Interactiva")
            fig = go.Figure(go.Pie(
                labels=df2['Departamento'],
                values=df2['Presupuesto_Porcentaje'],
                hole=0.3,
                textinfo='label+percent',
                marker=dict(colors=px_colors if False else
                            ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3',
                             '#fdb462','#b3de69','#fccde5'])
            ))
            fig.update_layout(title='Distribución de Presupuesto por Departamento')
            st.plotly_chart(fig, use_container_width=True)