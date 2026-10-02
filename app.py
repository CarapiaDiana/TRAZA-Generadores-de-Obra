import streamlit as st
import html
import math
import csv
import io
from pathlib import Path

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="TRAZA | Generadores de Obra",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# IDENTIDAD VISUAL TRAZA
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #F4F1E8;
    color: #252923;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ============================================================
   SIDEBAR
============================================================ */

section[data-testid="stSidebar"] {
    background-color: #344238;
}

section[data-testid="stSidebar"] * {
    color: #F4F1E8;
}

.sidebar-logo {
    font-size: 34px;
    font-weight: 700;
    letter-spacing: 7px;
    color: #F4F1E8;
    margin-bottom: 4px;
}

.sidebar-sub {
    color: #C9D0C3;
    font-size: 13px;
    letter-spacing: 1px;
    margin-bottom: 30px;
}

.sidebar-titulo {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #A8B59F;
    margin-top: 25px;
    margin-bottom: 10px;
}

.sidebar-item-activo {
    background: #F4F1E8;
    color: #344238 !important;
    padding: 11px 14px;
    border-radius: 9px;
    font-weight: 700;
    margin-bottom: 8px;
}

.sidebar-item {
    padding: 8px 14px;
    color: #D9DED5 !important;
    margin-bottom: 4px;
}


/* ============================================================
   ENCABEZADO
============================================================ */

.marca {
    font-size: 18px;
    letter-spacing: 6px;
    font-weight: 700;
    color: #6F8068;
    margin-bottom: 8px;
}

.titulo-principal {
    font-size: 46px;
    line-height: 1.05;
    font-weight: 700;
    color: #252923;
    margin-bottom: 8px;
}

.subtitulo {
    font-size: 17px;
    color: #6F746B;
    margin-bottom: 32px;
}


/* ============================================================
   SECCIONES
============================================================ */

.seccion {
    font-size: 27px;
    font-weight: 700;
    color: #344238;
    margin-top: 34px;
    margin-bottom: 15px;
}

.seccion-mini {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #6F8068;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.linea {
    border-top: 1px solid #DCD8CA;
    margin: 28px 0;
}


/* ============================================================
   TARJETAS
============================================================ */

.tarjeta {
    background-color: #FCFBF7;
    border: 1px solid #DDD9CE;
    border-radius: 16px;
    padding: 22px 24px;
    margin-bottom: 18px;
    box-shadow: 0px 2px 10px rgba(37, 41, 35, 0.04);
}

.tarjeta-verde {
    background-color: #344238;
    border-radius: 16px;
    padding: 24px 26px;
    margin: 20px 0;
}

.tarjeta-verde .label {
    color: #C8D1C3;
    font-size: 13px;
    letter-spacing: 2px;
}

.tarjeta-verde .numero {
    color: #F4F1E8;
    font-size: 42px;
    font-weight: 600;
    margin-top: 3px;
}

.tarjeta-resultado {
    background-color: #E3E8DE;
    border-left: 5px solid #6F8068;
    border-radius: 10px;
    padding: 15px 18px;
    margin-top: 14px;
}

.muro-titulo {
    font-size: 22px;
    font-weight: 700;
    color: #344238;
    margin-bottom: 4px;
}

.muro-numero {
    color: #6F8068;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 700;
}


/* ============================================================
   RESULTADOS
============================================================ */

.resumen {
    font-size: 16px;
    color: #252923;
    padding: 10px 0;
    border-bottom: 1px solid #E2DED3;
}

.detalle {
    font-size: 15px;
    line-height: 1.75;
    color: #383D37;
    background-color: #FCFBF7;
    border: 1px solid #E2DED3;
    border-radius: 12px;
    padding: 17px 20px;
    margin-bottom: 12px;
}

.clave {
    display: inline-block;
    background-color: #344238;
    color: #F4F1E8;
    padding: 5px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 10px;
}

.dato {
    margin-top: 10px;
}

.dato strong {
    color: #6F8068;
    font-size: 12px;
    letter-spacing: 1px;
}


/* ============================================================
   INPUTS
============================================================ */

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
textarea {
    background-color: #FCFBF7 !important;
    border-color: #D5D1C7 !important;
    border-radius: 9px !important;
}

div[data-testid="stFileUploader"] {
    background-color: #FCFBF7;
    border: 1px dashed #A8B59F;
    border-radius: 14px;
    padding: 10px;
}

div[data-testid="stAlert"] {
    border-radius: 10px;
}

.stButton > button {
    background-color: #344238;
    color: #F4F1E8;
    border: none;
    border-radius: 9px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #6F8068;
    color: #F4F1E8;
    border: none;
}

.stDownloadButton > button {
    background-color: #344238;
    color: #F4F1E8;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1.2rem;
    font-weight: 600;
    min-height: 46px;
}

.stDownloadButton > button:hover {
    background-color: #6F8068;
    color: #F4F1E8;
    border: none;
}

.stDownloadButton > button:focus {
    border: none;
    box-shadow: none;
}

</style>
""",
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    from pathlib import Path

    logo_path = Path(__file__).parent / "traza_logo.png"

    st.markdown(
        """
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            padding-top: 8px;
            margin-bottom: 22px;
        ">
        """,
        unsafe_allow_html=True
    )

    st.image(str(logo_path), width=245)

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="sidebar-titulo">PROYECTO</div>
<div class="sidebar-item">⌂ Información general</div>
<div class="sidebar-item">▱ Plano arquitectónico</div>

<div class="sidebar-titulo">CUANTIFICACIÓN</div>
<div class="sidebar-item-activo">Muros</div>
<div class="sidebar-item">Pisos · Próximamente</div>
<div class="sidebar-item">Plafones · Próximamente</div>
<div class="sidebar-item">Acabados · Próximamente</div>

<div class="sidebar-titulo">RESULTADOS</div>
<div class="sidebar-item">Resumen</div>
<div class="sidebar-item">Catálogo de conceptos</div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ENCABEZADO PRINCIPAL
# ============================================================

st.markdown(
    '<div class="marca">TRAZA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="titulo-principal">Generadores de Obra</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="subtitulo">
Sistema de cuantificación y generación de conceptos para proyectos de construcción.
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# DATOS DEL PROYECTO
# ============================================================

st.markdown(
    '<div class="seccion-mini">01 / Proyecto</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Información del proyecto</div>',
    unsafe_allow_html=True
)

col_proy1, col_proy2 = st.columns(2)

with col_proy1:

    nombre_proyecto = st.text_input(
        "Nombre del proyecto",
        placeholder="Ej. Casa Habitación Morelia"
    )

with col_proy2:

    ubicacion_proyecto = st.text_input(
        "Ubicación",
        placeholder="Ej. Morelia, Michoacán"
    )


# ============================================================
# CARGA DEL PLANO PDF
# ============================================================

st.markdown(
    '<div class="seccion">Plano arquitectónico</div>',
    unsafe_allow_html=True
)

st.write(
    "Carga el plano de referencia del proyecto en formato PDF."
)

archivo_plano = st.file_uploader(
    "Seleccionar plano",
    type=["pdf"],
    accept_multiple_files=False
)

if archivo_plano is not None:

    nombre_pdf = html.escape(archivo_plano.name)
    tamano_kb = archivo_plano.size / 1024

    st.success(
        f"Plano cargado correctamente: {archivo_plano.name}"
    )

    st.markdown(
        f"""
<div class="tarjeta">
<div class="seccion-mini">ARCHIVO DEL PROYECTO</div>
<strong>{nombre_pdf}</strong><br>
<span style="color:#747A71;">
PDF · {tamano_kb:,.1f} KB
</span>
</div>
""",
        unsafe_allow_html=True
    )


st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)


# ============================================================
# GENERADOR DE MUROS
# ============================================================

st.markdown(
    '<div class="seccion-mini">02 / Cuantificación</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Generador de muros</div>',
    unsafe_allow_html=True
)

st.write(
    "Captura las dimensiones de cada muro y TRAZA calculará automáticamente el área neta."
)


# ============================================================
# CANTIDAD DE MUROS
# ============================================================

cantidad_muros = st.number_input(
    "¿Cuántos muros deseas cuantificar?",
    min_value=1,
    max_value=100,
    value=1,
    step=1
)


# ============================================================
# TIPOS DE MURO
# ============================================================

tipos_muro = [
    "Muro de tablaroca",
    "Muro de block",
    "Muro de concreto",
    "Muro de ladrillo"
]

muros = []


# ============================================================
# CAPTURA DE MUROS
# ============================================================

for i in range(int(cantidad_muros)):

    numero_muro = i + 1

    st.markdown(
        '<div class="linea"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="muro-numero">MURO {numero_muro:02d}</div>
<div class="muro-titulo">Datos del muro</div>
""",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        tipo = st.selectbox(
            "Tipo de muro",
            tipos_muro,
            key=f"tipo_muro_{numero_muro}"
        )

    with col2:

        largo = st.number_input(
            "Largo (m)",
            min_value=0.0,
            value=0.0,
            step=0.10,
            format="%.2f",
            key=f"largo_muro_{numero_muro}"
        )

    with col3:

        alto = st.number_input(
            "Alto (m)",
            min_value=0.0,
            value=2.90,
            step=0.10,
            format="%.2f",
            key=f"alto_muro_{numero_muro}"
        )


    # ========================================================
    # ÁREA BRUTA
    # ========================================================

    area_bruta = largo * alto

    st.markdown(
        f"""
<div class="tarjeta-resultado">
<strong>Área bruta</strong><br>
<span style="font-size:26px;">
{area_bruta:,.2f} m²
</span>
</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # VANOS
    # ========================================================

    cantidad_vanos = st.number_input(
        f"¿Cuántos vanos tiene el muro {numero_muro}?",
        min_value=0,
        max_value=50,
        value=0,
        step=1,
        key=f"cantidad_vanos_{numero_muro}"
    )

    descuento_total = 0.0


    if cantidad_vanos > 0:

        st.markdown("#### Vanos")

        for j in range(int(cantidad_vanos)):

            numero_vano = j + 1

            col_a, col_b = st.columns(2)

            with col_a:

                ancho_vano = st.number_input(
                    f"Ancho del vano {numero_vano} (m)",
                    min_value=0.0,
                    value=0.0,
                    step=0.10,
                    format="%.2f",
                    key=f"ancho_vano_{numero_muro}_{numero_vano}"
                )

            with col_b:

                alto_vano = st.number_input(
                    f"Alto del vano {numero_vano} (m)",
                    min_value=0.0,
                    value=0.0,
                    step=0.10,
                    format="%.2f",
                    key=f"alto_vano_{numero_muro}_{numero_vano}"
                )

            area_vano = ancho_vano * alto_vano

            descuento_total += area_vano

            st.caption(
                f"Vano {numero_vano}: {area_vano:,.2f} m²"
            )


    # ========================================================
    # ÁREA NETA
    # ========================================================

    area_neta = max(
        area_bruta - descuento_total,
        0.0
    )

    st.markdown(
        f"""
<div class="tarjeta-resultado">
<strong>Área neta del muro</strong><br>
<span style="font-size:28px; color:#344238;">
{area_neta:,.2f} m²
</span><br>
<span style="font-size:13px; color:#70766E;">
Descuento de vanos: {descuento_total:,.2f} m²
</span>
</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # GUARDAR DATOS
    # ========================================================

    muros.append(
        {
            "numero": numero_muro,
            "tipo": tipo,
            "largo": largo,
            "alto": alto,
            "area_bruta": area_bruta,
            "descuento": descuento_total,
            "area_neta": area_neta
        }
    )


# ============================================================
# CÁLCULOS GENERALES
# ============================================================

total_muros = sum(
    muro["area_neta"]
    for muro in muros
)

total_bruto = sum(
    muro["area_bruta"]
    for muro in muros
)

total_descuentos = sum(
    muro["descuento"]
    for muro in muros
)


# ============================================================
# RESULTADOS
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">03 / Resultados</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Resumen del generador</div>',
    unsafe_allow_html=True
)


col_r1, col_r2, col_r3, col_r4 = st.columns(4)

with col_r1:

    st.metric(
        "Muros",
        len(muros)
    )

with col_r2:

    st.metric(
        "Área bruta",
        f"{total_bruto:,.2f} m²"
    )

with col_r3:

    st.metric(
        "Descuentos",
        f"{total_descuentos:,.2f} m²"
    )

with col_r4:

    st.metric(
        "Área neta",
        f"{total_muros:,.2f} m²"
    )


# ============================================================
# TOTAL DE MUROS
# ============================================================

st.markdown(
    f"""
<div class="tarjeta-verde">
<div class="label">TOTAL DE MUROS</div>
<div class="numero">{total_muros:,.2f} m²</div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# RESUMEN POR TIPO
# ============================================================

resumen_final = {
    "Muro de tablaroca": 0.0,
    "Muro de block": 0.0,
    "Muro de concreto": 0.0,
    "Muro de ladrillo": 0.0
}


for muro in muros:

    tipo_actual = muro["tipo"]

    if tipo_actual in resumen_final:

        resumen_final[tipo_actual] += muro["area_neta"]


st.markdown(
    '<div class="seccion">Resumen por tipo de muro</div>',
    unsafe_allow_html=True
)


for tipo_resumen, area_resumen in resumen_final.items():

    st.markdown(
        f"""
<div class="resumen">
<strong>{html.escape(tipo_resumen)}</strong>
<span style="float:right;">
{area_resumen:,.2f} m²
</span>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# DETALLE DE COMPROBACIÓN
# ============================================================

with st.expander("Ver detalle de comprobación"):

    for muro in muros:

        tipo_seguro = html.escape(muro["tipo"])

        st.markdown(
            f"""
<div class="detalle">
<strong>Muro {muro["numero"]:02d}</strong><br>
{tipo_seguro}<br>
Área bruta: {muro["area_bruta"]:,.2f} m²<br>
Descuento: {muro["descuento"]:,.2f} m²<br>
<strong>Área neta: {muro["area_neta"]:,.2f} m²</strong>
</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# CONCEPTOS
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">04 / Conceptos</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Catálogo de conceptos</div>',
    unsafe_allow_html=True
)

st.write(
    "Escribe el concepto correspondiente a cada tipo de muro."
)


conceptos = {}


for tipo_concepto in tipos_muro:

    st.markdown(
        f"#### {tipo_concepto}"
    )

    concepto = st.text_area(
        f"Concepto para {tipo_concepto}",
        key=f"concepto_{tipo_concepto}",
        placeholder="Ej. Suministro y colocación de muro...",
        height=90,
        label_visibility="collapsed"
    )

    conceptos[tipo_concepto] = concepto


# ============================================================
# TIPOS UTILIZADOS
# ============================================================

tipos_utilizados = []


for muro in muros:

    if (
        muro["area_neta"] > 0
        and muro["tipo"] not in tipos_utilizados
    ):

        tipos_utilizados.append(
            muro["tipo"]
        )


# ============================================================
# CATÁLOGO FINAL DE CONCEPTOS
# ============================================================

st.markdown(
    '<div class="seccion">📑 Catálogo final de conceptos</div>',
    unsafe_allow_html=True
)


if len(tipos_utilizados) == 0:

    st.info(
        "Captura al menos un muro con un área mayor a 0.00 m² para generar el catálogo."
    )


else:

    for indice, tipo in enumerate(tipos_utilizados, start=1):

        # ----------------------------------------------------
        # CANTIDAD TOTAL DEL TIPO DE MURO
        # ----------------------------------------------------

        cantidad_tipo = sum(
            muro["area_neta"]
            for muro in muros
            if muro["tipo"] == tipo
        )


        # ----------------------------------------------------
        # CONCEPTO
        # ----------------------------------------------------

        concepto = conceptos.get(tipo, "").strip()

        if concepto == "":
            concepto = "Sin concepto capturado"


        # ----------------------------------------------------
        # PROTEGER TEXTO PARA HTML
        # ----------------------------------------------------

        tipo_seguro = html.escape(tipo)
        concepto_seguro = html.escape(concepto)


        # ----------------------------------------------------
        # CLAVE
        # ----------------------------------------------------

        clave = f"MU-{indice:02d}"


        # ----------------------------------------------------
        # CATÁLOGO
        # ----------------------------------------------------

        html_catalogo = f"""
<div class="detalle">
<div class="clave">{clave}</div>
<div class="dato"><strong>TIPO</strong><br>{tipo_seguro}</div>
<div class="dato"><strong>CONCEPTO</strong><br>{concepto_seguro}</div>
<div class="dato"><strong>UNIDAD</strong><br>m²</div>
<div class="dato"><strong>CANTIDAD</strong><br>{cantidad_tipo:,.2f} m²</div>
</div>
"""


        st.markdown(
            html_catalogo,
            unsafe_allow_html=True
        )


        if indice < len(tipos_utilizados):

            st.markdown(
                '<div class="linea"></div>',
                unsafe_allow_html=True
            )

# ============================================================
# 05 / MATERIALES
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">05 / Materiales</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Generador de materiales</div>',
    unsafe_allow_html=True
)

st.write(
    "Consulta la composición y cantidad estimada de materiales "
    "asociados a cada sistema constructivo."
)


# ============================================================
# CONFIGURACIÓN DEL SISTEMA DE TABLAROCA
# ============================================================

st.markdown(
    '<div class="seccion-mini">Configuración del sistema</div>',
    unsafe_allow_html=True
)

col_tab1, col_tab2, col_tab3 = st.columns(3)


with col_tab1:

    caras_tablaroca = st.selectbox(
        "Caras de tablaroca",
        [1, 2],
        index=1,
        key="caras_tablaroca",
        help=(
            "1 = una cara de tablaroca. "
            "2 = tablaroca en ambas caras."
        )
    )


with col_tab2:

    separacion_postes = st.selectbox(
        "Separación de postes",
        [0.40, 0.60],
        index=1,
        format_func=lambda x: f"{x:.2f} m",
        key="separacion_postes",
        help="Separación entre postes metálicos."
    )


with col_tab3:

    desperdicio = st.selectbox(
        "Desperdicio",
        [0.00, 0.05, 0.10],
        index=1,
        format_func=lambda x: f"{x * 100:.0f} %",
        key="desperdicio_material",
        help="Porcentaje adicional para cortes y desperdicios."
    )


# ============================================================
# FUNCIÓN PARA CALCULAR MATERIALES
# ============================================================

def calcular_materiales_tabaroca(
    muros_tipo,
    caras,
    separacion,
    desperdicio
):

    resultados = []


    # --------------------------------------------------------
    # ÁREA TOTAL
    # --------------------------------------------------------

    area_total = sum(
        muro["area_neta"]
        for muro in muros_tipo
    )


    # --------------------------------------------------------
    # ÁREA DE PLACAS
    # --------------------------------------------------------

    area_placa = (
        area_total
        * caras
        * (1 + desperdicio)
    )

    resultados.append(
        {
            "material": "Placa de tablaroca de 12.5 mm",
            "unidad": "m²",
            "cantidad": area_placa,
            "detalle": (
                f"{area_total:.2f} m² × "
                f"{caras} cara(s) + desperdicio"
            )
        }
    )


    # --------------------------------------------------------
    # CANAL METÁLICO
    # --------------------------------------------------------

    canal_total = 0.0

    for muro in muros_tipo:

        # Canal inferior + canal superior
        canal_muro = muro["largo"] * 2

        canal_total += canal_muro


    canal_total *= (1 + desperdicio)


    resultados.append(
        {
            "material": "Canal metálico",
            "unidad": "m",
            "cantidad": canal_total,
            "detalle": "Canal superior e inferior"
        }
    )


    # --------------------------------------------------------
    # POSTES METÁLICOS
    # --------------------------------------------------------

    postes_total = 0.0
    cantidad_postes = 0


    for muro in muros_tipo:

        largo_muro = muro["largo"]

        if largo_muro > 0:

            postes_muro = (
                int(
                    largo_muro
                    / separacion
                )
                + 1
            )

            cantidad_postes += postes_muro

            postes_total += (
                postes_muro
                * muro["alto"]
            )


    postes_total *= (1 + desperdicio)


    resultados.append(
        {
            "material": "Poste metálico",
            "unidad": "m",
            "cantidad": postes_total,
            "detalle": (
                f"{cantidad_postes} postes × altura"
            )
        }
    )


    # --------------------------------------------------------
    # TORNILLOS PARA TABLAROCA
    # --------------------------------------------------------

    tornillos_tablaroca = (
        area_total
        * caras
        * 15
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Tornillo para tablaroca",
            "unidad": "pza",
            "cantidad": tornillos_tablaroca,
            "detalle": "15 tornillos/m² por cara"
        }
    )


    # --------------------------------------------------------
    # TORNILLOS METAL-METAL
    # --------------------------------------------------------

    tornillos_metal = (
        cantidad_postes
        * 4
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Tornillo metal-metal",
            "unidad": "pza",
            "cantidad": tornillos_metal,
            "detalle": "4 tornillos por poste"
        }
    )


    # --------------------------------------------------------
    # CINTA PARA JUNTAS
    # --------------------------------------------------------

    cinta = (
        area_total
        * caras
        * 1.20
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Cinta para juntas",
            "unidad": "m",
            "cantidad": cinta,
            "detalle": "1.20 m/m² por cara"
        }
    )


    # --------------------------------------------------------
    # COMPUESTO PARA JUNTAS
    # --------------------------------------------------------

    compuesto = (
        area_total
        * caras
        * 0.30
        * (1 + desperdicio)
    )


    resultados.append(
        {
            "material": "Compuesto para juntas",
            "unidad": "kg",
            "cantidad": compuesto,
            "detalle": "0.30 kg/m² por cara"
        }
    )


    # --------------------------------------------------------
    # ESQUINERO
    # --------------------------------------------------------

    esquinero = 0.0


    for muro in muros_tipo:

        esquinero += (
            muro["alto"]
            * 2
        )


    esquinero *= (1 + desperdicio)


    resultados.append(
        {
            "material": "Esquinero",
            "unidad": "m",
            "cantidad": esquinero,
            "detalle": "2 esquineros verticales por muro"
        }
    )


    return resultados


# ============================================================
# TIPOS DE MURO UTILIZADOS
# ============================================================

tipos_materiales_utilizados = []


for muro in muros:

    if (
        muro["area_neta"] > 0
        and muro["tipo"] not in tipos_materiales_utilizados
    ):

        tipos_materiales_utilizados.append(
            muro["tipo"]
        )


# ============================================================
# MOSTRAR MENSAJE SI NO HAY MUROS
# ============================================================

if len(tipos_materiales_utilizados) == 0:

    st.info(
        "Captura al menos un muro con un área mayor a "
        "0.00 m² para generar el listado de materiales."
    )


# ============================================================
# GENERAR MATERIALES
# ============================================================

else:

    for tipo in tipos_materiales_utilizados:


        # ----------------------------------------------------
        # MUROS DEL TIPO ACTUAL
        # ----------------------------------------------------

        muros_tipo = [
            muro
            for muro in muros
            if muro["tipo"] == tipo
            and muro["area_neta"] > 0
        ]


        # ----------------------------------------------------
        # ÁREA TOTAL DEL TIPO
        # ----------------------------------------------------

        area_tipo = sum(
            muro["area_neta"]
            for muro in muros_tipo
        )


        # ----------------------------------------------------
        # ENCABEZADO
        # ----------------------------------------------------

        st.markdown(
            f"""
<div class="seccion-mini">
MATERIAL / {html.escape(tipo.upper())}
</div>

<div class="seccion" style="font-size:22px;">
{html.escape(tipo)}
</div>
""",
            unsafe_allow_html=True
        )


        st.markdown(
            f"""
<div class="tarjeta-resultado">

<strong>Área neta cuantificada</strong><br>

<span style="font-size:28px; color:#344238;">
{area_tipo:,.2f} m²
</span>

</div>
""",
            unsafe_allow_html=True
        )


        # ====================================================
        # TABLAROCA
        # ====================================================

        if tipo == "Muro de tablaroca":

            materiales = calcular_materiales_tabaroca(
                muros_tipo,
                caras_tablaroca,
                separacion_postes,
                desperdicio
            )


            # ------------------------------------------------
            # MOSTRAR MATERIALES
            # ------------------------------------------------

            for material in materiales:

                nombre_material = html.escape(
                    material["material"]
                )

                unidad_material = html.escape(
                    material["unidad"]
                )

                detalle_material = html.escape(
                    material["detalle"]
                )

                cantidad_material = material["cantidad"]


                st.markdown(
                    f"""
<div class="detalle">

<strong>
{nombre_material}
</strong>

<br><br>

<span style="color:#70766E;">
Unidad: {unidad_material}
</span>

<br>

<span style="color:#70766E;">
Criterio: {detalle_material}
</span>

<br><br>

<strong>
Cantidad estimada:
{cantidad_material:,.2f}
{unidad_material}
</strong>

</div>
""",
                    unsafe_allow_html=True
                )


        # ====================================================
        # BLOCK
        # ====================================================

        elif tipo == "Muro de block":

            materiales_block = [

                (
                    "Block de concreto",
                    "pza",
                    area_tipo * 12.50,
                    "12.50 piezas/m²"
                ),

                (
                    "Mortero",
                    "m³",
                    area_tipo * 0.020,
                    "0.020 m³/m²"
                ),

                (
                    "Cemento",
                    "kg",
                    area_tipo * 4.50,
                    "4.50 kg/m²"
                ),

                (
                    "Arena",
                    "m³",
                    area_tipo * 0.020,
                    "0.020 m³/m²"
                )
            ]


            for nombre, unidad, cantidad, criterio in materiales_block:

                st.markdown(
                    f"""
<div class="detalle">

<strong>{html.escape(nombre)}</strong>

<br><br>

<span style="color:#70766E;">
Unidad: {unidad}
</span>

<br>

<span style="color:#70766E;">
Criterio: {criterio}
</span>

<br><br>

<strong>
Cantidad estimada:
{cantidad:,.2f} {unidad}
</strong>

</div>
""",
                    unsafe_allow_html=True
                )


        # ====================================================
        # LADRILLO
        # ====================================================

        elif tipo == "Muro de ladrillo":

            materiales_ladrillo = [

                (
                    "Ladrillo",
                    "pza",
                    area_tipo * 16.00,
                    "16.00 piezas/m²"
                ),

                (
                    "Mortero",
                    "m³",
                    area_tipo * 0.025,
                    "0.025 m³/m²"
                ),

                (
                    "Cemento",
                    "kg",
                    area_tipo * 5.00,
                    "5.00 kg/m²"
                ),

                (
                    "Arena",
                    "m³",
                    area_tipo * 0.025,
                    "0.025 m³/m²"
                )
            ]


            for nombre, unidad, cantidad, criterio in materiales_ladrillo:

                st.markdown(
                    f"""
<div class="detalle">

<strong>{html.escape(nombre)}</strong>

<br><br>

<span style="color:#70766E;">
Unidad: {unidad}
</span>

<br>

<span style="color:#70766E;">
Criterio: {criterio}
</span>

<br><br>

<strong>
Cantidad estimada:
{cantidad:,.2f} {unidad}
</strong>

</div>
""",
                    unsafe_allow_html=True
                )


        # ====================================================
        # CONCRETO
        # ====================================================

        elif tipo == "Muro de concreto":

            materiales_concreto = [

                (
                    "Concreto",
                    "m³",
                    area_tipo * 0.12,
                    "0.12 m³/m²"
                ),

                (
                    "Acero de refuerzo",
                    "kg",
                    area_tipo * 10.00,
                    "10.00 kg/m²"
                ),

                (
                    "Alambre recocido",
                    "kg",
                    area_tipo * 0.20,
                    "0.20 kg/m²"
                ),

                (
                    "Cimbra",
                    "m²",
                    area_tipo * 2.00,
                    "2.00 m²/m²"
                )
            ]


            for nombre, unidad, cantidad, criterio in materiales_concreto:

                st.markdown(
                    f"""
<div class="detalle">

<strong>{html.escape(nombre)}</strong>

<br><br>

<span style="color:#70766E;">
Unidad: {unidad}
</span>

<br>

<span style="color:#70766E;">
Criterio: {criterio}
</span>

<br><br>

<strong>
Cantidad estimada:
{cantidad:,.2f} {unidad}
</strong>

</div>
""",
                    unsafe_allow_html=True
                )


        # ----------------------------------------------------
        # SEPARADOR ENTRE TIPOS
        # ----------------------------------------------------

        st.markdown(
            '<div class="linea"></div>',
            unsafe_allow_html=True
        )

# ============================================================
# 06 / EXPORTACIÓN
# ============================================================

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion-mini">06 / Exportación</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="seccion">Exportar cuantificación</div>',
    unsafe_allow_html=True
)

st.write(
    "Descarga el cuadro de cuantificación generado por TRAZA."
)


# ============================================================
# CREAR ARCHIVO CSV
# ============================================================

csv_buffer = io.StringIO()

writer = csv.writer(csv_buffer)

# Encabezado
writer.writerow([
    "Clave",
    "Tipo de muro",
    "Concepto",
    "Unidad",
    "Largo (m)",
    "Alto (m)",
    "Área bruta (m²)",
    "Descuento vanos (m²)",
    "Área neta (m²)"
])


# Datos de cada muro
for muro in muros:

    concepto_muro = conceptos.get(
        muro["tipo"],
        ""
    ).strip()

    if concepto_muro == "":
        concepto_muro = "Sin concepto capturado"

    clave_muro = f"MU-{muro['numero']:02d}"

    writer.writerow([
        clave_muro,
        muro["tipo"],
        concepto_muro,
        "m²",
        f"{muro['largo']:.2f}",
        f"{muro['alto']:.2f}",
        f"{muro['area_bruta']:.2f}",
        f"{muro['descuento']:.2f}",
        f"{muro['area_neta']:.2f}"
    ])


# ============================================================
# FILA TOTAL
# ============================================================

writer.writerow([])

writer.writerow([
    "TOTAL",
    "",
    "",
    "m²",
    "",
    "",
    f"{total_bruto:.2f}",
    f"{total_descuentos:.2f}",
    f"{total_muros:.2f}"
])


csv_data = csv_buffer.getvalue()


# ============================================================
# BOTÓN DE DESCARGA
# ============================================================

col_exp1, col_exp2 = st.columns(2)

with col_exp1:

    st.download_button(
        label="⬇ Descargar catálogo",
        data=csv_data,
        file_name="TRAZA_Catalogo_Cuantificacion.csv",
        mime="text/csv",
        use_container_width=True
    )


with col_exp2:

    st.download_button(
        label="⬇ Descargar cuadro de muros",
        data=csv_data,
        file_name="TRAZA_Cuadro_de_Muros.csv",
        mime="text/csv",
        use_container_width=True
    )

# ============================================================
# INFORMACIÓN DEL ARCHIVO
# ============================================================

st.markdown(
    """
<div class="tarjeta">
<div class="seccion-mini">ARCHIVO GENERADO</div>

<div style="font-size:18px; font-weight:600; margin-top:10px;">
TRAZA_Catalogo_Cuantificacion.csv
</div>

<div style="color:#70766E; margin-top:18px; line-height:1.6;">
Incluye tipo de muro, concepto, dimensiones,
área bruta, descuentos por vanos y área neta.
</div>

</div>
""",
    unsafe_allow_html=True
)
