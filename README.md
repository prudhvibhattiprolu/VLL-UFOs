# Vectorlike-leptons

This repository has FeynRules and Madgraph (i.e. UFO) model files for vectorlike leptons

## Files  
**FeynRules model files in `FeynRulesfiles` folder:**

Doublet VLL model: `VLLD.fr`

Singlet VLL model: `VLLS.fr`

To obtain UFO (Universal FeynRules Output) files, can run FeynRulesfiles/*.nb Mathematica notebook files (edit the paths to FeynRules, FeynArts and NLOCT packages before running .nb files).

**UFO model files in `MG5UFOs` folder (generated using FeynRules, MadGraph-compatible):**

Doublet VLL model: `VLLD_NLO`

Singlet VLL model: `VLLS_NLO`

## Importing UFO model file into MadGraph:

**Before importing into MadGraph, the UFO model files should be moved to `<path to MadGraph>/models/`**

    MG5_aMC> import model XYZ
**XYZ = `VLLD_NLO` or `VLLS_NLO`**

## Model information

In these VLL models,

#### Particles:

`taup` : charged VLL (in both models)
`taup~` : its anti-particle

`nup` : neutral VLL (only in VLLD_NLO)
`nup~` : its anti-particle

#### Masses:

`MTAUP` : mass of **taup** particle
`MNUP` : mass of **nup** particle

#### Widths:
`WTAUP` : width of taup
`WNUP` : width of nup

**Note: These widths are set to 1 GeV. This should not matter if one forces the decay of these particles while generating events (see below).**

## Pair-production of VLLs (LO cross-sections and LO event generation)

### Computing cross-sections at LO:

#### Doublet VLL

**For p p -> taup taup:**

    MG5_aMC> generate p p > taup taup~

**For p p -> taup nup:**

    MG5_aMC> generate p p > taup nup~
    MG5_aMC> add process p p > taup~ nup

**For p p -> nup nup:**

    MG5_aMC> generate p p > nup nup~

#### Singlet VLL

**For p p -> taup taup:**

    MG5_aMC> generate p p > taup taup~

  

#### Running MADGRAPH from a script to compute cross-sections:

One can calculate cross-sections using MADGRAPH from a script by doing:

    $ <path to MADGRAPH>/bin/mg5_aMC script

Below is an example MadGraph-script to calculate LO production cross-section for p p > taup nup, at 13 TeV LHC, in the Doublet VLL model for MTAUP = MNUP = 100, 200, 300, .., 1000 GeV using MSTW2008nlo68cl PDFs (lhaid: 21100) with factorization scale = 200 GeV.

    ###script###
    import model VLLD_NLO
    generate p p > taup nup~
    add process p p > taup~ nup
    output dvll_tpnp
    launch dvll_tpnp
    shower=off
    detector=off
    analysis=off
    done
    #set iseed=1000
    set nevents 10000
    set ebeam1 6500
    set ebeam2 6500
    #CHANGE SCALES HERE
    set fixed_ren_scale=True
    set fixed_fac_scale=True
    set scale=200
    set dsqrt_q2fact1=200
    set dsqrt_q2fact2=200
    #CHANGE PDF SET HERE
    set pdlabel = lhapdf
    set lhaid = 21100
    #SYNCHRONIZED SCAN OVER MULTIPLE PARAMETERS CAN BE DONE USING *_scan1_* (INSTEAD OF *_scan_*)
    set mtaup scan1:range(100,1100,100)
    set mnup scan1:range(100,1100,100)
    done

**Note: By default MadGraph sets `fixed_ren_scale` and `fixed_fac_scale` to `False` (i.e. *dynamic* scale choice). They should be set to `True` to use *fixed* scales.**

**Also, by default MadGraph sets `pdlabel` to `nn23lo1` (MadGraph's default PDFs based on NNPDF2.3 set) for LO calculations. `pdlabel` should be set to `lhapdf` to gain access to many other PDFs with `lhaid` listed in https://lhapdf.hepforge.org/pdfsets.html**

### Generating events at LO:

**Note: For event generation, one should force *taup -> Z ta or h ta* and *nup -> W ta* (in the Doublet VLL model) or *taup -> Z ta or h ta or W vt* (in the Singlet VLL model)**


In the following, only the decay of higgs into W+W−, ZZ, and ta+ta- final states are considered (ignoring all other higgs decay channels).

(Below "zz", "zhww",... etc. are names given to signal components)

#### Doublet VLL

    ## Multiparticle definitions in MADGRAPH ##
    p = g u c d s u~ c~ d~ s~
    j = g u c d s u~ c~ d~ s~
    l+ = e+ mu+
    l- = e- mu-
    vl = ve vm vt
    vl~ = ve~ vm~ vt~
    lep+ = e+ mu+ ta+
    lep- = e- mu- ta-
    lep = e- mu- e+ mu+ ta- ta+
    w = w+ w-
    ferm = u u~ d d~ s s~ c c~ b b~ lep+ lep- vl vl~
    vlep = ve vm vt ve~ vm~ vt~
    vll = taup taup~ nup nup~
    vllferm = vll ferm
    all = g a ve vm vt ve~ vm~ vt~ u c t d s b u~ c~ t~ d~ s~ b~ z w+ h w- e- mu- ta- taup nup e+ mu+ ta+ taup~ nup~

1. **zz** : taup+ taup- (both taup's  are forced to z tau)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > z ta+)
        
cross-section =  sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > z tau)

2. **zhww** : taup+ taup- (one taup > z tau, other taup > h tau, where h > w+ w-)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > h ta+, h > w ferm ferm / vllferm)

cross-section =  2*sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > h tau)*BR(h > ww)

3. **zhzz** : taup+ taup- (one taup > z tau, other taup > h tau, where h > z z)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > h ta+, h > z ferm ferm / vllferm)

cross-section =  2*sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > h tau)*BR(h > zz)

4. **zhtata** : taup+ taup- (one taup > z tau, other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > h ta+, h > ta+ ta-)

cross-section =  2*sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > h tau)*BR(h > tau tau)

5. **hhwwww** : taup+ taup- (one taup > h tau, where h > w+ w-; other taup > h tau, where h > w+ w-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > w ferm ferm / vllferm), (taup~ > h ta+, h > w ferm ferm / vllferm)

cross-section =  sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > ww)*BR(h > ww)

6. **hhwwzz** : taup+ taup- (one taup > h tau, where h > w+ w-; other taup > h tau, where h > z z)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > w ferm ferm / vllferm), (taup~ > h ta+, h > z ferm ferm / vllferm)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > ww)*BR(h > zz)

7. **hhwwtata** : taup+ taup- (one taup > h tau, where h > w+ w-; other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > w ferm ferm / vllferm), (taup~ > h ta+, h > ta+ ta-)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > ww)*BR(h > tau tau)

8. **hhzzzz** : taup+ taup- (one taup > h tau, where h > z z; other taup > h tau, where h > z z)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > z ferm ferm / vllferm), (taup~ > h ta+, h > z ferm ferm / vllferm)

cross-section =  sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > zz)*BR(h > zz)

9. **hhzztata** : taup+ taup- (one taup > h tau, where h > z z; other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > z ferm ferm / vllferm), (taup~ > h ta+, h > ta+ ta-)
        
cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > zz)*BR(h > tau tau)

10. **hhtatatata** : taup+ taup- (one taup > h tau, where h > ta+ ta-; other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > ta+ ta-), (taup~ > h ta+, h > ta+ ta-)

cross-section =  sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > tau tau)*BR(h > tau tau)

11. **zw** : taup nup (taup > z tau, nup > w tau)

        MG5_aMC> generate p p > taup nup~, (taup > z ta-), (nup~ > w- ta+)
        MG5_aMC> add process p p > taup~ nup, (taup~ > z ta+), (nup > w+ ta-)

cross-section =  sigma(pp > taup nup)*BR(taup > z tau)

12. **hwww** : taup nup (taup > h tau, h > w+ w- ; nup > w tau)

        MG5_aMC> generate p p > taup nup~, (taup > h ta-, h > w ferm ferm / vllferm), (nup~ > w- ta+)
        MG5_aMC> add process p p > taup~ nup, (taup~ > h ta+, h > w ferm ferm / vllferm), (nup > w+ ta-)

cross-section =  sigma(pp > taup nup)*BR(taup > h tau)*BR(h > ww)

13. **hwzz** : taup nup (taup > h tau, h > z z ; nup > w tau)

        MG5_aMC> generate p p > taup nup~, (taup > h ta-, h > z ferm ferm / vllferm), (nup~ > w- ta+)
        MG5_aMC> add process p p > taup~ nup, (taup~ > h ta+, h > z ferm ferm / vllferm), (nup > w+ ta-)

cross-section =  sigma(pp > taup nup)*BR(taup > h tau)*BR(h > zz)

14. **hwtata** : taup nup (taup > h tau, h > ta+ ta- ; nup > w tau)

        MG5_aMC> generate p p > taup nup~, (taup > h ta-, h > ta+ ta-), (nup~ > w- ta+)
        MG5_aMC> add process p p > taup~ nup, (taup~ > h ta+, h > ta+ ta-), (nup > w+ ta-)

cross-section =  sigma(pp > taup nup)*BR(taup > h tau)*BR(h > tau tau)

15. **ww** : nup nup (both nup's  are forced to w tau)

        MG5_aMC> generate p p > nup nup~, (nup > w+ ta-), (nup~ > w- ta+)

cross-section =  sigma(pp > nup nup)

#### Singlet VLL

1. **zz** : taup+ taup- (both taup's  are forced to z tau)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > z ta+)

cross-section =  sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > z tau)

2. **zhww** : taup+ taup- (one taup > z tau, other taup > h tau, where h > w+ w-)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > h ta+, h > w ferm ferm / vllferm)

cross-section =  2*sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > h tau)*BR(h > ww)

3. **zhzz** : taup+ taup- (one taup > z tau, other taup > h tau, where h > z z)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > h ta+, h > z ferm ferm / vllferm)

cross-section =  2*sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > h tau)*BR(h > zz)

4. **zhtata** : taup+ taup- (one taup > z tau, other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > h ta+, h > ta+ ta-)

cross-section =  2*sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > h tau)*BR(h > tau tau)

5. **hhwwww** : taup+ taup- (one taup > h tau, where h > w+ w-; other taup > h tau, where h > w+ w-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > w ferm ferm / vllferm), (taup~ > h ta+, h > w ferm ferm / vllferm)

cross-section =  sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > ww)*BR(h > ww)

6. **hhwwzz** : taup+ taup- (one taup > h tau, where h > w+ w-; other taup > h tau, where h > z z)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > w ferm ferm / vllferm), (taup~ > h ta+, h > z ferm ferm / vllferm)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > ww)*BR(h > zz)

7. **hhwwtata** : taup+ taup- (one taup > h tau, where h > w+ w-; other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > w ferm ferm / vllferm), (taup~ > h ta+, h > ta+ ta-)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > ww)*BR(h > tau tau)

8. **hhzzzz** : taup+ taup- (one taup > h tau, where h > z z; other taup > h tau, where h > z z)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > z ferm ferm / vllferm), (taup~ > h ta+, h > z ferm ferm / vllferm)

cross-section =  sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > zz)*BR(h > zz)

9. **hhzztata** : taup+ taup- (one taup > h tau, where h > z z; other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > z ferm ferm / vllferm), (taup~ > h ta+, h > ta+ ta-)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > zz)*BR(h > tau tau)

10. **hhtatatata** : taup+ taup- (one taup > h tau, where h > ta+ ta-; other taup > h tau, where h > ta+ ta-)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > ta+ ta-), (taup~ > h ta+, h > ta+ ta-)

cross-section =  sigma(pp > taup taup)*BR(taup > h tau)*BR(taup > h tau)*BR(h > tau tau)*BR(h > tau tau)

11. **zw** : taup taup (taup > z tau, taup > w vtau)

        MG5_aMC> generate p p > taup taup~, (taup > z ta-), (taup~ > w+ vt~)
        MG5_aMC> add process p p > taup taup~, (taup > w- vt), (taup~ > z ta+)

cross-section =  2*sigma(pp > taup taup)*BR(taup > z tau)*BR(taup > w vtau)

12. **hwww** : taup taup (taup > h tau, h > w+ w- ; taup > w vtau)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > w ferm ferm / vllferm), (taup~ > w+ vt~)
        MG5_aMC> add process p p > taup~ taup, (taup~ > h ta+, h > w ferm ferm / vllferm), (taup > w- vt)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(h > ww)*BR(taup > w vtau)

13. **hwzz** : taup taup (taup > h tau, h > z z ; taup > w vtau)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > z ferm ferm / vllferm), (taup~ > w+ vt~)
        MG5_aMC> add process p p > taup~ taup, (taup~ > h ta+, h > z ferm ferm / vllferm), (taup > w- vt)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(h > zz)*BR(taup > w vtau)

14. **hwtata** : taup taup (taup > h tau, h > ta+ ta- ; taup > w vtau)

        MG5_aMC> generate p p > taup taup~, (taup > h ta-, h > ta+ ta-), (taup~ > w+ vt~)
        MG5_aMC> add process p p > taup~ taup, (taup~ > h ta+, h > ta+ ta-), (taup > w- vt)

cross-section =  2*sigma(pp > taup taup)*BR(taup > h tau)*BR(h > tau tau)*BR(taup > w vtau)

15. **ww** : taup taup (both taup's  are forced to w vtau)

        MG5_aMC> generate p p > taup taup~, (taup > w- vt), (taup~ > w+ vt~)

cross-section =  sigma(pp > taup taup)*BR(taup > w vtau)*BR(taup > w vtau)
