---
layout: embed_default
---

# 4.2 Blackbody Radiation

The color and intensity of a star’s light aren’t just beautiful to behold—they are cosmic clues, revealing the star’s temperature, energy output, and even its life cycle. This fascinating story of light is explained by **blackbody radiation**—a key concept in astrophysics that helps us decode the mysteries of the universe.

Blackbody radiation allows astronomers to measure the temperature of distant stars, understand their energy distribution, and classify them. In this lesson, we will uncover the secrets of this phenomenon and explore how the light from stars guides us to a deeper understanding of the cosmos.

<div class="alert alert-block alert-success">
  <h4>Video</h4>
  <p>Watch <a href="https://www.youtube.com/watch?v=XdXAdwb7loE" target="_blank">this video</a> for an explanation of blackbody radiation and Wien's Law.</p>
</div>

---

## The Blackbody Spectrum

At the heart of blackbody radiation is the concept of a **blackbody**—an idealized object that perfectly absorbs all the radiation that falls on it and re-emits it based purely on its temperature. This re-emitted radiation forms a characteristic curve known as the **blackbody spectrum**.

<img src="https://raw.githubusercontent.com/teaghan/astronomy-12/main/Unit4/figures/blackbody_spectrum.png" alt="Blackbody Spectrum" width="1000" style="display: block; margin-left: auto; margin-right: auto;">

The blackbody spectrum is a graph that shows how the intensity of radiation emitted by an object varies across different wavelengths. There are several key features of this graph that provide valuable insights into the nature of the object emitting the radiation:

1. **Wavelength (x-axis):** The horizontal axis represents the wavelength of the emitted radiation, typically measured in nanometers (nm) or micrometers (µm). As you move from left to right on the graph, the wavelength increases. Shorter wavelengths correspond to higher energy radiation, such as ultraviolet and visible light, while longer wavelengths correspond to lower energy radiation, such as infrared.

2. **Intensity (y-axis):** The vertical axis represents the intensity or amount of radiation emitted at each wavelength. The height of the curve at a particular wavelength shows how much energy is being radiated at that wavelength. The higher the peak, the more radiation is emitted at that wavelength.

3. **The Peak of the Curve:** The peak of the blackbody spectrum indicates the wavelength at which the object emits the most radiation. Hotter objects have their peaks at shorter wavelengths (bluer light), while cooler objects have their peaks at longer wavelengths (redder light). This relationship is governed by **Wien's Displacement Law**, which links temperature to the peak wavelength.

4. **The Shape of the Curve:** The shape of the blackbody curve rises steeply on the shorter wavelength side (left) and falls off more gradually on the longer wavelength side (right). This shape tells us how energy is distributed across different wavelengths, with hotter objects concentrating more energy in shorter wavelengths.

5. **Area Under the Curve:** The total area under the blackbody curve represents the **total energy emitted by the object** across all wavelengths. This area is directly related to the object's temperature and is described by the **Stefan-Boltzmann Law**. Hotter objects emit more total energy, which results in a larger area under the curve. This explains why hotter stars are more luminous than cooler ones.

> **Interactive Exploration:** Curious to see how temperature changes affect the blackbody spectrum? Use the simulator below to experiment with different temperatures and observe how the peak wavelength, total intensity, and area under the curve change. This hands-on experience will help you understand why hot objects glow blue while cooler ones appear red.

<div style="width: 100%; height: 0; padding-bottom: 75%; position: relative;">
    <iframe src="https://phet.colorado.edu/sims/html/blackbody-spectrum/latest/blackbody-spectrum_en.html" 
            style="position: absolute; width: 100%; height: 100%; top: 0; left: 0;" 
            allowfullscreen>
    </iframe>
</div>

---

## Wien’s Displacement Law

Have you ever noticed how some stars twinkle red in the night sky, while others gleam blue or white? This dazzling array of colors isn’t just for show—it’s a direct result of **Wien’s Displacement Law**, a powerful tool that helps astronomers determine the temperature of stars based on the color of their light.

**Wien’s Displacement Law** describes the relationship between the temperature of a blackbody and the wavelength at which it emits the most radiation. Essentially, it tells us that hotter objects radiate more at shorter wavelengths (toward the blue end of the spectrum), while cooler objects radiate more at longer wavelengths (toward the red end of the spectrum). Mathematically, this relationship is expressed as:

> $$ \lambda_{\text{max}} = \frac{b}{T} $$

where:
- $\lambda_{\text{max}}$ is the wavelength of maximum emission,
- $T$ is the temperature in Kelvin,
- $b$ is Wien’s constant, approximately $2.898 \times 10^{-3} \, \text{m} \cdot \text{K}$.

What does this mean for stars? 

- **Cooler stars**, like red dwarfs, have their peak emission in the red part of the spectrum, which is why they glow with a reddish hue.
- **Hotter stars**, like blue giants, emit more light at shorter wavelengths, making them appear blue or white.

Wien’s Displacement Law provides a cosmic thermometer, letting us gauge the temperature of stars billions of kilometers away simply by observing their light.

<div class="alert alert-block alert-warning">
  <h4>Example</h4>
  <p>If a star has a surface temperature of 5800 K (similar to the Sun), the peak wavelength of its radiation can be calculated as:</p>
</div>

> $$ \lambda_{\text{max}} = \frac{2.898 \times 10^{-3} \, \text{m} \cdot \text{K}}{5800 \, \text{K}} \approx 500 \, \text{nm} $$
>
> This wavelength is in the visible light range, explaining why the Sun appears white or yellowish to our eyes.

<div class="alert alert-block alert-info">
<h4>Stellar Age and Colour</h4>
The color of a star can also tell us about its stage in the stellar life cycle. Hot, young stars tend to be blue or white, while older, cooler stars often appear red as they near the end of their life cycle.
</div>

---

## Stefan-Boltzmann Law

Have you ever wondered why some stars shine brighter than others, even though they might be cooler? The secret lies in the **Stefan-Boltzmann Law**, a powerful relationship between the temperature of a star and the total energy it radiates.

The Stefan-Boltzmann Law tells us that the energy radiated per unit surface area by a blackbody increases dramatically with temperature—specifically, with the **fourth power** of the temperature! This means that even a small increase in a star’s temperature results in a massive increase in the energy it emits. The law is expressed mathematically as:

> $$ F = \sigma T^4 $$

where:
- $F$ is the energy radiated per unit area,
- $T$ is the temperature in Kelvin,
- $\sigma$ is the Stefan-Boltzmann constant, approximately $5.67 \times 10^{-8} \, \text{W/m}^2 \cdot \text{K}^4$.

What does this mean for stars? Consider this: if one star is twice as hot as another, it doesn’t just emit twice the energy—it emits **16 times** more energy per unit area! This is because the energy output scales with $T^4$, meaning that small differences in temperature can lead to enormous differences in brightness.

But temperature isn't the only factor at play. The **luminosity** of a star, which is the total energy it emits, also depends on the star’s surface area. Large stars like red giants, even though they might be cooler, can shine just as brightly as smaller, hotter stars because they have much more surface area over which to radiate their energy.

The Stefan-Boltzmann Law gives us a deeper understanding of how stars of different sizes and temperatures contribute to the dazzling array of brightness we see in the night sky.

<div class="alert alert-block alert-info">
<h4>Size, Temperature, and Luminosity</h4>
The Stefan-Boltzmann Law explains why a cool red giant can appear just as luminous as a small, blazing-hot blue star. Size and temperature both play crucial roles in determining a star’s brightness.
</div>

---

## Color Indices and Stellar Classification

Imagine walking through the cosmos, guided only by the color of the stars. Their colors aren’t just a visual treat—they are cosmic signposts that tell us about a star’s temperature, age, and even its future. This information is vital for astronomers, who classify stars based on their color using a system known as **color indices**.

Remember when you first encountered the **Hertzsprung-Russell (HR) diagram**? You learned how stars are categorized based on their luminosity and temperature. The color index is a similar concept that connects the star’s color to its temperature, allowing astronomers to classify stars into different spectral types.

The **color index** is a numerical value obtained by measuring a star’s brightness through different filters, usually comparing the amount of light in the **blue** and **red** parts of the spectrum. This measurement provides a quick and powerful way to determine a star’s temperature:
- **Hot stars** (like O-type stars) emit more blue light than red, resulting in a **negative color index** and giving them their characteristic blue appearance.
- **Cool stars** (like M-type stars) emit more red light than blue, resulting in a **positive color index** and making them appear red.

These spectral classifications (O, B, A, F, G, K, M) provide a systematic way to categorize stars based on their temperature:
- **O-type stars**: These are the hottest and most massive stars, glowing with a brilliant blue hue and burning through their nuclear fuel at an extraordinary rate.
- **M-type stars**: At the other end of the spectrum, M-type stars are the coolest and smallest, often appearing red due to their lower temperature.

<div class="alert alert-block alert-info">
<h4>The Sun</h4>
Our Sun is a G-type star, meaning it has a moderate surface temperature of about 5,800 K. This places it between the hottest blue stars and the coolest red ones, giving it a warm yellowish-white color.
</div>

The **color index** is more than just a temperature gauge—it plays a crucial role in understanding **stellar evolution**. By knowing a star's color and classification, astronomers can predict its life cycle, from its formation in a molecular cloud to its eventual death as a white dwarf, neutron star, or black hole. 

These color classifications, combined with the HR diagram, give astronomers a powerful toolkit for charting the life stories of stars. Every star in the night sky has a tale to tell, and its color is the key to unlocking its secrets.

---

## Check Your Understanding

1. Why does the peak wavelength of radiation emitted by a star shift towards shorter wavelengths as the star’s temperature increases?
2. A star has a surface temperature of $3000 \, \text{K}$. Calculate its peak emission wavelength using Wien’s Displacement Law.
3. If the emitted radiation from a red dwarf star has a wavelength of maximum
power at 1200 nm, what is the temperature of this star, assuming it is a blackbody?
4. If a star emits $1.42 \times 10^6 \, \text{W/m}^2$ of energy, what is its surface temperature?

---

## Resources

- Astronomy (2016). Andrew Fraknoi, David Morrison, and Sidney C. Wolff.

# 4.2 Blackbody Radiation

- **Planck’s Law and Spectrum**: Description of the spectrum of radiation emitted by a blackbody.
- **Wien’s Displacement Law**: Relating temperature to the peak wavelength of blackbody radiation.
- **Stefan-Boltzmann Law**: Explaining the total energy radiated per unit surface area in relation to temperature.
- **Color Indices and Stellar Classification**: Overview of how color indices help classify stars based on temperature and color.

<iframe src="https://phet.colorado.edu/sims/html/blackbody-spectrum/latest/blackbody-spectrum_en.html"
        width="800"
        height="600"
        allowfullscreen>
</iframe>

video: https://www.youtube.com/watch?v=XdXAdwb7loE

EXAMPLE 5.3

EXAMPLE 5.4
