#!/bin/bash

# Define the units and subtopics with corresponding filenames
declare -A units
units[Unit1]="1_1_history 1_2_universe_origins 1_3_tools_techniques 1_4_numbers 1_5_light_travel"
units[Unit2]="2_1_newtons_laws 2_2_keplers_laws 2_3_gravitational_forces 2_4_ancient_astronomy 2_5_astrology_vs_astronomy"
units[Unit3]="3_1_nature_of_light 3_2_spectroscopy 3_3_applications 3_4_electromagnetic_spectrum 3_5_spectral_lines"
units[Unit4]="4_1_solar_system_formation 4_2_the_sun 4_3_planets_moons 4_4_dating_surfaces 4_5_solar_system_origin"
units[Unit5]="5_1_star_formation 5_2_stellar_classification 5_3_stellar_evolution 5_4_atom_structure 5_5_doppler_effect"
units[Unit6]="6_1_galaxy_types 6_2_cosmology 6_3_universe_future 6_4_expanding_universe 6_5_dark_matter_energy"
units[Unit7]="7_1_conditions_for_life 7_2_seti 7_3_astrobiology 7_4_cosmic_context 7_5_seti"

# Create HTML files from Jupyter notebooks
for unit in "${!units[@]}"; do
  for file in ${units[$unit]}; do
    jupyter nbconvert --to html "./notebooks/${file}.ipynb" --output-dir="./${unit}"
  done
done

echo "HTML files created successfully."
