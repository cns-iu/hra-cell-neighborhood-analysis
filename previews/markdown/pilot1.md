#  Preview: Vasculature CCF Visualization for Intestine Data

HuBMAP Atlas Previews demonstrate functionality and resources that will become available in future HuBMAP portal releases. Previews may rely on externally hosted data or analysis results that were generated with processing pipelines that are not yet integrated into the HuBMAP data infrastructure.


### Description

This preview showcases a novel visualization in support of a vasculature-based common coordinate system (VCCF), see paper on “[Considerations for Using the Vasculature as a Coordinate System to Map All the Cells in the Human Body](https://doi.org/10.3389/fcvm.2020.00029)”.

Experimental data from the “[High Resolution Single Cell Maps Reveals Distinct Cell Organization and Function Across Different Regions of the Human Intestine](https://www.biorxiv.org/content/early/2021/11/25/2021.11.25.469203)” paper, is used to compute distances of different cell types to the nearest blood vessel using 2D volumes of digital intestine biopsy data generated using multiplexed imaging on 64 sections of the human intestine (~16 mm2) from 8 donors (B004, B005, B006, B008, B009, B010, B011, and B012) using a panel of 57 oligonucleotide-barcoded antibodies. Subsequently, images underwent standard CODEX image processing (tile stitching, drift compensation, cycle concatenation, background subtraction, deconvolution, and determination of best focal plane), single cell segmentation, and column marker z-normalization by tissue. The outputs of this process were data frames of 2.6 million cells with 57 antibody fluorescence values quantified from each marker. Each cell has its cell type, cellular neighborhood, community of neighborhooods, and tissue unit defined with x, y coordinates representing pixel location in the original image. This data was taken from  8 donors with 8 individual tissue Regions (64 tissues imaged) across 2.6 million cells, with 25 cell types, 20 multicellular neighborhoods, 10 communities of neighborhoods, and 3 tissue segments could be used to understand the cellular interactions, composition, and structure of the human intestine from the duodenum to the sigmoid colon and understand differences between different areas of the intestine. 


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
    <li class="active"><a data-toggle="tab" href="#Region1">Region 1</a></li>
    <li><a data-toggle="tab" href="#Region2">Region 2</a></li>
    <li><a data-toggle="tab" href="#Region3">Region 3</a></li>
    <li><a data-toggle="tab" href="#Region4">Region 4</a></li>
    <li><a data-toggle="tab" href="#Region5">Region 5</a></li>
    <li><a data-toggle="tab" href="#Region6">Region 6</a></li>
    <li><a data-toggle="tab" href="#Region7">Region 7</a></li>
    <li><a data-toggle="tab" href="#Region8">Region 8</a></li>
    <li><a data-toggle="tab" href="#Region9">Region 9</a></li>
    <li><a data-toggle="tab" href="#Region10">Region 10</a></li>
    <li><a data-toggle="tab" href="#Region11">Region 11</a></li>
    <li><a data-toggle="tab" href="#Region12">Region 12</a></li>
    <li><a data-toggle="tab" href="#Region13">Region 13</a></li>
    <li><a data-toggle="tab" href="#Region14">Region 14</a></li>
    <li><a data-toggle="tab" href="#Region15">Region 15</a></li>
    <li><a data-toggle="tab" href="#Region16">Region 16</a></li>
    <li><a data-toggle="tab" href="#Region17">Region 17</a></li>
    <li><a data-toggle="tab" href="#Region18">Region 18</a></li>
    <li><a data-toggle="tab" href="#Region19">Region 19</a></li>
    <li><a data-toggle="tab" href="#Region20">Region 20</a></li>
    <li><a data-toggle="tab" href="#Region21">Region 21</a></li>
    <li><a data-toggle="tab" href="#Region22">Region 22</a></li>
    <li><a data-toggle="tab" href="#Region23">Region 23</a></li>
    <li><a data-toggle="tab" href="#Region24">Region 24</a></li>
    <li><a data-toggle="tab" href="#Region25">Region 25</a></li>
    <li><a data-toggle="tab" href="#Region26">Region 26</a></li>
    <li><a data-toggle="tab" href="#Region27">Region 27</a></li>
    <li><a data-toggle="tab" href="#Region28">Region 28</a></li>
    <li><a data-toggle="tab" href="#Region29">Region 29</a></li>
    <li><a data-toggle="tab" href="#Region30">Region 30</a></li>
    <li><a data-toggle="tab" href="#Region31">Region 31</a></li>
    <li><a data-toggle="tab" href="#Region32">Region 32</a></li>
    <li><a data-toggle="tab" href="#Region33">Region 33</a></li>
    <li><a data-toggle="tab" href="#Region34">Region 34</a></li>
    <li><a data-toggle="tab" href="#Region35">Region 35</a></li>
    <li><a data-toggle="tab" href="#Region36">Region 36</a></li>
    <li><a data-toggle="tab" href="#Region37">Region 37</a></li>
    <li><a data-toggle="tab" href="#Region38">Region 38</a></li>
    <li><a data-toggle="tab" href="#Region39">Region 39</a></li>
    <li><a data-toggle="tab" href="#Region40">Region 40</a></li>
    <li><a data-toggle="tab" href="#Region41">Region 41</a></li>
    <li><a data-toggle="tab" href="#Region42">Region 42</a></li>
    <li><a data-toggle="tab" href="#Region43">Region 43</a></li>
    <li><a data-toggle="tab" href="#Region44">Region 44</a></li>
    <li><a data-toggle="tab" href="#Region45">Region 45</a></li>
    <li><a data-toggle="tab" href="#Region46">Region 46</a></li>
    <li><a data-toggle="tab" href="#Region47">Region 47</a></li>
    <li><a data-toggle="tab" href="#Region48">Region 48</a></li>
    <li><a data-toggle="tab" href="#Region49">Region 49</a></li>
    <li><a data-toggle="tab" href="#Region50">Region 50</a></li>
    <li><a data-toggle="tab" href="#Region51">Region 51</a></li>
    <li><a data-toggle="tab" href="#Region52">Region 52</a></li>
    <li><a data-toggle="tab" href="#Region53">Region 53</a></li>
    <li><a data-toggle="tab" href="#Region54">Region 54</a></li>
    <li><a data-toggle="tab" href="#Region55">Region 55</a></li>
    <li><a data-toggle="tab" href="#Region56">Region 56</a></li>
    <li><a data-toggle="tab" href="#Region57">Region 57</a></li>
    <li><a data-toggle="tab" href="#Region58">Region 58</a></li>
    <li><a data-toggle="tab" href="#Region59">Region 59</a></li>
    <li><a data-toggle="tab" href="#Region61">Region 60</a></li>
    <li><a data-toggle="tab" href="#Region61">Region 61</a></li>
    <li><a data-toggle="tab" href="#Region62">Region 62</a></li>
    <li><a data-toggle="tab" href="#Region63">Region 63</a></li>
    <li><a data-toggle="tab" href="#Region64">Region 64</a></li>

  </ul>

  
  <div class="tab-content">
    <div id="Region1" class="tab-pane fade in active">
      <h3>Region 1</h3>
      <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_1.png" >
      <img src=".../../viz_low_res/Region_1.png" alt="Region1" style="width:100%">
        </a>
      <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_1.png" >new window.</a>  
    </div>
    <div id="Region2" class="tab-pane fade">
      <h3>Region 2</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_2.png" >
      <img src=".../../viz_low_res/Region_2.png" alt="Region2" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_2.png" >new window.</a>
  </div>
    <div id="Region3" class="tab-pane fade">
      <h3>Region 3</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_3.png" >
      <img src=".../../viz_low_res/Region_3.png" alt="Region3" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_3.png" >new window.</a>
    </div>
    <div id="Region4" class="tab-pane fade">
      <h3>Region 4</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_4.png" >
      <img src=".../../viz_low_res/Region_4.png" alt="Region4" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_4.png" >new window.</a>
    </div>
    <div id="Region5" class="tab-pane fade">
      <h3>Region 5</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_5.png" >
      <img src=".../../viz_low_res/Region_5.png" alt="Region5" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_5.png" >new window.</a>
    </div>
    <div id="Region6" class="tab-pane fade">
      <h3>Region 6</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_6.png" >
      <img src=".../../viz_low_res/Region_6.png" alt="Region6" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_6.png" >new window.</a>
    </div>
    <div id="Region7" class="tab-pane fade">
      <h3>Region 7</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_7.png" >
      <img src=".../../viz_low_res/Region_7.png" alt="Region7" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_7.png" >new window.</a>
    </div>
    <div id="Region8" class="tab-pane fade">
      <h3>Region 8</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_8.png" >
      <img src=".../../viz_low_res/Region_8.png" alt="Region8" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_8.png" >new window.</a>
    </div>
    <div id="Region9" class="tab-pane fade">
      <h3>Region 9</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_9.png" >
      <img src=".../../viz_low_res/Region_9.png" alt="Region9" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_9.png" >new window.</a>
    </div>
    <div id="Region10" class="tab-pane fade">
      <h3>Region 10</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_10.png" >
      <img src=".../../viz_low_res/Region_10.png" alt="Region10" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_10.png" >new window.</a>
    </div>
    <div id="Region11" class="tab-pane fade">
      <h3>Region 11</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_11.png" >
      <img src=".../../viz_low_res/Region_11.png" alt="Region11" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_11.png" >new window.</a>
    </div>
    <div id="Region12" class="tab-pane fade">
      <h3>Region 12</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_12.png" >
      <img src=".../../viz_low_res/Region_12.png" alt="Region12" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_12.png" >new window.</a>
    </div>
    <div id="Region13" class="tab-pane fade">
      <h3>Region 13</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_13.png" >
      <img src=".../../viz_low_res/Region_13.png" alt="Region13" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_13.png" >new window.</a>
    </div>
    <div id="Region14" class="tab-pane fade">
      <h3>Region 14</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_14.png" >
      <img src=".../../viz_low_res/Region_14.png" alt="Region14" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_14.png" >new window.</a>
    </div>
    <div id="Region15" class="tab-pane fade">
      <h3>Region 15</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_15.png" >
      <img src=".../../viz_low_res/Region_15.png" alt="Region15" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_15.png" >new window.</a>
    </div>
    <div id="Region16" class="tab-pane fade">
      <h3>Region 16</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_16.png" >
      <img src=".../../viz_low_res/Region_16.png" alt="Region16" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_16.png" >new window.</a>
    </div>
    <div id="Region17" class="tab-pane fade">
      <h3>Region 17</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_17.png" >
      <img src=".../../viz_low_res/Region_17.png" alt="Region17" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_17.png" >new window.</a>
    </div>
    <div id="Region18" class="tab-pane fade">
      <h3>Region 18</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_18.png" >
      <img src=".../../viz_low_res/Region_18.png" alt="Region18" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_18.png" >new window.</a>
    </div>
    <div id="Region19" class="tab-pane fade">
      <h3>Region 19</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_19.png" >
      <img src=".../../viz_low_res/Region_19.png" alt="Region19" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_19.png" >new window.</a>
    </div>
    <div id="Region20" class="tab-pane fade">
      <h3>Region 20</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_20.png" >
      <img src=".../../viz_low_res/Region_20.png" alt="Region20" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_20.png" >new window.</a>
    </div>
    <div id="Region21" class="tab-pane fade">
      <h3>Region 21</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_21.png" >
      <img src=".../../viz_low_res/Region_21.png" alt="Region21" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_21.png" >new window.</a>
    </div>
    <div id="Region22" class="tab-pane fade">
      <h3>Region 22</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_22.png" >
      <img src=".../../viz_low_res/Region_22.png" alt="Region22" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_22.png" >new window.</a>
    </div>
    <div id="Region23" class="tab-pane fade">
      <h3>Region 23</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_23.png" >
      <img src=".../../viz_low_res/Region_23.png" alt="Region23" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_23.png" >new window.</a>
    </div>
    <div id="Region24" class="tab-pane fade">
      <h3>Region 24</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_24.png" >
      <img src=".../../viz_low_res/Region_24.png" alt="Region24" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_24.png" >new window.</a>
    </div>
    <div id="Region25" class="tab-pane fade">
      <h3>Region 25</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_25.png" >
      <img src=".../../viz_low_res/Region_25.png" alt="Region25" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_25.png" >new window.</a>
    </div>
    <div id="Region26" class="tab-pane fade">
      <h3>Region 26</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_26.png" >
      <img src=".../../viz_low_res/Region_26.png" alt="Region26" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_26.png" >new window.</a>
    </div>
    <div id="Region27" class="tab-pane fade">
      <h3>Region 27</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_27.png" >
      <img src=".../../viz_low_res/Region_27.png" alt="Region27" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_27.png" >new window.</a>
    </div>
    <div id="Region28" class="tab-pane fade">
      <h3>Region 28</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_28.png" >
      <img src=".../../viz_low_res/Region_28.png" alt="Region28" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_28.png" >new window.</a>
    </div>
    <div id="Region29" class="tab-pane fade">
      <h3>Region 29</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_29.png" >
      <img src=".../../viz_low_res/Region_29.png" alt="Region29" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_29.png" >new window.</a>
    </div>
    <div id="Region30" class="tab-pane fade">
      <h3>Region 30</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_30.png" >
      <img src=".../../viz_low_res/Region_30.png" alt="Region30" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_30.png" >new window.</a>
    </div>
    <div id="Region31" class="tab-pane fade">
      <h3>Region 31</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_31.png" >
      <img src=".../../viz_low_res/Region_31.png" alt="Region31" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_31.png" >new window.</a>
    </div>
    <div id="Region32" class="tab-pane fade">
      <h3>Region 32</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_32.png" >
      <img src=".../../viz_low_res/Region_32.png" alt="Region32" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_32.png" >new window.</a>
    </div>
    <div id="Region33" class="tab-pane fade">
      <h3>Region 33</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_33.png" >
      <img src=".../../viz_low_res/Region_33.png" alt="Region33" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_33.png" >new window.</a>
    </div>
    <div id="Region34" class="tab-pane fade">
      <h3>Region 34</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_34.png" >
      <img src=".../../viz_low_res/Region_34.png" alt="Region34" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_34.png" >new window.</a>
    </div>
    <div id="Region35" class="tab-pane fade">
      <h3>Region 35</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_35.png" >
      <img src=".../../viz_low_res/Region_35.png" alt="Region35" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_35.png" >new window.</a>
    </div>
    <div id="Region36" class="tab-pane fade">
      <h3>Region 36</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_36.png" >
      <img src=".../../viz_low_res/Region_36.png" alt="Region36" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_36.png" >new window.</a>
    </div>
    <div id="Region37" class="tab-pane fade">
      <h3>Region 37</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_37.png" >
      <img src=".../../viz_low_res/Region_37.png" alt="Region37" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_37.png" >new window.</a>
    </div>
    <div id="Region38" class="tab-pane fade">
      <h3>Region 38</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_38.png" >
      <img src=".../../viz_low_res/Region_38.png" alt="Region38" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_38.png" >new window.</a>
    </div>
    <div id="Region39" class="tab-pane fade">
      <h3>Region 39</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_39.png" >
      <img src=".../../viz_low_res/Region_39.png" alt="Region39" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_39.png" >new window.</a>
    </div>
    <div id="Region40" class="tab-pane fade">
      <h3>Region 40</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_40.png" >
      <img src=".../../viz_low_res/Region_40.png" alt="Region40" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_40.png" >new window.</a>
    </div>
    <div id="Region41" class="tab-pane fade">
      <h3>Region 41</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_41.png" >
      <img src=".../../viz_low_res/Region_41.png" alt="Region41" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_41.png" >new window.</a>
    </div>
    <div id="Region42" class="tab-pane fade">
      <h3>Region 42</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_42.png" >
      <img src=".../../viz_low_res/Region_42.png" alt="Region42" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_42.png" >new window.</a>
    </div>
    <div id="Region43" class="tab-pane fade">
      <h3>Region 43</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_43.png" >
      <img src=".../../viz_low_res/Region_43.png" alt="Region43" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_43.png" >new window.</a>
    </div>
    <div id="Region44" class="tab-pane fade">
      <h3>Region 44</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_44.png" >
      <img src=".../../viz_low_res/Region_44.png" alt="Region44" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_44.png" >new window.</a>
    </div>
    <div id="Region45" class="tab-pane fade">
      <h3>Region 45</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_45.png" >
      <img src=".../../viz_low_res/Region_45.png" alt="Region45" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_45.png" >new window.</a>
    </div>
    <div id="Region46" class="tab-pane fade">
      <h3>Region 46</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_46.png" >
      <img src=".../../viz_low_res/Region_46.png" alt="Region46" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_46.png" >new window.</a>
    </div>
    <div id="Region47" class="tab-pane fade">
      <h3>Region 47</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_47.png" >
      <img src=".../../viz_low_res/Region_47.png" alt="Region47" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_47.png" >new window.</a>
    </div>
    <div id="Region48" class="tab-pane fade">
      <h3>Region 48</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_48.png" >
      <img src=".../../viz_low_res/Region_48.png" alt="Region48" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_48.png" >new window.</a>
    </div>
    <div id="Region49" class="tab-pane fade">
      <h3>Region 49</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_49.png" >
      <img src=".../../viz_low_res/Region_49.png" alt="Region49" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_49.png" >new window.</a>
    </div>
    <div id="Region50" class="tab-pane fade">
      <h3>Region 50</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_50.png" >
      <img src=".../../viz_low_res/Region_50.png" alt="Region50" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_50.png" >new window.</a>
    </div>
    <div id="Region51" class="tab-pane fade">
      <h3>Region 51</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_51.png" >
      <img src=".../../viz_low_res/Region_51.png" alt="Region51" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_51.png" >new window.</a>
    </div>
    <div id="Region52" class="tab-pane fade">
      <h3>Region 52</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_52.png" >
      <img src=".../../viz_low_res/Region_52.png" alt="Region52" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_52.png" >new window.</a>
    </div>
    <div id="Region53" class="tab-pane fade">
      <h3>Region 53</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_53.png" >
      <img src=".../../viz_low_res/Region_53.png" alt="Region53" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_53.png" >new window.</a>
    </div>
    <div id="Region54" class="tab-pane fade">
      <h3>Region 54</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_54.png" >
      <img src=".../../viz_low_res/Region_54.png" alt="Region54" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_54.png" >new window.</a>
    </div>
    <div id="Region55" class="tab-pane fade">
      <h3>Region 55</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_55.png" >
      <img src=".../../viz_low_res/Region_55.png" alt="Region55" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_55.png" >new window.</a>
    </div>
    <div id="Region56" class="tab-pane fade">
      <h3>Region 56</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_56.png" >
      <img src=".../../viz_low_res/Region_56.png" alt="Region56" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_56.png" >new window.</a>
    </div>
    <div id="Region57" class="tab-pane fade">
      <h3>Region 57</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_57.png" >
      <img src=".../../viz_low_res/Region_57.png" alt="Region57" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_57.png" >new window.</a>
    </div>
    <div id="Region58" class="tab-pane fade">
      <h3>Region 58</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_58.png" >
      <img src=".../../viz_low_res/Region_58.png" alt="Region58" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_58.png" >new window.</a>
    </div>
    <div id="Region59" class="tab-pane fade">
      <h3>Region 59</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_59.png" >
      <img src=".../../viz_low_res/Region_59.png" alt="Region59" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_59.png" >new window.</a>
    </div>
    <div id="Region60" class="tab-pane fade">
      <h3>Region 60</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_60.png" >
      <img src=".../../viz_low_res/Region_60.png" alt="Region60" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_60.png" >new window.</a>
    </div>
    <div id="Region61" class="tab-pane fade">
      <h3>Region 61</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_61.png" >
      <img src=".../../viz_low_res/Region_61.png" alt="Region61" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_61.png" >new window.</a>
    </div>
    <div id="Region62" class="tab-pane fade">
      <h3>Region 62</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_62.png" >
      <img src=".../../viz_low_res/Region_62.png" alt="Region62" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_62.png" >new window.</a>
    </div>
    <div id="Region63" class="tab-pane fade">
      <h3>Region 63</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_63.png" >
      <img src=".../../viz_low_res/Region_63.png" alt="Region63" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_63.png" >new window.</a>
    </div>
    <div id="Region64" class="tab-pane fade">
      <h3>Region 64</h3>
        <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_64.png" >
      <img src=".../../viz_low_res/Region_64.png" alt="Region64" style="width:100%">
        </a>
        <p> Open the visualization in <a target="_blank" href="https://cns-iu.github.io/hra-cell-neighborhood-analysis/viz/Region_64.png" >new window.</a>
    </div>


</div>
</div>