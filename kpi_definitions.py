"""
KPI definitions for the arid resilience toolkit.
Single source of truth — used to generate CSV, XLSX, and Markdown documentation.
"""

# Each KPI is a dict with:
#   id, name, family, tier, formula, units, domain, source, assumptions,
#   limitations_in_BWk_BSk, regional_extension_rationale, references

KPIS = [
    # =====================================================================
    # TIER 1 — CORE (5 indicators, computed on 100% of cases)
    # =====================================================================
    {
        "id": "IOD",
        "name": "Indoor Overheating Degree",
        "family": "Annex 80 — Overheating magnitude",
        "tier": "CORE",
        "formula": "IOD = sum_z [ sum_t max(T_op,z(t) - T_comf,z(t), 0) * dt * occ_z(t) ] / sum_z [ sum_t occ_z(t) * dt ]",
        "units": "°C·h",
        "domain": "Magnitude of overheating, weighted by zone occupancy",
        "source": "Hamdy, Carlucci, Hoes & Hensen (2017)",
        "assumptions": "Single comfort threshold T_comf,z; occupancy schedule known per zone; positive part operator; sub-hourly time step dt",
        "limitations_in_BWk_BSk": "T_comf was calibrated on European temperate climates; underestimates intra-day variations characteristic of arid regions with diurnal range > 15 °C",
        "regional_extension_rationale": "T_comf must be derived from a locally validated adaptive comfort model rather than a fixed European threshold",
        "references": "Hamdy et al. (2017) Building and Environment 122; ASHRAE 55-2020; EN 16798-1:2019",
    },
    {
        "id": "CCOR",
        "name": "Climate Change Overheating Resistivity",
        "family": "Annex 80 — Resilience to climate change",
        "tier": "CORE",
        "formula": "CCOR = (IOD_baseline - IOD_strategy) / Delta_T_climate",
        "units": "°C·h / °C",
        "domain": "Effectiveness of a passive strategy under climate-change-driven temperature shifts",
        "source": "Rahif, Hamdy, Homaei et al. (2022)",
        "assumptions": "A baseline strategy is defined; Delta_T_climate is the projected mean annual temperature increase under the SSP scenario considered",
        "limitations_in_BWk_BSk": "Requires a locally meaningful baseline; importing a European baseline produces non-comparable results",
        "regional_extension_rationale": "Baseline defined as IRAM 11605 Level B (current Argentine residential standard); Delta_T_climate computed from CMIP6 multi-GCM ensemble for the specific city",
        "references": "Rahif et al. (2022) Building and Environment 208, 108599; IEA EBC Annex 80 (Holzer et al., 2024)",
    },
    {
        "id": "UDH",
        "name": "Unmet Degree Hours during power outage (Passive Survivability)",
        "family": "Annex 80 — Passive survivability",
        "tier": "CORE",
        "formula": "UDH_w = sum_t in W max(T_op(t) - T_threshold, 0) * dt , for window W in {24h, 72h, 7d}",
        "units": "°C·h",
        "domain": "Habitability during a sustained power outage triggered during an extreme weather event (EWY)",
        "source": "Sun, Zhang, Zeng, Levinson, Wei & Hong (2021)",
        "assumptions": "T_threshold = 30 °C (cooling) or 26 °C (more conservative); HVAC unavailable during W; outage triggered at the EWY peak",
        "limitations_in_BWk_BSk": "Threshold 30 °C calibrated to North American climates; low RH typical of arid regions modifies thermal perception (effective temperature differs from dry-bulb)",
        "regional_extension_rationale": "Threshold to be recalibrated using SET (Standard Effective Temperature) for low RH conditions, or alternatively WBGT/UTCI",
        "references": "Sun et al. (2021) Energy and Buildings 252, 111383; Levinson et al. (2019); ANSI/ASHRAE 55-2020",
    },
    {
        "id": "DEDT",
        "name": "Energy sensitivity to climate (delta E / delta T)",
        "family": "Sensitivity",
        "tier": "CORE",
        "formula": "delta_E / delta_T = slope of regression EUI ~ T_mean across SSP scenarios and time horizons",
        "units": "kWh·m^-2·yr^-1 / °C",
        "domain": "Robustness of building energy performance under climate-warming trajectories",
        "source": "Proposed in this work, building on Flores Larsen, Filippín & Barea (2019)",
        "assumptions": "Linearity of EUI vs T_mean within the SSP × horizon range considered; identical occupancy and HVAC schedules across scenarios",
        "limitations_in_BWk_BSk": "Linearity must be tested empirically; in highly insulated envelopes the response can be non-linear",
        "regional_extension_rationale": "Captures degradation of bioclimatic strategies under climate change; particularly relevant in arid regions where cooling demand is projected to rise sharply",
        "references": "Flores Larsen, Filippín & Barea (2019) Energy and Buildings 184; Hamdy et al. (2017)",
    },
    {
        "id": "DTDT_MAX",
        "name": "Maximum indoor thermal change rate (dT/dt max)",
        "family": "Hygrothermal stability",
        "tier": "CORE",
        "formula": "max_t | dT_in(t)/dt |  computed over the cooling season",
        "units": "°C/h",
        "domain": "Intra-day dynamic stability of indoor temperature; captures the speed of thermal transients",
        "source": "Proposed in this work",
        "assumptions": "Time series at 10-min resolution or finer; smoothed by a 3-point moving average to reduce sensor noise",
        "limitations_in_BWk_BSk": "None specific; this indicator is itself an extension specifically motivated by BWk/BSk dynamics",
        "regional_extension_rationale": "Conventional aggregated indicators (EUI, HDD/CDD, discomfort hours) are insensitive to intra-day dynamics. In arid climates with diurnal range > 15 °C, dT/dt is a primary discriminator of envelope thermal mass",
        "references": "Cantón, Ganem, Barea & Fernández Llano (2014) Renewable Energy 69; Flores-Larsen, Filippín & Bre (2023) Building and Environment 230",
    },
    # =====================================================================
    # TIER 2 — EXTENSION (computed when data permits)
    # =====================================================================
    {
        "id": "AWD",
        "name": "Ambient Warmness Degree",
        "family": "Annex 80 — Climate forcing",
        "tier": "EXTENSION",
        "formula": "AWD = sum_t max(T_ext(t) - T_b, 0) * dt   (with T_b = 18 °C in the original Annex 80 definition for summer)",
        "units": "°C·h",
        "domain": "Climate-side warming forcing on the building, normalised by base temperature",
        "source": "Hamdy, Carlucci, Hoes & Hensen (2017)",
        "assumptions": "T_b = 18 °C; integration over the cooling season",
        "limitations_in_BWk_BSk": "T_b derived from temperate-climate methodologies; in arid hot climates (e.g. summer Mendoza) T_b should be higher to avoid saturation",
        "regional_extension_rationale": "T_b regional candidate: 22-24 °C for BWk summer based on local thermal autonomy curves and adaptive comfort models",
        "references": "Hamdy et al. (2017) Building and Environment 122; CIBSE TM52/TM59",
    },
    {
        "id": "AIOD_AWD",
        "name": "Building Climate Vulnerability Factor",
        "family": "Annex 80 — Vulnerability ratio",
        "tier": "EXTENSION",
        "formula": "BCVF = IOD / AWD",
        "units": "dimensionless",
        "domain": "Ratio of indoor overheating to ambient warming forcing; measures intrinsic vulnerability of the building",
        "source": "Hamdy, Carlucci, Hoes & Hensen (2017)",
        "assumptions": "Linearity of the IOD-AWD relationship; both indicators computed over the same period",
        "limitations_in_BWk_BSk": "Linearity assumption may break in BWk where high diurnal amplitude allows night cooling; BCVF in arid climates may show non-monotonic behaviour",
        "regional_extension_rationale": "Validate linearity empirically per typology; if non-linear, report the IOD-AWD scatter and the regression residual structure",
        "references": "Hamdy et al. (2017); Attia, Levinson, Ndongo et al. (2021) Energy and Buildings 239",
    },
    {
        "id": "HE_ADAPTIVE",
        "name": "Hours of Exceedance over adaptive comfort",
        "family": "Annex 80 — Adaptive comfort",
        "tier": "EXTENSION",
        "formula": "HE = #{ t : T_op(t) > T_comf,adapt(t) and t is occupied }",
        "units": "hours",
        "domain": "Frequency of exceedance over an adaptive comfort threshold",
        "source": "EN 16798-1:2019; CIBSE TM52/TM59",
        "assumptions": "Adaptive comfort model valid for the climate; occupancy schedule known",
        "limitations_in_BWk_BSk": "European adaptive comfort models have not been validated for arid South American climates",
        "regional_extension_rationale": "Use adaptive comfort models locally validated when available (Pérez-Fargallo et al., 2024 for Chile); otherwise report HE under multiple candidate models with sensitivity analysis",
        "references": "EN 16798-1:2019; CIBSE TM52, TM59; Pérez-Fargallo et al. (2024)",
    },
    {
        "id": "ATTENUATION",
        "name": "Indoor/outdoor thermal attenuation",
        "family": "Passive performance",
        "tier": "EXTENSION",
        "formula": "Atten = ( max(T_in,daily) - min(T_in,daily) ) / ( max(T_ext,daily) - min(T_ext,daily) )",
        "units": "dimensionless (0 = perfect attenuation, 1 = no attenuation)",
        "domain": "Thermal mass effect on damping outdoor amplitude",
        "source": "ISO 13786:2017",
        "assumptions": "Daily amplitudes; cooling season; HVAC off or in free-running mode",
        "limitations_in_BWk_BSk": "None specific; ISO 13786 is climate-agnostic",
        "regional_extension_rationale": "Critical in BWk where outdoor diurnal range frequently exceeds 15 °C; discriminates effectively between adobe (high mass) and lightweight industrialised typologies",
        "references": "ISO 13786:2017 — Thermal performance of building components — Dynamic thermal characteristics; Cantón, Ganem, Barea & Fernández Llano (2014) Renewable Energy 69",
    },
    {
        "id": "PHASE_LAG",
        "name": "Thermal phase lag (time shift between outdoor and indoor peaks)",
        "family": "Passive performance",
        "tier": "EXTENSION",
        "formula": "phi = t_peak,indoor - t_peak,outdoor   (median over the cooling season)",
        "units": "hours",
        "domain": "Time delay introduced by envelope thermal mass; complements attenuation",
        "source": "ISO 13786:2017; Shaviv, Yezioro & Capeluto (2001)",
        "assumptions": "Daily peak detection robust to noise (use smoothed series); free-running mode preferred for evaluation",
        "limitations_in_BWk_BSk": "None specific; well-suited to BWk which presents strong diurnal cycles",
        "regional_extension_rationale": "Strategy of central importance in arid climates: a phase lag of 8-12 h shifts the peak indoor temperature to the cool dawn hours, enabling effective night ventilation",
        "references": "ISO 13786:2017; Shaviv, Yezioro & Capeluto (2001) Energy and Buildings 33; Filippín, Ricard, Flores Larsen & Marek (2022) Energy and Buildings 273",
    },
    {
        "id": "PASSIVE_LOSS_SSP",
        "name": "Passive strategy loss under SSP scenario",
        "family": "Resilience",
        "tier": "EXTENSION",
        "formula": "Loss_SSP = IOD_strategy(2080, SSP) - IOD_strategy(actual)",
        "units": "°C·h",
        "domain": "Degradation of a passive strategy under future climate scenarios",
        "source": "Proposed in this work, building on Moazami, Nik, Carlucci & Geving (2019)",
        "assumptions": "Same building model; same occupancy schedule; only the EPW file changes between actual and 2080 horizon",
        "limitations_in_BWk_BSk": "None specific",
        "regional_extension_rationale": "Anchors hypothesis H3 of the plan: passive strategies in BWk lose less effectiveness than in temperate European climates",
        "references": "Moazami et al. (2019) Building and Environment 162; Nik (2016) Applied Energy 177",
    },
    {
        "id": "INTER_SCENARIO_ROBUSTNESS",
        "name": "Inter-scenario robustness",
        "family": "Resilience",
        "tier": "EXTENSION",
        "formula": "R = std_{m in M} ( IOD_m )   for ensemble M of GCMs under fixed SSP and horizon",
        "units": "°C·h",
        "domain": "Inter-model dispersion of building performance across the GCM ensemble",
        "source": "Proposed in this work, following Nik (2016) and Almazroui et al. (2021)",
        "assumptions": "GCM ensemble with at least 8 members; equal weighting (or entropy-weighted variant)",
        "limitations_in_BWk_BSk": "Inter-model dispersion is itself larger over the Andes than over flat domains, so this indicator is essential — not optional — in our region",
        "regional_extension_rationale": "Quantifies the climate uncertainty propagated into the building outcome; reporting only the ensemble mean hides the spread",
        "references": "Nik (2016) Applied Energy 177; Almazroui et al. (2021) Earth Systems and Environment 5(2)",
    },
    # =====================================================================
    # TIER 3 — EXPLORATORY (computed opportunistically)
    # =====================================================================
    {
        "id": "SET_HOURS",
        "name": "SET-weighted exceedance hours",
        "family": "Annex 80 — Heat-stress weighted",
        "tier": "EXPLORATORY",
        "formula": "SET·h = sum_t max(SET(t) - 30, 0) * dt",
        "units": "°C·h",
        "domain": "Heat stress weighted by Standard Effective Temperature",
        "source": "Sun et al. (2021); ANSI/ASHRAE 55-2020",
        "assumptions": "SET model assumes moderate-to-high relative humidity",
        "limitations_in_BWk_BSk": "Very low RH (sometimes <20%) characteristic of the arid regime falls outside the validation envelope of the SET model",
        "regional_extension_rationale": "Compare against UTCI or WBGT; report all three, document which is most consistent with measured discomfort surveys",
        "references": "Sun et al. (2021); ANSI/ASHRAE 55-2020; Gagge, Fobelets & Berglund (1986)",
    },
    {
        "id": "HIHH",
        "name": "Heat Index Hazard Hours",
        "family": "Heat-stress",
        "tier": "EXPLORATORY",
        "formula": "HIHH = #{ t : HI(T, RH) > HI_threshold }",
        "units": "hours",
        "domain": "Heat stress as Steadman Heat Index exceedance",
        "source": "Steadman (1979); Tao, Sahin, Akbari et al. (2024)",
        "assumptions": "Steadman model calibrated on humid mid-latitude climates",
        "limitations_in_BWk_BSk": "Underestimates heat stress in dry climates; not recommended as primary indicator. Prefer UTCI or WBGT in our region",
        "regional_extension_rationale": "Reported only for cross-comparability with international literature; flagged as potentially misleading in BWk",
        "references": "Steadman (1979) J. Applied Meteorology 18; Tao et al. (2024) Energy and Buildings 307",
    },
    {
        "id": "DISCOMFORT_PERSIST",
        "name": "Discomfort persistence",
        "family": "Hygrothermal stability",
        "tier": "EXPLORATORY",
        "formula": "P = mean duration (h) of consecutive runs where T_op > T_comf",
        "units": "hours",
        "domain": "Severity of discomfort beyond simple counting of exceedance hours",
        "source": "Proposed in this work",
        "assumptions": "Run-length encoding on the binary series 1{T_op > T_comf}",
        "limitations_in_BWk_BSk": "None specific; run lengths in arid climates tend to be shorter than in humid climates due to nocturnal cooling, so this indicator captures regime differences",
        "regional_extension_rationale": "Two buildings with the same exceedance hour count can have very different occupant impact: a cluster of 8 consecutive uncomfortable hours is worse than 8 isolated hours",
        "references": "Carlucci & Pagliano (2012) Building and Environment 53",
    },
    {
        "id": "HYGRO_STABILITY",
        "name": "Joint T-RH-dewpoint stability score",
        "family": "Hygrothermal stability",
        "tier": "EXPLORATORY",
        "formula": "S = std(T_in) + alpha*std(RH_in) + beta*std(Td_in)   with alpha and beta to be calibrated",
        "units": "dimensionless (composite)",
        "domain": "Joint stability of indoor T, RH and dewpoint over a defined period",
        "source": "Proposed in this work",
        "assumptions": "alpha and beta to be calibrated against occupant comfort surveys; provisional alpha = beta = 1",
        "limitations_in_BWk_BSk": "Coefficients require local calibration",
        "regional_extension_rationale": "In arid climates condensation risk is low but moisture variability still matters for material durability and respiratory comfort",
        "references": "ASHRAE Standard 160-2016 — Criteria for Moisture-Control Design Analysis in Buildings",
    },
    {
        "id": "ACRS",
        "name": "Arid Climate Resilience Score (composite)",
        "family": "Composite",
        "tier": "EXPLORATORY",
        "formula": "ACRS = sum_j w_j * normalised_KPI_j   with weights w_j from Shannon entropy weighting (Diakoulaki et al., 1995)",
        "units": "dimensionless (0-100 scale after normalisation)",
        "domain": "Single-number summary score over the 5 core KPIs",
        "source": "Proposed in this work, building on Diakoulaki, Mavrotas & Papayannakis (1995)",
        "assumptions": "Min-max normalisation per KPI before weighting; PCA used as sensitivity check on weights (OECD, 2008)",
        "limitations_in_BWk_BSk": "A composite score always loses information; ACRS must be reported alongside the individual core KPIs, never replacing them",
        "regional_extension_rationale": "Useful for institutional audiences (IRAM, INTI, IPV) requiring a single score; entropy weighting avoids subjective weighting and is reproducible",
        "references": "Diakoulaki, Mavrotas & Papayannakis (1995) Computers & Operations Research 22; OECD (2008) Handbook on constructing composite indicators",
    },
]


def get_kpi_by_id(kpi_id):
    """Return the KPI dict matching the given id."""
    for kpi in KPIS:
        if kpi["id"] == kpi_id:
            return kpi
    raise KeyError(f"Unknown KPI id: {kpi_id}")


def kpis_by_tier(tier):
    """Return all KPIs of a given tier ('CORE', 'EXTENSION', 'EXPLORATORY')."""
    return [k for k in KPIS if k["tier"] == tier]


if __name__ == "__main__":
    # Quick sanity check
    assert len(KPIS) == 17, f"Expected 17 KPIs, got {len(KPIS)}"
    assert len(kpis_by_tier("CORE")) == 5
    assert len(kpis_by_tier("EXTENSION")) == 7
    assert len(kpis_by_tier("EXPLORATORY")) == 5
    print(f"OK — {len(KPIS)} KPIs defined ({len(kpis_by_tier('CORE'))} core, "
          f"{len(kpis_by_tier('EXTENSION'))} extension, "
          f"{len(kpis_by_tier('EXPLORATORY'))} exploratory)")
