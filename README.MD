# Interaktiv Volto Animated Layers Block

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)
![Plone 6.0.x](https://img.shields.io/badge/Plone-6.0.x-blue.svg)

## USE AT YOUR OWN RISK

This addon bypasses a Plone security feature of @@display-file.

It serves as an enhancement to "volto-animated-layeres-block", enabling the usage of SVGs from your Plone Files instead of external SVGs. 
However, Plone has disabled this functionality for security purposes. If you still wish to utilize it, 
this addon will introduce a view "@@display-file-svg" that allows the inline display of SVGs, which is then used by "volto-animated-layeres-block".