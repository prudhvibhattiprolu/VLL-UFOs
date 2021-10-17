# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Mac OS X x86 (64-bit) (April 7, 2019)
# Date: Sun 17 Oct 2021 14:01:13



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# This is a default parameter object representing the renormalization scale (MU_R).
MU_R = Parameter(name = 'MU_R',
                 nature = 'external',
                 type = 'real',
                 value = 91.188,
                 texname = '\\text{\\mu_r}',
                 lhablock = 'LOOP',
                 lhacode = [1])

# User-defined parameters.
epstaupeR = Parameter(name = 'epstaupeR',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{epstaupeR}',
                      lhablock = 'Couplings',
                      lhacode = [ 1 ])

epstaupmuR = Parameter(name = 'epstaupmuR',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{epstaupmuR}',
                       lhablock = 'Couplings',
                       lhacode = [ 2 ])

epstauptaR = Parameter(name = 'epstauptaR',
                       nature = 'external',
                       type = 'real',
                       value = 0.1,
                       texname = '\\text{epstauptaR}',
                       lhablock = 'Couplings',
                       lhacode = [ 3 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.952,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663787,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1179,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.76,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.76,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.1,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MTAUP = Parameter(name = 'MTAUP',
                  nature = 'external',
                  type = 'real',
                  value = 300,
                  texname = '\\text{MTAUP}',
                  lhablock = 'MASS',
                  lhacode = [ 17 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.42,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00417,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

MNUP = Parameter(name = 'MNUP',
                 nature = 'internal',
                 type = 'real',
                 value = 'MTAUP',
                 texname = '\\text{MNUP}')

Tl = Parameter(name = 'Tl',
               nature = 'internal',
               type = 'real',
               value = '-0.5',
               texname = '\\text{Tl}')

WTAUP = Parameter(name = 'WTAUP',
                  nature = 'internal',
                  type = 'real',
                  value = '((epstaupeR**2 + epstaupmuR**2 + epstauptaR**2)*MTAUP*((1 - MH**2/MTAUP**2)**2 + (1 - MZ**2/MTAUP**2)**2*(1 + (2*MZ**2)/MTAUP**2)))/(64.*cmath.pi)',
                  texname = '\\text{WTAUP}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

WNUP = Parameter(name = 'WNUP',
                 nature = 'internal',
                 type = 'real',
                 value = '((epstaupeR**2 + epstaupmuR**2 + epstauptaR**2)*MNUP*(1 - MW**2/MTAUP**2)**2*(1 + (2*MW**2)/MTAUP**2))/(32.*cmath.pi)',
                 texname = '\\text{WNUP}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

gnupb = Parameter(name = 'gnupb',
                  nature = 'internal',
                  type = 'real',
                  value = 'g1*Tl',
                  texname = '\\text{gnupb}')

gtaupb = Parameter(name = 'gtaupb',
                   nature = 'internal',
                   type = 'real',
                   value = 'g1*(-1 - Tl)',
                   texname = '\\text{gtaupb}')

gtaupnupw3 = Parameter(name = 'gtaupnupw3',
                       nature = 'internal',
                       type = 'real',
                       value = 'gw*Tl',
                       texname = '\\text{gtaupnupw3}')

gwtaupnup = Parameter(name = 'gwtaupnup',
                      nature = 'internal',
                      type = 'real',
                      value = '-(gw*Tl*cmath.sqrt(2))',
                      texname = '\\text{gwtaupnup}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I2a33}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I3a33}')

