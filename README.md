# KPI Comparison Matrix v1.0

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19964373.svg)](https://doi.org/10.5281/zenodo.19964373)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## Indicadores de resiliencia climática edilicia para climas áridos sudamericanos

**Autor:** Dr. Arq. Gustavo Javier Barea Paci
**Afiliación:** Instituto de Ambiente, Hábitat y Energía (INAHE) — CONICET Mendoza
**Contacto:** gbarea@mendoza-conicet.gob.ar
**Repositorio:** https://github.com/gbarea-INAHE/kpi-comparison-matrix
**DOI:** [10.5281/zenodo.19964373](https://doi.org/10.5281/zenodo.19964373)
**Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Versión:** 1.0
**Librería compañera:** `aridkpi` (Python) — *próximamente*

---

## 1. Resumen

Este dataset documenta de manera comparable y reproducible 17 indicadores de desempeño termo-energético (KPIs) relevantes para la evaluación de resiliencia climática de viviendas unifamiliares en climas áridos y semi-áridos sudamericanos (BWk, BSk de la clasificación Köppen-Geiger). Para cada indicador se documentan: fórmula formal, dominio, supuestos críticos, limitaciones específicas en el régimen árido sudamericano, justificación de la extensión regional propuesta, y referencias bibliográficas verificadas. Los KPIs se organizan jerárquicamente en tres niveles —núcleo, extensión y exploratorio— que reflejan distintos grados de prioridad operativa dentro del Plan de Trabajo 2026–2029 alineado con el IEA EBC Annex 80.

El dataset se publica como insumo abierto reutilizable por la comunidad regional e internacional de investigación en desempeño edilicio bajo cambio climático. Constituye la base teórica formal sobre la que se construye la librería Python `aridkpi` (próximo entregable del Sprint 2).

---

## 2. Motivación: por qué un dataset comparativo

El campo de la resiliencia edilicia bajo cambio climático ha experimentado una proliferación rápida de indicadores en los últimos cinco años. Carlucci et al. (2021) documentaron en su revisión sobre 95 documentos normativos que la dispersión metodológica del campo dificulta sustancialmente la comparabilidad entre estudios: el mismo indicador se calcula con fórmulas, supuestos y umbrales distintos según la fuente. Wei, Jiang, Pandey, Liu, Li, O'Neill, Dong y Hamdy (2025) y Borraccino, Losito, Campagna, Carlucci y Fiorito (2026) —las dos revisiones internacionales más recientes— identifican esta dispersión como uno de los desafíos abiertos del campo.

A esta dispersión metodológica se suma un segundo problema, específico de nuestra región: los indicadores consolidados por el IEA EBC Annex 80 (Holzer, Attia, Levinson et al., 2024) fueron calibrados sobre evidencia empírica europea y norteamericana, donde las olas de calor son típicamente húmedas y las amplitudes térmicas diarias son moderadas. En climas áridos sudamericanos —con amplitudes térmicas diarias superiores a 15 °C, humedad relativa media inferior al 40 % y radiación solar superior a 2200 kWh·m⁻²·año⁻¹ (Filippín, Ricard, Flores Larsen y Marek, 2022)— varios supuestos centrales de los indicadores Annex 80 se rompen.

Esta matriz comparativa cumple tres funciones simultáneas. Primero, documenta de manera explícita la fórmula, los supuestos y las limitaciones de cada indicador, permitiendo comparaciones rigurosas entre estudios. Segundo, identifica las limitaciones específicas en el régimen árido sudamericano y propone justificaciones técnicas para extensiones regionales. Tercero, organiza el sistema en tres niveles de prioridad operativa, evitando la sobre-ingeniería y orientando los esfuerzos del plan hacia un núcleo manejable de cinco indicadores comprometidos en todos los casos.

---

## 3. Estructura del sistema de KPIs

Los 17 indicadores se organizan en tres niveles jerárquicos:

### 3.1. Núcleo (CORE) — 5 indicadores

Calculados sobre el 100 % de los casos del plan 2026–2029. Forman el conjunto comprometido y reportable independientemente de demoras en otros componentes. Los cinco indicadores cubren las cuatro dimensiones críticas del desempeño bajo cambio climático: magnitud del sobrecalentamiento (IOD), resistividad al cambio climático (CCOR), habitabilidad ante cortes de energía (UDH), sensibilidad energética (ΔE/ΔT) y estabilidad dinámica (dT/dt máx).

| ID | Nombre | Dimensión |
|---|---|---|
| `IOD` | Indoor Overheating Degree | Magnitud agregada de sobrecalentamiento |
| `CCOR` | Climate Change Overheating Resistivity | Resiliencia frente al cambio climático |
| `UDH` | Unmet Degree Hours during outage | Habitabilidad ante corte de energía |
| `DEDT` | δE/δT — sensibilidad energética | Robustez de la demanda bajo trayectorias SSP |
| `DTDT_MAX` | dT/dt máx — tasa de cambio térmico interior | Dinámica intra-diaria |

### 3.2. Extensión (EXTENSION) — 7 indicadores

Calculados cuando la calidad de los datos lo permite (registros de monitoreo de mayor duración, modelos calibrados disponibles). Refuerzan los hallazgos del núcleo aportando dimensiones complementarias: la atenuación y el desfase térmico (efecto de la inercia), la pérdida de eficacia bajo SSP (degradación de estrategias pasivas), la robustez interescenario (incertidumbre intermodelo), entre otros.

### 3.3. Exploratorio (EXPLORATORY) — 5 indicadores

Calculados de forma oportunística cuando un paper o proyecto específico lo requiera y los datos estén disponibles. Incluyen indicadores de heat-stress (SET·h, HIHH) que requieren validación específica para clima árido, métricas dinámicas (persistencia de disconfort, estabilidad higrotérmica conjunta), y el índice compuesto ACRS (Arid Climate Resilience Score) ponderado por entropía de Shannon (Diakoulaki, Mavrotas y Papayannakis, 1995).

---

## 4. Limitaciones de los indicadores Annex 80 en BWk/BSk

La matriz documenta sistemáticamente las limitaciones identificadas para cada indicador del Annex 80 cuando se aplica a climas áridos sudamericanos. Sintetizamos aquí las cuatro más relevantes:

**Modelos de confort adaptativo no validados localmente.** Tanto IOD como HE dependen de un umbral de confort T_comf que en la formulación original se deriva del modelo adaptativo europeo (EN 16798-1) o norteamericano (ASHRAE 55). Estos modelos no han sido validados en climas BWk/BSk sudamericanos. Pérez-Fargallo et al. (2024) propusieron un modelo adaptativo para Chile pero su transferibilidad al resto del dominio regional aún no está establecida. La matriz recomienda reportar IOD y HE bajo múltiples modelos candidatos con análisis de sensibilidad cuando no haya validación local.

**Umbrales de Passive Survivability calibrados a Norteamérica.** UDH utiliza un umbral típico de 30 °C (refrigeración) calibrado en el contexto norteamericano (Sun, Zhang, Zeng, Levinson, Wei y Hong, 2021). La humedad relativa baja (frecuentemente inferior al 30 %) característica del régimen árido modifica sustancialmente la percepción térmica: a 30 °C dry-bulb con HR 20 %, la temperatura efectiva (SET) es significativamente menor que a 30 °C dry-bulb con HR 60 %. La matriz recomienda recalibrar el umbral usando SET, WBGT o UTCI cuando se reporte UDH en BWk/BSk.

**Linealidad implícita de la relación IOD-AWD.** El Building Climate Vulnerability Factor (IOD/AWD) presupone una relación monotónica entre forzamiento ambiental y respuesta interior. En climas BWk con amplitud diurna superior a 15 °C la ventilación nocturna puede romper esta linealidad: edificios con alta inercia y ventilación nocturna pueden mostrar IOD bajo aún con AWD alto. La matriz recomienda validar empíricamente la linealidad por tipología antes de reportar el cociente.

**Heat Index de Steadman inadecuado para climas secos.** HIHH (Heat Index Hazard Hours) se calcula con la fórmula de Steadman (1979), calibrada en climas húmedos de latitudes medias. En climas áridos subestima sistemáticamente el estrés térmico. La matriz lo clasifica como exploratorio y recomienda preferir UTCI o WBGT para reportes primarios en nuestro contexto.

---

## 5. Extensiones propuestas para el régimen árido

La matriz propone cuatro extensiones específicas que capturan fenómenos no representados adecuadamente por los indicadores Annex 80 existentes:

**Sensibilidad energética al cambio climático (δE/δT).** Pendiente de la regresión EUI vs. T_media bajo escenarios SSP × horizonte. Cuantifica la robustez de un edificio frente a trayectorias climáticas. Antecedente directo: Flores Larsen, Filippín y Barea (2019).

**Tasa máxima de cambio térmico interior (dT/dt máx).** Indicador empírico de dinámica intra-diaria. Captura la velocidad con que el edificio responde a forzamientos térmicos rápidos —fenómeno crítico en climas con amplitud > 15 °C donde ningún indicador Annex 80 lo refleja directamente.

**Pérdida de eficacia pasiva bajo SSP.** Δ(IOD_2080 − IOD_actual) por estrategia. Mide la degradación de una estrategia pasiva específica (p. ej. ventilación nocturna) bajo escenarios futuros. Ancla directa de la H3 del plan.

**Robustez interescenario.** Desviación estándar de IOD entre los GCMs del ensemble bajo SSP fijo. Cuantifica la dispersión intermodelo —dimensión crítica en regiones de alta altitud como los Andes donde la dispersión CMIP6 es mayor que en dominios planos (Almazroui, Ashfaq, Islam, Rashid, Kamil et al., 2021).

---

## 6. Cómo usar este dataset

**Lectura programática (Python).** El archivo `data/kpi_comparison_matrix.csv` puede leerse directamente con pandas:

```python
import pandas as pd
matrix = pd.read_csv("data/kpi_comparison_matrix.csv")
core_kpis = matrix[matrix["tier"] == "CORE"]
```

**Lectura humana.** El archivo `data/kpi_comparison_matrix.xlsx` contiene tres hojas: README, KPI matrix (la matriz formateada con código de color por tier), y Tier legend. Optimizado para impresión A3 horizontal.

**Integración con la librería compañera.** La librería Python `aridkpi` (Sprint 2, próximamente) implementará los 5 KPIs del núcleo siguiendo exactamente las fórmulas, supuestos y umbrales documentados aquí. Consistencia garantizada por tests unitarios automatizados que se ejecutan contra esta matriz.

---

## 7. Cómo citar

> Barea Paci, G. J. (2026). *KPI Comparison Matrix v1.0 — climate-resilience indicators for residential buildings in arid South American climates*. Zenodo. https://doi.org/10.5281/zenodo.19964373

BibTeX:

```bibtex
@dataset{barea_kpi_matrix_2026,
  author    = {Barea Paci, Gustavo Javier},
  title     = {KPI Comparison Matrix v1.0 — climate-resilience indicators
               for residential buildings in arid South American climates},
  year      = {2026},
  publisher = {Zenodo},
  version   = {1.0},
  doi       = {10.5281/zenodo.19964373},
  url       = {https://doi.org/10.5281/zenodo.19964373}
}
```

---

## 8. Versionado

Versiones futuras seguirán semantic versioning:

- **MAJOR** (2.0, 3.0…): cambio incompatible en la estructura del CSV (columnas eliminadas o renombradas; KPIs eliminados).
- **MINOR** (1.1, 1.2…): adición de nuevos KPIs o columnas sin romper los existentes.
- **PATCH** (1.0.1…): correcciones de fórmulas, referencias o redacción sin cambio estructural.

El changelog completo se mantiene en [`CHANGELOG.md`](CHANGELOG.md) del repositorio y cada release etiquetado en GitHub se sincroniza automáticamente con un nuevo DOI versionado en Zenodo. El **concept DOI** que apunta siempre a la versión más reciente es [10.5281/zenodo.19964372](https://doi.org/10.5281/zenodo.19964372).

---

## 9. Agradecimientos

Este dataset es el primer entregable del Plan de Trabajo 2026–2029 desarrollado en el INAHE-CONICET para la evaluación de resiliencia termo-energética de viviendas en climas áridos sudamericanos, alineado con el IEA EBC Annex 80. Alimenta los OE1 y OE2 del plan y se consume desde la librería Python `aridkpi`. El trabajo se beneficia de la línea de investigación construida en colaboración con C. Filippín (CONICET — La Pampa), S. Flores Larsen (CONICET — Salta), F. Bre y V. Fachinotti (CIMEC — Santa Fe), C. Ganem y M. V. Mercado (INAHE — Mendoza) y A. Esteves (INAHE — Mendoza), cuyas contribuciones individuales se citan en el campo `references` de cada KPI.

---

## 10. Referencias

Las referencias completas, en formato APA y con DOI verificado, están listadas en el campo `references` de cada KPI. Las fuentes principales son:

- **Annex 80 — IOD, AWD, CCOR, UDH:** Hamdy, Carlucci, Hoes y Hensen (2017); Rahif, Hamdy, Homaei et al. (2022); Sun, Zhang, Zeng, Levinson, Wei y Hong (2021); Holzer, Attia, Levinson et al. (2024).
- **Calibración bayesiana:** Kennedy y O'Hagan (2001); Chong y Menberg (2018); Coakley, Raftery y Keane (2014).
- **Surrogates y aprendizaje automático:** Westermann y Evins (2019, 2021); Bre, Roman y Fachinotti (2020).
- **Escenarios CMIP6:** Almazroui, Ashfaq, Islam, Rashid, Kamil et al. (2021); Belcher, Hacker y Powell (2005); Nik (2016); O'Neill et al. (2016).
- **Análisis de sensibilidad:** Tian (2013); Saltelli et al. (2010); Herman y Usher (2017).
- **Antecedentes regionales propios:** Flores Larsen, Filippín y Barea (2019); Barea Paci, Mercado, Filippín, Monteoliva y Villalba (2022); Barea Paci, Ganem, Molina y Mateo (2023); Cantón, Ganem, Barea y Fernández Llano (2014); Filippín, Ricard, Flores Larsen y Marek (2022).
- **Índices compuestos:** Diakoulaki, Mavrotas y Papayannakis (1995); OECD (2008).
- **Revisiones recientes:** Cruz, Mendes, Mendes, Caldas y Bastos (2024); Cruz, López-Guerrero, Mendes, Mendes, Caldas y Bastos (2025); Wei, Jiang, Pandey, Liu, Li, O'Neill, Dong y Hamdy (2025); Borraccino, Losito, Campagna, Carlucci y Fiorito (2026).

---

*Documento generado a partir de la fuente única de verdad `kpi_definitions.py`. Para reproducir CSV, XLSX y este documento, ejecutar `make all` desde el directorio raíz del repositorio.*
