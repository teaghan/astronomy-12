# Unit 1 Solutions 

This notebook contains solutions and calculations for all relevant derivations, examples and Check Your Understanding problems for this unit.

# 1.2 The Scale of the Univers

> **Derivation of a Light Year**:
> Light travels at a speed of approximately 299,792 kilometers per second (km/s) in a vacuum.
> There are 60 seconds in a minute, 60 minutes in an hour, and 24 hours in a day.
>
> $$ \text{Speed of light} = 299,792 \, \text{km/s} $$
>
> $$ \text{Seconds in a minute} = 60 $$
>
> $$ \text{Minutes in an hour} = 60 $$
>
> $$ \text{Hours in a day} = 24 $$
>
> $$ \text{Days in a year} = 365.25 $$
>
> To find the distance light travels in one year:
>
> $$ \text{Distance} = \text{Speed} \times \text{Time} $$
>
> First, calculate the number of seconds in a year:
>
> $$ 60 \times 60 \times 24 \times 365.25 \approx 31,557,600 \, \text{seconds/year} $$
>
> Then, multiply the speed of light by the number of seconds in a year:
>
> $$ 299,792 \, \text{km/s} \times 31,557,600 \, \text{s/year} \approx 9.46 \times 10^{12} \, \text{kilometers/year} $$
>
> Therefore, one light-year is approximately 9.46 trillion kilometers.


<div class="alert alert-block alert-warning">
<b>Example:</b> Calculate the distance to a star with a parallax angle of 0.1 arcseconds. 
</div>

> Using the formula: 
>
> $$ \text{Distance (parsecs)} = \frac{1}{\text{parallax (arcseconds)}} $$
> $$ \text{Distance} = \frac{1}{0.1} = 10 \text{ parsecs} $$
>
> To convert parsecs to light-years, use the conversion factor: 
> $$ 1 \text{ parsec} = 3.26 \text{ light-years} $$
> $$ 10 \text{ parsecs} = 10 \times 3.26 = 32.6 \text{ light-years} $$


### Check Your Understanding

1. **Unit Conversion**: The distance from Earth to Proxima Centauri is 4.24 light-years. Convert this distance to km, using appropriate scientific notation. How many Astonomical Units (AUs) would this be?
<br><br>

2. **Unit Conversion**: Convert the distance from Earth to the Sun (150 million kilometers) into light-years (use scientific notation).
<br><br>

3. **Solar System Scale**: If the Sun were the size of a basketball, how far would Neptune be in your model?
<br><br>

4. **Measuring Distances**: Explain how parallax is used to measure the distance to nearby stars.
<br><br>

5. **Parallax**: If a star has a parallax angle of 0.2 arcseconds, what is its distance from Earth in parsecs? Convert this distance to light-years and kilometers (using scientific notation).
<br><br>

6. **Observing the Universe**: Reflect on the significance of the Hubble Deep Field images and what they reveal about the universe.
<br><br>


```python
import numpy as np

# Light year derivation

# Speed of light in meters per second
c = 299792458  # m/s

# Seconds in a year
t = 60 * 60 * 24 * 365.25  # s/year

# Distance of one light year in meters
ly = c * t

print(f'There are {t:.3e} seconds in one year.')
print(f'Therefore, one light-year is approximately {ly:.3e} meters.')

# Example calculation for parallax

# Parallax angle in arcseconds
parallax_angle = 0.1  # arcseconds

# Distance in parsecs
distance_parsecs = 1 / parallax_angle

# Convert parsecs to light-years
distance_ly = distance_parsecs * 3.26

print(f'The distance to the star is {distance_parsecs:.2f} parsecs, which is {distance_ly:.2f} light-years.')

# CYU 1 - Unit Conversion: Distance to Proxima Centauri
d_ly = 4.24  # light-years

# Convert light-years to kilometers
d_km = d_ly * ly_km
print(f'The distance from Earth to Proxima Centauri is approximately {d_km:.2e} kilometers.')

# Astronomical Unit (AU)
AU = 1.496e+8  # kilometers

# Distance in AU
d_AU = d_km / AU
print(f'The distance from Earth to Proxima Centauri is approximately {d_AU:.2e} AU.')

# CYU 2 - Unit Conversion: Distance to the Sun
d_sun_km = 150e+6  # kilometers

# Convert distance to light-years
d_sun_ly = d_sun_km / ly_km
print(f'The distance from Earth to the Sun is approximately {d_sun_ly:.2e} light-years.')

# CYU 3 - Solar System Scale: Neptune distance
# If the Sun were the size of a basketball (24.26 cm diameter), how far would Neptune be?
# Assume Sun's actual diameter is 1.3927e+6 km and Neptune's average distance from the Sun is 4.495e+9 km
sun_diameter_basketball_cm = 24.26  # cm
sun_diameter_actual_km = 1.3927e+6  # km
neptune_distance_actual_km = 4.495e+9  # km

# Scale factor
scale_factor = sun_diameter_basketball_cm / sun_diameter_actual_km

# Scaled distance to Neptune
neptune_distance_scaled_cm = neptune_distance_actual_km * scale_factor
print(f'If the Sun were the size of a basketball, Neptune would be approximately {neptune_distance_scaled_cm:.2f} cm away.')

# CYU 5 - Parallax calculation
parallax_angle = 0.2  # arcseconds

# Distance in parsecs
d_parsecs = 1 / parallax_angle
print(f'The distance from Earth to the star is {d_parsecs:.2f} parsecs.')

# Convert parsecs to light-years
d_ly = d_parsecs * 3.26
print(f'The distance from Earth to the star is {d_ly:.2f} light-years.')

# Convert light-years to kilometers
d_km = d_ly * ly_km
print(f'The distance from Earth to the star is approximately {d_km:.2e} kilometers.')

```

    There are 3.156e+07 seconds in one year.
    Therefore, one light-year is approximately 9.461e+15 meters.
    The distance to the star is 10.00 parsecs, which is 32.60 light-years.
    The distance from Earth to Proxima Centauri is approximately 4.01e+13 kilometers.
    The distance from Earth to Proxima Centauri is approximately 2.68e+05 AU.
    The distance from Earth to the Sun is approximately 1.59e-05 light-years.
    If the Sun were the size of a basketball, Neptune would be approximately 78300.21 cm away.
    The distance from Earth to the star is 5.00 parsecs.
    The distance from Earth to the star is 16.30 light-years.
    The distance from Earth to the star is approximately 1.54e+14 kilometers.


## 1.3 The Celestial Sphere


### Check Your Understanding

1. How many degrees does the Sun move per day relative to the fixed stars? How many days does it take for the Sun to return to its original location relative to the fixed stars?
<br><br>

2. The Moon's orbital period around Earth is approximately 27.3 days. How many degrees does the Moon move per day relative to the fixed stars? 
<br><br>

3. Is the ecliptic the same thing as the celestial equator? Explain.
<br><br>

4. Explain why more stars are circumpolar for observers at higher latitudes.
<br><br>

5. What is the altitude of the north celestial pole in the sky from your latitude? (The latitude of Salt Spring Island, BC is approximately 49 degrees N.)
<br><br>

6. Suppose you are on a strange planet and observe, at night, that the stars do not rise and set, but circle parallel to the horizon. Next, you walk in a constant direction for 8000 miles, and at your new location on the planet, you find that all stars rise straight up in the east and set straight down in the west, perpendicular to the horizon. How could you determine the circumference of the planet without any further observations? What is the circumference, in miles, of the planet?
<br><br>



```python
# CYU 1 - Sun's movement
days_in_year = 365.25
degrees_per_day = 360 / days_in_year
print(f'The Sun moves approximately {degrees_per_day:.2f} degrees per day relative to the fixed stars.')
# CYU 2 - Moon's movement
moon_orbital_period_days = 27.3
degrees_per_day_moon = 360 / moon_orbital_period_days
print(f'The Moon moves approximately {degrees_per_day_moon:.2f} degrees per day relative to the fixed stars.')
# CYU 5 - Altitude of the north celestial pole
latitude_salt_spring_island = 49  # degrees N
altitude_north_celestial_pole = latitude_salt_spring_island
print(f'The altitude of the north celestial pole in the sky from Salt Spring Island, BC is {altitude_north_celestial_pole:.2f} degrees.')
# CYU 6 - Circumference of the planet
distance_walked_miles = 8000  # miles

# When stars rise straight up in the east and set straight down in the west, it means you have traveled from the pole to the equator, which is 1/4 of the planet's circumference
circumference_planet = 4 * distance_walked_miles
print(f'The circumference of the planet is approximately {circumference_planet} miles.')

```

    The Sun moves approximately 0.99 degrees per day relative to the fixed stars.
    The Moon moves approximately 13.19 degrees per day relative to the fixed stars.
    The altitude of the north celestial pole in the sky from Salt Spring Island, BC is 49.00 degrees.
    The circumference of the planet is approximately 32000 miles.


# 1.4 The Brightness of Stars

<div class="alert alert-block alert-warning">
<b>Example:</b> Calculating the Solar Flux at Different Distances
</div>

> The luminosity of the Sun is $ 3.839 \times 10^{26} $ W and is at a distance of 1 AU (astronomical unit) away from Earth, which is $ 1.496 \times 10^{11} $ meters.
> 
> Earth receives a radiant flux above its absorbing atmosphere given by:
> 
> > $$ F = \frac{L}{4\pi r^2} $$
> > 
> > $$ F = \frac{3.839 \times 10^{26}}{4\pi (1.496 \times 10^{11})^2} $$
> > 
> > $$ F \approx 1365 \, \text{W/m}^2 $$
>
>This value of the solar flux is known as the **solar irradiance**, sometimes also called the solar constant.

<div class="alert alert-block alert-warning">
<b>Example:</b> Suppose an astronomer has discovered something special about a dim star with a magnitude of 8.5 and wants to explain how much dimmer this star is compared to Sirius. We'll use the dim star as Star 1 and Sirius as Star 2 in our equation.
</div>

> Given:
> 
> > Dim star magnitude, $ m_1 = 8.5 $
> > 
> > Sirius magnitude, $ m_2 = -1.5 $
> 
> Solution:
> 
> > $$ \frac{F_2}{F_1} = \left(100^{0.2}\right)^{8.5 - (-1.5)} $$
> > 
> > $$ \frac{F_2}{F_1} = \left(100^{0.2}\right)^{10} $$
> > 
> > $$ \frac{F_2}{F_1} = (100)^2 = 100 \times 100 = 10,000 $$
> > 
> > Therefore, the dim star is 10,000 times dimmer than Sirius.

<div class="alert alert-block alert-warning">
<b>Example:</b> It is a common misconception that Polaris (magnitude 2.0) is the brightest star in the sky. However, Sirius, with a magnitude of -1.5, holds that title. Let's compare the apparent brightness of Sirius to Polaris.
</div>

> Given:
> 
> > Polaris magnitude, $ m_1 = 2.0 $
> > 
> > Sirius magnitude, $ m_2 = -1.5 $
> 
> Solution:
> 
> > $$ \frac{F_2}{F_1} = \left(100^{0.2}\right)^{2.0 - (-1.5)} $$
> > 
> > $$ \frac{F_2}{F_1} = \left(100^{0.2}\right)^{3.5} $$
> > 
> > $$ \frac{F_2}{F_1} = 100^{0.7} = 25 $$
> 
> Our calculation shows that Sirius’ apparent brightness is 25 times greater than Polaris’ apparent brightness.

<div class="alert alert-block alert-warning">
<b>Example:</b> Calculating the Absolute Magnitude of the Sun
</div>

> The apparent magnitude of the Sun, $ m_{\text{Sun}} $, is $ -26.83 $, and its distance from Earth is 1 AU, which is $ 4.848 \times 10^{-6} $ parsecs. Using the formula for absolute magnitude:
> 
> $$ M_{\text{Sun}} = m_{\text{Sun}} - 5 \log_{10}(d) + 5 $$
> 
> we can calculate the absolute magnitude of the Sun.
> 
> $$ M_{\text{Sun}} = m_{\text{Sun}} - 5 \log_{10}(d) + 5 $$
> 
> $$ M_{\text{Sun}} = -26.83 - 5 \log_{10}(4.848 \times 10^{-6}) + 5 $$
> 
> Since $ \log_{10}(4.848 \times 10^{-6}) \approx -5.315 $:
> 
> $$ M_{\text{Sun}} = -26.83 - 5(-5.315) + 5 $$
> 
> $$ M_{\text{Sun}} = -26.83 + 26.575 + 5 $$
> 
> $$ M_{\text{Sun}} = 4.74 $$
>
>> Thus, the absolute magnitude of the Sun is $ +4.74 $.

---

## Check Your Understanding

1. **Flux and Luminosity**: Given a star with a luminosity of $ 4 \times 10^{26} $ watts and a distance of 2 parsecs, calculate the flux received on Earth.
<br><br>
2. **Absolute Magnitude**: If a star has an apparent magnitude of 7 and is located 50 parsecs away, what is its absolute magnitude?
<br><br>
3. **Apparent Brightness**: Two stars have apparent magnitudes of 3 and 5. Calculate the ratio of their fluxes.
<br><br>
4. **Distance Modulus**: Calculate the distance to a star with an apparent magnitude of 10 and an absolute magnitude of 2.
<br><br>
5. **Flux**: At what distance from a 100-W light bulb is the radiant flux equal to the solar irradiance?
<br><br>
6. **Bonus**: Derive the relation

$$m = M_{Sun} − 2.5 \log_{10}(\frac{F}{F_{10,Sun}})$$


```python
# Example - Solar Flux at Different Distances

# Given values
L_sun = 3.839e26  # watts
r_earth_sun_m = 1.496e11  # meters

# Calculate the flux
F_earth = L_sun / (4 * np.pi * r_earth_sun_m**2)
print(f'The solar flux received on Earth is approximately {F_earth:.2f} W/m^2.')

# Example - Comparing brightness of dim star and Sirius

# Given magnitudes
m1 = 8.5
m2 = -1.5

# Calculate the flux ratio
flux_ratio = (100**0.2)**(m1 - m2)
print(f'The dim star is {flux_ratio:.2f} times dimmer than Sirius.')

# Example - Comparing brightness of Sirius and Polaris

# Given magnitudes
m1 = 2.0
m2 = -1.5

# Calculate the flux ratio
flux_ratio = (100**0.2)**(m1 - m2)
print(f'Sirius is {flux_ratio:.2f} times brighter than Polaris.')

# Example - Absolute Magnitude of the Sun

# Given values
m_sun = -26.83
d_sun_parsecs = 4.848e-6  # parsecs

# Calculate the absolute magnitude
M_sun = m_sun - 5 * (np.log10(d_sun_parsecs) - 1)
print(f'The absolute magnitude of the Sun is {M_sun:.2f}.')

# CYU 1 - Flux and Luminosity

# Given luminosity of the star
L_star = 4e26  # watts

# Distance to the star in parsecs
d_parsecs = 2  # parsecs

# Convert distance from parsecs to meters (1 parsec ≈ 3.086e16 meters)
d_meters = d_parsecs * 3.086e16

# Calculate the flux
F_star = L_star / (4 * np.pi * d_meters**2)
print(f'The flux received on Earth from the star is approximately {F_star:.2e} W/m^2.')

# CYU 2 - Absolute Magnitude

# Given apparent magnitude of the star
m_star = 7

# Distance to the star in parsecs
d_star = 50  # parsecs

# Calculate absolute magnitude using the distance modulus formula
M_star = m_star - 5 * (np.log10(d_star) - 1)
print(f'The absolute magnitude of the star is {M_star:.2f}.')
# CYU 3 - Apparent Brightness

# Given apparent magnitudes of two stars
m1 = 3
m2 = 5

# Calculate the ratio of their fluxes
flux_ratio = 100**((m2 - m1) / 5)
print(f'The ratio of the fluxes of the two stars is {flux_ratio:.2f}.')
# CYU 4 - Distance Modulus

# Given apparent magnitude and absolute magnitude of the star
m_star = 10
M_star = 2

# Calculate the distance to the star using the distance modulus formula
d_star = 10**((m_star - M_star + 5) / 5)
print(f'The distance to the star is {d_star:.2f} parsecs.')

```

    The solar flux received on Earth is approximately 1365.04 W/m^2.
    The dim star is 10000.00 times dimmer than Sirius.
    Sirius is 25.12 times brighter than Polaris.
    The absolute magnitude of the Sun is 4.74.
    The flux received on Earth from the star is approximately 8.36e-09 W/m^2.
    The absolute magnitude of the star is 3.51.
    The ratio of the fluxes of the two stars is 6.31.
    The distance to the star is 398.11 parsecs.


### 1.5 Consequences of Light Travel Time

<div class="alert alert-block alert-warning">
<b>Example:</b> Imagine astronomers observe a Cepheid variable star in a nearby galaxy. The observed apparent magnitude of the star is 15.2, and its absolute magnitude is known to be -3.4. Calculate the distance to the Cepheid variable star.
</div>

> **Solution**:
>
> 1. **Formula**: The distance modulus formula relates the apparent magnitude ($m$) and absolute magnitude ($M$) of a star to its distance in parsecs ($d$):
>    $$
>    m - M = 5 \log_{10}(d) - 5
>    $$
> 2. **Rearrange the Formula to Solve for Distance**:
>    $$
>    m - M + 5 = 5 \log_{10}(d)
>    $$
>    $$
>    \frac{m - M + 5}{5} = \log_{10}(d)
>    $$
>    $$
>    d = 10^{\left( \frac{m - M + 5}{5} \right)}
>    $$
> 3. **Substitute the Given Values**: $m = 15.2$, $M = -3.4$
>    $$
>    d = 10^{\left( \frac{15.2 - (-3.4) + 5}{5} \right)}
>    $$
>    $$
>    d = 10^{\left( \frac{15.2 + 3.4 + 5}{5} \right)}
>    $$
>    $$
>    d = 10^{\left( \frac{23.6}{5} \right)}
>    $$
>    $$
>    d = 10^{4.72}
>    $$
> 4. **Calculate the Distance**:
>    $$
>    d \approx 52,480 \text{ parsecs}
>    $$
> 
>> Therefore, the distance to the Cepheid variable star is approximately 52,480 parsecs.

## Check Your Understanding

1. **Reflect on Historical Contributions**: How did early experiments by Ole Rømer and Albert A. Michelson contribute to our understanding of light travel time?
   <br><br>

2. **Unit Conversion**: The distance from Earth to Proxima Centauri is 4.24 light-years. Convert this distance to kilometers.
   <br><br>

3. **Parallax Calculation**: If a star has a parallax angle of 0.2 arcseconds, what is its distance from Earth in parsecs? Convert this distance to light-years.
   <br><br>

4. **Observing the Past**: Explain how observing distant galaxies allows astronomers to study the early universe.
   <br><br>

5. **Future Telescopes**: Discuss the potential impact of the James Webb Space Telescope on our understanding of the universe.
   <br><br>

Imagine astronomers observe a supernova in a distant galaxy. The light from the supernova, which occurred 163 years ago, has just reached Earth. Determine the parallax angle of the supernova.


```python
# Example - Distance to Cepheid Variable Star

# Given values
m_cepheid = 15.2
M_cepheid = -3.4

# Calculate the distance using the distance modulus formula
d_cepheid = 10**((m_cepheid - M_cepheid + 5) / 5)
print(f'The distance to the Cepheid variable star is approximately {d_cepheid:.2f} parsecs.')
# CYU 2 - Unit Conversion: Distance to Proxima Centauri
d_ly = 4.24  # light-years

# Convert light-years to kilometers
d_km = d_ly * ly_km
print(f'The distance from Earth to Proxima Centauri is approximately {d_km:.2e} kilometers.')

# CYU 3 - Parallax Calculation
parallax_angle = 0.2  # arcseconds

# Distance in parsecs
d_parsecs = 1 / parallax_angle
print(f'The distance from Earth to the star is {d_parsecs:.2f} parsecs.')

# Convert parsecs to light-years
d_ly = d_parsecs * 3.26
print(f'The distance from Earth to the star is {d_ly:.2f} light-years.')

```

    The distance to the Cepheid variable star is approximately 52480.75 parsecs.
    The distance from Earth to Proxima Centauri is approximately 4.01e+13 kilometers.
    The distance from Earth to the star is 5.00 parsecs.
    The distance from Earth to the star is 16.30 light-years.



```python

```
