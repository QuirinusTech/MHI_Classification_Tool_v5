# MHI_Classification_Tool_v5

The MHI classification tool is essentially a large spreadsheet for determining whether a given inventory of substances exceeds any of the thresholds of the current regulations.
The calculations done are purely on the basis of inventory size and substance type.
No ther factors are taken into accout as they would be during a proper full MHI assessment

The user adds substances to a fictional inventory, that is supposed to represent the chemicals stored by a company on their premises
Once they've added all the substances they have on their premises, the calculator will perform two assessments:
1. Do any of the substances on exceed any of the thresholds stipulated for that particular substance and, if so, which of the three levels?
2. If no single substance exceeds the threshhold, do any specific combinations of chemicals (groupings specified by the regulations), when counted together, exceed the allowed thresholds.

Finally the tool will give a basic Risk Tier in the form of a numbers between 0 and 3 (0 being no risk and 3 being the highest level)

The Hyginus module contains the Database with roughly 40 named chemicals. These are taken directly from the current regulation documentation.
It also contains guidelines and thresholds for custom substance addition.

A note on the listed substances:
When users try to add a substance 