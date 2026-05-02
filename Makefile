.PHONY: all clean install validate

# Default target — regenerate everything
all: data/kpi_comparison_matrix.csv data/kpi_comparison_matrix.xlsx

# Regenerate CSV + XLSX from the canonical Python source of truth
data/kpi_comparison_matrix.csv data/kpi_comparison_matrix.xlsx: kpi_definitions.py build_matrix.py
	python build_matrix.py

# Install Python dependencies
install:
	pip install --user openpyxl pandas

# Sanity-check the source of truth
validate:
	python kpi_definitions.py

# Remove generated artefacts (sources are kept)
clean:
	rm -f data/kpi_comparison_matrix.csv
	rm -f data/kpi_comparison_matrix.xlsx
	rm -f data/kpi_comparison_matrix.pdf
	rm -f data/kpi_matrix_README.pdf
	rm -f data/preview*.jpg data/readme*.jpg

# Print a summary of what is in the matrix
summary:
	@python -c "from kpi_definitions import KPIS, kpis_by_tier; \
		print(f'Total KPIs: {len(KPIS)}'); \
		print(f'  CORE:        {len(kpis_by_tier(\"CORE\"))}'); \
		print(f'  EXTENSION:   {len(kpis_by_tier(\"EXTENSION\"))}'); \
		print(f'  EXPLORATORY: {len(kpis_by_tier(\"EXPLORATORY\"))}')"
