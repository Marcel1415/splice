[![DOI](https://zenodo.org/badge/644778381.svg)](https://zenodo.org/badge/latestdoi/644778381)

# splice

A simple Jupyter Notebook to visualize the splice of a composite core of long cores, based on a logic table (`merge_sheet`)

`splice` uses the IODP Depth Scales Terminology (https://www.iodp.org/policies-and-guidelines/142-iodp-depth-scales-terminology-april-2011/file) within the `merge_sheet`. And visualizes the raw dataset, simple filtered dataset (based on IQR: https://en.wikipedia.org/wiki/Interquartile_range) and a Gaussian smoothed dataset.

# Setup

The Jupyter Notebook runs on Python 3, with `pandas`, `numpy`, `matplotlib` and `pathlib`

Install the required packages:
```
pip install -r requirements.txt
```

Create `merge_sheet` including the
1) 'splice_num' representing the order of the various sediment core section
2) 'Name' of the sediment core section, which need to be identical to the name of the core section of the dataset
3) 'core_TOP' in mm which represents the sediment TOP of a core section
4) 'core_BOTTOM' in mm which represents the sediment BOTTOM of a core section
5) 'Vertical offset' based on IODP Depth Scales Terminology
6) 'Depth_CSF-A_(m)_Top' to calculate core depth etc. within the Jupyter Notebook

# Usage

Individual core sections of a splice will be tied or appended depending on the `merge_sheet` and combined into a single dataframe

## Getting statistics data

Split up the dataframe to individual segments if needed, and use `describe()` for a quick analysis
