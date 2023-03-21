#  Preview: Vasculature CCF Visualization for Intestine Data

HuBMAP Atlas Previews demonstrate functionality and resources that will become available in future HuBMAP portal releases. Previews may rely on externally hosted data or analysis results that were generated with processing pipelines that are not yet integrated into the HuBMAP data infrastructure.


### Description

This preview showcases a novel visualization in support of a vasculature-based common coordinate system (VCCF), see paper on “[Considerations for Using the Vasculature as a Coordinate System to Map All the Cells in the Human Body](https://doi.org/10.3389/fcvm.2020.00029)”.

Experimental data from the “[High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine](https://www.biorxiv.org/content/early/2021/11/25/2021.11.25.469203)” paper, is used to compute distances of different cell types to the nearest blood vessel using 2D volumes of digital intestine biopsy data generated using multiplexed imaging on 64 sections of the human intestine (~16 mm2) from 8 donors (B004, B005, B006, B008, B009, B010, B011, and B012) using a panel of 57 oligonucleotide-barcoded antibodies. Subsequently, images underwent standard CODEX image processing (tile stitching, drift compensation, cycle concatenation, background subtraction, deconvolution, and determination of best focal plane), single cell segmentation, and column marker z-normalization by tissue. The outputs of this process were data frames of 2.6 million cells with 57 antibody fluorescence values quantified from each marker. Each cell has its cell type, cellular neighborhood, community of neighborhooods, and tissue unit defined with x, y coordinates representing pixel location in the original image. This data was taken from  8 donors with 8 individual tissue regions (64 tissues imaged) across 2.6 million cells, with 25 cell types, 20 multicellular neighborhoods, 10 communities of neighborhoods, and 3 tissue segments could be used to understand the cellular interactions, composition, and structure of the human intestine from the duodenum to the sigmoid colon and understand differences between different areas of the intestine. 


### Atlas Details

This Preview showcases a 2D interactive visualization of distances from cell nuclei of different cell types(NK, M1 Macrophage, CD8+ T, DC, M2 Macrophage, B, Neutrophil, Plasma, CD4+ T cell, CD7+ Immune) to vasculature across donor groups.  


### Experimental Data Details

The experimental intestine data used here is detailed in the “[High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine](https://www.biorxiv.org/content/early/2021/11/25/2021.11.25.469203)” paper.

### Contributors
**Intestine Data:** John Hickey et al.

**Vasculature CCF Visualization:** Himani Shah, Yingnan Ju & Katy Börner


### Attribution

| Group  | Creator                          |
|--------|----------------------------------|
| TMC-Stanford | John Hickey (jwhickey@stanford.edu) |
| MC-IU  | Katy Börner (katy@indiana.edu)   |


### Visualization

<div class="tabs-nav">
  <ul class="nav nav-tabs">
    <li class="active"><a data-toggle="tab" href="#region1">Region 1</a></li>
    <li><a data-toggle="tab" href="#region2">Region 2</a></li>
    <li><a data-toggle="tab" href="#region3">Region 3</a></li>
    <li><a data-toggle="tab" href="#region4">Region 4</a></li>
    <li><a data-toggle="tab" href="#region5">Region 5</a></li>
    <li><a data-toggle="tab" href="#region6">Region 6</a></li>
    <li><a data-toggle="tab" href="#region7">Region 7</a></li>
    <li><a data-toggle="tab" href="#region8">Region 8</a></li>
    <li><a data-toggle="tab" href="#region9">Region 9</a></li>
    <li><a data-toggle="tab" href="#region10">Region 10</a></li>
    <li><a data-toggle="tab" href="#region11">Region 11</a></li>
    <li><a data-toggle="tab" href="#region12">Region 12</a></li>
    <li><a data-toggle="tab" href="#region13">Region 13</a></li>
    <li><a data-toggle="tab" href="#region14">Region 14</a></li>
    <li><a data-toggle="tab" href="#region15">Region 15</a></li>
    <li><a data-toggle="tab" href="#region16">Region 16</a></li>
    <li><a data-toggle="tab" href="#region17">Region 17</a></li>
    <li><a data-toggle="tab" href="#region18">Region 18</a></li>
    <li><a data-toggle="tab" href="#region19">Region 19</a></li>
    <li><a data-toggle="tab" href="#region20">Region 20</a></li>
    <li><a data-toggle="tab" href="#region21">Region 21</a></li>
    <li><a data-toggle="tab" href="#region22">Region 22</a></li>
    <li><a data-toggle="tab" href="#region23">Region 23</a></li>
    <li><a data-toggle="tab" href="#region24">Region 24</a></li>
    <li><a data-toggle="tab" href="#region25">Region 25</a></li>
    <li><a data-toggle="tab" href="#region26">Region 26</a></li>
    <li><a data-toggle="tab" href="#region27">Region 27</a></li>
    <li><a data-toggle="tab" href="#region28">Region 28</a></li>
    <li><a data-toggle="tab" href="#region29">Region 29</a></li>
    <li><a data-toggle="tab" href="#region30">Region 30</a></li>
    <li><a data-toggle="tab" href="#region31">Region 31</a></li>
    <li><a data-toggle="tab" href="#region32">Region 32</a></li>
    <li><a data-toggle="tab" href="#region33">Region 33</a></li>
    <li><a data-toggle="tab" href="#region34">Region 34</a></li>
    <li><a data-toggle="tab" href="#region35">Region 35</a></li>
    <li><a data-toggle="tab" href="#region36">Region 36</a></li>
    <li><a data-toggle="tab" href="#region37">Region 37</a></li>
    <li><a data-toggle="tab" href="#region38">Region 38</a></li>
    <li><a data-toggle="tab" href="#region39">Region 39</a></li>
    <li><a data-toggle="tab" href="#region40">Region 40</a></li>
    <li><a data-toggle="tab" href="#region41">Region 41</a></li>
    <li><a data-toggle="tab" href="#region42">Region 42</a></li>
    <li><a data-toggle="tab" href="#region43">Region 43</a></li>
    <li><a data-toggle="tab" href="#region44">Region 44</a></li>
    <li><a data-toggle="tab" href="#region45">Region 45</a></li>
    <li><a data-toggle="tab" href="#region46">Region 46</a></li>
    <li><a data-toggle="tab" href="#region47">Region 47</a></li>
    <li><a data-toggle="tab" href="#region48">Region 48</a></li>
    <li><a data-toggle="tab" href="#region49">Region 49</a></li>
    <li><a data-toggle="tab" href="#region50">Region 50</a></li>
    <li><a data-toggle="tab" href="#region51">Region 51</a></li>
    <li><a data-toggle="tab" href="#region52">Region 52</a></li>
    <li><a data-toggle="tab" href="#region53">Region 53</a></li>
    <li><a data-toggle="tab" href="#region54">Region 54</a></li>
    <li><a data-toggle="tab" href="#region55">Region 55</a></li>
    <li><a data-toggle="tab" href="#region56">Region 56</a></li>
    <li><a data-toggle="tab" href="#region57">Region 57</a></li>
    <li><a data-toggle="tab" href="#region58">Region 58</a></li>
    <li><a data-toggle="tab" href="#region59">Region 59</a></li>
    <li><a data-toggle="tab" href="#region61">Region 60</a></li>
    <li><a data-toggle="tab" href="#region61">Region 61</a></li>
    <li><a data-toggle="tab" href="#region62">Region 62</a></li>
    <li><a data-toggle="tab" href="#region63">Region 63</a></li>
    <li><a data-toggle="tab" href="#region64">Region 64</a></li>

  </ul>

  
  <div class="tab-content">
    <div id="region1" class="tab-pane fade in active">
      <h3>Region 1</h3>
      <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_1.html" >
      <img src="../../images_vccf/Region_1.png" alt="region1" style="width:100%">
        </a>
      <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_1.html" >new window.</a>  
    </div>
    <div id="region2" class="tab-pane fade">
      <h3>Region 2</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_2.html" >
      <img src="../../images_vccf/Region_2.png" alt="region2" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_2.html" >new window.</a>
  </div>
    <div id="region3" class="tab-pane fade">
      <h3>Region 3</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_3.html" >
      <img src="../../images_vccf/Region_3.png" alt="region3" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_3.html" >new window.</a>
    </div>
    <div id="region4" class="tab-pane fade">
      <h3>Region 4</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_4.html" >
      <img src="../../images_vccf/Region_4.png" alt="region4" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_4.html" >new window.</a>
    </div>
    <div id="region5" class="tab-pane fade">
      <h3>Region 5</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_5.html" >
      <img src="../../images_vccf/Region_5.png" alt="region5" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_5.html" >new window.</a>
    </div>
    <div id="region6" class="tab-pane fade">
      <h3>Region 6</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_6.html" >
      <img src="../../images_vccf/Region_6.png" alt="region6" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_6.html" >new window.</a>
    </div>
    <div id="region7" class="tab-pane fade">
      <h3>Region 7</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_7.html" >
      <img src="../../images_vccf/Region_7.png" alt="region7" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_7.html" >new window.</a>
    </div>
    <div id="region8" class="tab-pane fade">
      <h3>Region 8</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_8.html" >
      <img src="../../images_vccf/Region_8.png" alt="region8" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_8.html" >new window.</a>
    </div>
    <div id="region9" class="tab-pane fade">
      <h3>Region 9</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_9.html" >
      <img src="../../images_vccf/Region_9.png" alt="region9" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_9.html" >new window.</a>
    </div>
    <div id="region10" class="tab-pane fade">
      <h3>Region 10</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_10.html" >
      <img src="../../images_vccf/Region_10.png" alt="region10" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_10.html" >new window.</a>
    </div>
    <div id="region11" class="tab-pane fade">
      <h3>Region 11</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_11.html" >
      <img src="../../images_vccf/Region_11.png" alt="region11" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_11.html" >new window.</a>
    </div>
    <div id="region12" class="tab-pane fade">
      <h3>Region 12</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_12.html" >
      <img src="../../images_vccf/Region_12.png" alt="region12" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_12.html" >new window.</a>
    </div>
    <div id="region13" class="tab-pane fade">
      <h3>Region 13</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_13.html" >
      <img src="../../images_vccf/Region_13.png" alt="region13" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_13.html" >new window.</a>
    </div>
    <div id="region14" class="tab-pane fade">
      <h3>Region 14</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_14.html" >
      <img src="../../images_vccf/Region_14.png" alt="region14" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_14.html" >new window.</a>
    </div>
    <div id="region15" class="tab-pane fade">
      <h3>Region 15</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_15.html" >
      <img src="../../images_vccf/Region_15.png" alt="region15" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_15.html" >new window.</a>
    </div>
    <div id="region16" class="tab-pane fade">
      <h3>Region 16</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_16.html" >
      <img src="../../images_vccf/Region_16.png" alt="region16" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_16.html" >new window.</a>
    </div>
    <div id="region17" class="tab-pane fade">
      <h3>Region 17</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_17.html" >
      <img src="../../images_vccf/Region_17.png" alt="region17" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_17.html" >new window.</a>
    </div>
    <div id="region18" class="tab-pane fade">
      <h3>Region 18</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_18.html" >
      <img src="../../images_vccf/Region_18.png" alt="region18" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_18.html" >new window.</a>
    </div>
    <div id="region19" class="tab-pane fade">
      <h3>Region 19</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_19.html" >
      <img src="../../images_vccf/Region_19.png" alt="region19" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_19.html" >new window.</a>
    </div>
    <div id="region20" class="tab-pane fade">
      <h3>Region 20</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_20.html" >
      <img src="../../images_vccf/Region_20.png" alt="region20" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_20.html" >new window.</a>
    </div>
    <div id="region21" class="tab-pane fade">
      <h3>Region 21</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_21.html" >
      <img src="../../images_vccf/Region_21.png" alt="region21" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_21.html" >new window.</a>
    </div>
    <div id="region22" class="tab-pane fade">
      <h3>Region 22</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_22.html" >
      <img src="../../images_vccf/Region_22.png" alt="region22" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_22.html" >new window.</a>
    </div>
    <div id="region23" class="tab-pane fade">
      <h3>Region 23</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_23.html" >
      <img src="../../images_vccf/Region_23.png" alt="region23" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_23.html" >new window.</a>
    </div>
    <div id="region24" class="tab-pane fade">
      <h3>Region 24</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_24.html" >
      <img src="../../images_vccf/Region_24.png" alt="region24" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_24.html" >new window.</a>
    </div>
    <div id="region25" class="tab-pane fade">
      <h3>Region 25</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_25.html" >
      <img src="../../images_vccf/Region_25.png" alt="region25" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_25.html" >new window.</a>
    </div>
    <div id="region26" class="tab-pane fade">
      <h3>Region 26</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_26.html" >
      <img src="../../images_vccf/Region_26.png" alt="region26" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_26.html" >new window.</a>
    </div>
    <div id="region27" class="tab-pane fade">
      <h3>Region 27</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_27.html" >
      <img src="../../images_vccf/Region_27.png" alt="region27" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_27.html" >new window.</a>
    </div>
    <div id="region28" class="tab-pane fade">
      <h3>Region 28</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_28.html" >
      <img src="../../images_vccf/Region_28.png" alt="region28" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_28.html" >new window.</a>
    </div>
    <div id="region29" class="tab-pane fade">
      <h3>Region 29</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_29.html" >
      <img src="../../images_vccf/Region_29.png" alt="region29" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_29.html" >new window.</a>
    </div>
    <div id="region30" class="tab-pane fade">
      <h3>Region 30</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_30.html" >
      <img src="../../images_vccf/Region_30.png" alt="region30" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_30.html" >new window.</a>
    </div>
    <div id="region31" class="tab-pane fade">
      <h3>Region 31</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_31.html" >
      <img src="../../images_vccf/Region_31.png" alt="region31" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_31.html" >new window.</a>
    </div>
    <div id="region32" class="tab-pane fade">
      <h3>Region 32</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_32.html" >
      <img src="../../images_vccf/Region_32.png" alt="region32" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_32.html" >new window.</a>
    </div>
    <div id="region33" class="tab-pane fade">
      <h3>Region 33</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_33.html" >
      <img src="../../images_vccf/Region_33.png" alt="region33" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_33.html" >new window.</a>
    </div>
    <div id="region34" class="tab-pane fade">
      <h3>Region 34</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_34.html" >
      <img src="../../images_vccf/Region_34.png" alt="region34" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_34.html" >new window.</a>
    </div>
    <div id="region35" class="tab-pane fade">
      <h3>Region 35</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_35.html" >
      <img src="../../images_vccf/Region_35.png" alt="region35" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_35.html" >new window.</a>
    </div>
    <div id="region36" class="tab-pane fade">
      <h3>Region 36</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_36.html" >
      <img src="../../images_vccf/Region_36.png" alt="region36" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_36.html" >new window.</a>
    </div>
    <div id="region37" class="tab-pane fade">
      <h3>Region 37</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_37.html" >
      <img src="../../images_vccf/Region_37.png" alt="region37" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_37.html" >new window.</a>
    </div>
    <div id="region38" class="tab-pane fade">
      <h3>Region 38</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_38.html" >
      <img src="../../images_vccf/Region_38.png" alt="region38" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_38.html" >new window.</a>
    </div>
    <div id="region39" class="tab-pane fade">
      <h3>Region 39</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_39.html" >
      <img src="../../images_vccf/Region_39.png" alt="region39" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_39.html" >new window.</a>
    </div>
    <div id="region40" class="tab-pane fade">
      <h3>Region 40</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_40.html" >
      <img src="../../images_vccf/Region_40.png" alt="region40" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_40.html" >new window.</a>
    </div>
    <div id="region41" class="tab-pane fade">
      <h3>Region 41</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_41.html" >
      <img src="../../images_vccf/Region_41.png" alt="region41" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_41.html" >new window.</a>
    </div>
    <div id="region42" class="tab-pane fade">
      <h3>Region 42</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_42.html" >
      <img src="../../images_vccf/Region_42.png" alt="region42" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_42.html" >new window.</a>
    </div>
    <div id="region43" class="tab-pane fade">
      <h3>Region 43</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_43.html" >
      <img src="../../images_vccf/Region_43.png" alt="region43" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_43.html" >new window.</a>
    </div>
    <div id="region44" class="tab-pane fade">
      <h3>Region 44</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_44.html" >
      <img src="../../images_vccf/Region_44.png" alt="region44" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_44.html" >new window.</a>
    </div>
    <div id="region45" class="tab-pane fade">
      <h3>Region 45</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_45.html" >
      <img src="../../images_vccf/Region_45.png" alt="region45" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_45.html" >new window.</a>
    </div>
    <div id="region46" class="tab-pane fade">
      <h3>Region 46</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_46.html" >
      <img src="../../images_vccf/Region_46.png" alt="region46" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_46.html" >new window.</a>
    </div>
    <div id="region47" class="tab-pane fade">
      <h3>Region 47</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_47.html" >
      <img src="../../images_vccf/Region_47.png" alt="region47" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_47.html" >new window.</a>
    </div>
    <div id="region48" class="tab-pane fade">
      <h3>Region 48</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_48.html" >
      <img src="../../images_vccf/Region_48.png" alt="region48" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_48.html" >new window.</a>
    </div>
    <div id="region49" class="tab-pane fade">
      <h3>Region 49</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_49.html" >
      <img src="../../images_vccf/Region_49.png" alt="region49" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_49.html" >new window.</a>
    </div>
    <div id="region50" class="tab-pane fade">
      <h3>Region 50</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_50.html" >
      <img src="../../images_vccf/Region_50.png" alt="region50" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_50.html" >new window.</a>
    </div>
    <div id="region51" class="tab-pane fade">
      <h3>Region 51</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_51.html" >
      <img src="../../images_vccf/Region_51.png" alt="region51" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_51.html" >new window.</a>
    </div>
    <div id="region52" class="tab-pane fade">
      <h3>Region 52</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_52.html" >
      <img src="../../images_vccf/Region_52.png" alt="region52" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_52.html" >new window.</a>
    </div>
    <div id="region53" class="tab-pane fade">
      <h3>Region 53</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_53.html" >
      <img src="../../images_vccf/Region_53.png" alt="region53" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_53.html" >new window.</a>
    </div>
    <div id="region54" class="tab-pane fade">
      <h3>Region 54</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_54.html" >
      <img src="../../images_vccf/Region_54.png" alt="region54" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_54.html" >new window.</a>
    </div>
    <div id="region55" class="tab-pane fade">
      <h3>Region 55</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_55.html" >
      <img src="../../images_vccf/Region_55.png" alt="region55" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_55.html" >new window.</a>
    </div>
    <div id="region56" class="tab-pane fade">
      <h3>Region 56</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_56.html" >
      <img src="../../images_vccf/Region_56.png" alt="region56" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_56.html" >new window.</a>
    </div>
    <div id="region57" class="tab-pane fade">
      <h3>Region 57</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_57.html" >
      <img src="../../images_vccf/Region_57.png" alt="region57" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_57.html" >new window.</a>
    </div>
    <div id="region58" class="tab-pane fade">
      <h3>Region 58</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_58.html" >
      <img src="../../images_vccf/Region_58.png" alt="region58" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_58.html" >new window.</a>
    </div>
    <div id="region59" class="tab-pane fade">
      <h3>Region 59</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_59.html" >
      <img src="../../images_vccf/Region_59.png" alt="region59" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_59.html" >new window.</a>
    </div>
    <div id="region60" class="tab-pane fade">
      <h3>Region 60</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_60.html" >
      <img src="../../images_vccf/Region_60.png" alt="region60" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_60.html" >new window.</a>
    </div>
    <div id="region61" class="tab-pane fade">
      <h3>Region 61</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_61.html" >
      <img src="../../images_vccf/Region_61.png" alt="region61" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_61.html" >new window.</a>
    </div>
    <div id="region62" class="tab-pane fade">
      <h3>Region 62</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_62.html" >
      <img src="../../images_vccf/Region_62.png" alt="region62" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_62.html" >new window.</a>
    </div>
    <div id="region63" class="tab-pane fade">
      <h3>Region 63</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_63.html" >
      <img src="../../images_vccf/Region_63.png" alt="region63" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_63.html" >new window.</a>
    </div>
    <div id="region64" class="tab-pane fade">
      <h3>Region 64</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_64.html" >
      <img src="../../images_vccf/Region_64.png" alt="region64" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-vccf-cell-distance-visualizations/html_vccf/region_64.html" >new window.</a>
    </div>


</div>
