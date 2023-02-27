# MERFISH Analysis Routine

## Overview

MERFISH is a massively multiplexed single molecule imaging technology capable of simultaneously measuring the copy number and spatial distribution of hundreds to thousands of RNA species across hundreds of thousands of individual cells with unmatched detection efficiency.

Around 90% of the ~370 nonsensory GPCRs express in the brain and are critical for the regulation of neuronal excitability, metabolism, reproduction, development, hormonal homeostasis, and behavior. GPCRs are especially playing an increasing role in studying the aging brain and subsequent effects on the CNS and NDDs. 30% of marketed drugs modulate specific GPCRs. Analysis of GPCRs in vivo is a difficult process because of their structural properties, low abundance and lack of highly specific antibodies. MERFISH technology can play a critical role in the continued mapping of GPCR expressions in the brain as a high throughput spatially resolved technology with robust sensitivity and resolution.

In this analysis, I used a dataset that contains a MERFISH measurement of a gene panel containing 483 total genes including canonical brain cell type markers, GPCRs, and RTKs measured on 3 full coronal slices with 3 biological replicates for each slice position. The dataset includes the list of detected transcripts, gene counts per cell matrix, additional spatial cell metadata, cell boundary polygons, and DAPI images.

## Pipeline
- [DAPI Mosaic Image View]()
- [Single Field of View]()
- [Cluster Gene Expression Data]()
- [Map Leiden Clusters to Tentative Cell Types]()
- [scRNA-seq and MERFISH Integration]()
- [smnC-seq and MERFISH Integration]()
- [Pseudotime Analysis]() 
- [SpatialIDE]()

## Samples
This dataset includes 9 MERFISH measurements of full mouse coronal slices using a panel of 483 genes, including 3 slices at different positions along the rostral-codal axis with 3 biological replicates. Each replicate measurement includes:
### Information on all transcripts detected in the sample
- detected_transcripts_XX.csv - list of all detected transcripts in the sample where each row is a detected transcript. The columns are:
- barcode_id - internally used id of the gene
- global_x, global_y - The global micron x and y coordinates of this transcript
- x, y - The pixel coordinates of this transcript within the field of view
- global_z - The index of the z slice that this transcript was detected in. Each z slice is separated by 1.5 micronsfov - the index of the field of view where this transcript was detected
- gene - the gene name of this detected transcript

### Single cell information from cell segmentation
- cell_by_gene_XX.csv - Count of detected transcripts within the segmentation boundaries for each cell for each gene. Each row corresponds to a cell and the first column contains the cells unique ID. Each remaining column corresponds to a gene.
- cell_metadata_XX.csv - Spatial metadata for each of the detected cells. Each row corresponds to a cell. The first column in the unique cell ID and the remaining columns are:
- fov - the field of view containing the cell
- volume - The volume of the cell in um^3
- center_x, center_y - the x and y coordinate of the center of the cell in global micron coordinates
- min_x, max_x, min_x, max_y - the minimum and maximum of the bounding box containing this cell in x and y in global micron coordinates
- cell_boundaries/feature_data_X.hdf5 - Polygon boundaries for cells identified in field of view X. If no cells were detected within field of view X then there will be no file feature_data_X.hdf5.

### Mosaic images of the full tissue
- images/mosaic_X_zY.tif - Mosaic image of additional stains where X indicates the name of the stain (DAPI, polyT) and Y is the z index of the image
- images/micron_to_mosaic_pixel_transform.csv - Transformation matrix for converting from real world micron coordinates to pixels


## Code References
- https://github.com/FangmingXie/merfish_vizgen


## Work in Progress
-[ ] Improve the cell semgentation algorithm.
-[ ] Integrate the parallel image processing pipeline.
-[ ] Improve the pseudotime or RNA velocity analysis.
-[ ] Add ligand-receptor interaction analysis. 
