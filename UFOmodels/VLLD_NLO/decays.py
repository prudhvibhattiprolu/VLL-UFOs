# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Mac OS X x86 (64-bit) (April 7, 2019)
# Date: Sun 17 Oct 2021 14:01:14


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.e__minus__,P.taup__tilde__):'((MH**2 - MTAUP**2)*((epstaupeR**2*MH**2)/2. - (epstaupeR**2*MTAUP**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.taup__tilde__):'((MH**2 - MTAUP**2)*((epstaupmuR**2*MH**2)/2. - (epstaupmuR**2*MTAUP**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.taup__tilde__):'((MH**2 - MTAUP**2)*((epstauptaR**2*MH**2)/2. - (epstauptaR**2*MTAUP**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.taup,P.e__plus__):'((MH**2 - MTAUP**2)*((epstaupeR**2*MH**2)/2. - (epstaupeR**2*MTAUP**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.taup,P.mu__plus__):'((MH**2 - MTAUP**2)*((epstaupmuR**2*MH**2)/2. - (epstaupmuR**2*MTAUP**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.taup,P.ta__plus__):'((MH**2 - MTAUP**2)*((epstauptaR**2*MH**2)/2. - (epstauptaR**2*MTAUP**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_nup = Decay(name = 'Decay_nup',
                  particle = P.nup,
                  partial_widths = {(P.W__plus__,P.e__minus__):'((MNUP**2 - MW**2)*((epstaupeR**2*MNUP**4)/(MTAUP*complexconjugate(MTAUP)) + (epstaupeR**2*MNUP**2*MW**2)/(MTAUP*complexconjugate(MTAUP)) - (2*epstaupeR**2*MW**4)/(MTAUP*complexconjugate(MTAUP))))/(32.*cmath.pi*abs(MNUP)**3)',
                                    (P.W__plus__,P.mu__minus__):'((MNUP**2 - MW**2)*((epstaupmuR**2*MNUP**4)/(MTAUP*complexconjugate(MTAUP)) + (epstaupmuR**2*MNUP**2*MW**2)/(MTAUP*complexconjugate(MTAUP)) - (2*epstaupmuR**2*MW**4)/(MTAUP*complexconjugate(MTAUP))))/(32.*cmath.pi*abs(MNUP)**3)',
                                    (P.W__plus__,P.ta__minus__):'((MNUP**2 - MW**2)*((epstauptaR**2*MNUP**4)/(MTAUP*complexconjugate(MTAUP)) + (epstauptaR**2*MNUP**2*MW**2)/(MTAUP*complexconjugate(MTAUP)) - (2*epstauptaR**2*MW**4)/(MTAUP*complexconjugate(MTAUP))))/(32.*cmath.pi*abs(MNUP)**3)',
                                    (P.W__plus__,P.taup):'((2*gwtaupnup**2*MNUP**2 - 12*gwtaupnup**2*MNUP*MTAUP + 2*gwtaupnup**2*MTAUP**2 + (2*gwtaupnup**2*MNUP**4)/MW**2 - (4*gwtaupnup**2*MNUP**2*MTAUP**2)/MW**2 + (2*gwtaupnup**2*MTAUP**4)/MW**2 - 4*gwtaupnup**2*MW**2)*cmath.sqrt(MNUP**4 - 2*MNUP**2*MTAUP**2 + MTAUP**4 - 2*MNUP**2*MW**2 - 2*MTAUP**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MNUP)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_taup = Decay(name = 'Decay_taup',
                   particle = P.taup,
                   partial_widths = {(P.H,P.e__minus__):'((-MH**2 + MTAUP**2)*(-(epstaupeR**2*MH**2)/2. + (epstaupeR**2*MTAUP**2)/2.))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.H,P.mu__minus__):'((-MH**2 + MTAUP**2)*(-(epstaupmuR**2*MH**2)/2. + (epstaupmuR**2*MTAUP**2)/2.))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.H,P.ta__minus__):'((-MH**2 + MTAUP**2)*(-(epstauptaR**2*MH**2)/2. + (epstauptaR**2*MTAUP**2)/2.))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.W__minus__,P.nup):'((2*gwtaupnup**2*MNUP**2 - 12*gwtaupnup**2*MNUP*MTAUP + 2*gwtaupnup**2*MTAUP**2 + (2*gwtaupnup**2*MNUP**4)/MW**2 - (4*gwtaupnup**2*MNUP**2*MTAUP**2)/MW**2 + (2*gwtaupnup**2*MTAUP**4)/MW**2 - 4*gwtaupnup**2*MW**2)*cmath.sqrt(MNUP**4 - 2*MNUP**2*MTAUP**2 + MTAUP**4 - 2*MNUP**2*MW**2 - 2*MTAUP**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.Z,P.e__minus__):'((MTAUP**2 - MZ**2)*((epstaupeR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) + (epstaupeR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) - (epstaupeR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.Z,P.mu__minus__):'((MTAUP**2 - MZ**2)*((epstaupmuR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) + (epstaupmuR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) - (epstaupmuR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.Z,P.ta__minus__):'((MTAUP**2 - MZ**2)*((epstauptaR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) + (epstauptaR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) - (epstauptaR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(32.*cmath.pi*abs(MTAUP)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.nup,P.e__plus__):'((-MNUP**2 + MW**2)*(-((epstaupeR**2*MNUP**4)/(MTAUP*complexconjugate(MTAUP))) - (epstaupeR**2*MNUP**2*MW**2)/(MTAUP*complexconjugate(MTAUP)) + (2*epstaupeR**2*MW**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.nup,P.mu__plus__):'((-MNUP**2 + MW**2)*(-((epstaupmuR**2*MNUP**4)/(MTAUP*complexconjugate(MTAUP))) - (epstaupmuR**2*MNUP**2*MW**2)/(MTAUP*complexconjugate(MTAUP)) + (2*epstaupmuR**2*MW**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.nup,P.ta__plus__):'((-MNUP**2 + MW**2)*(-((epstauptaR**2*MNUP**4)/(MTAUP*complexconjugate(MTAUP))) - (epstauptaR**2*MNUP**2*MW**2)/(MTAUP*complexconjugate(MTAUP)) + (2*epstauptaR**2*MW**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.nup,P.taup__tilde__):'((-2*gwtaupnup**2*MNUP**2 + 12*gwtaupnup**2*MNUP*MTAUP - 2*gwtaupnup**2*MTAUP**2 - (2*gwtaupnup**2*MNUP**4)/MW**2 + (4*gwtaupnup**2*MNUP**2*MTAUP**2)/MW**2 - (2*gwtaupnup**2*MTAUP**4)/MW**2 + 4*gwtaupnup**2*MW**2)*cmath.sqrt(MNUP**4 - 2*MNUP**2*MTAUP**2 + MTAUP**4 - 2*MNUP**2*MW**2 - 2*MTAUP**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.taup__tilde__):'((-MTAUP**2 + MZ**2)*(-(epstaupeR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) - (epstaupeR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) + (epstaupeR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.taup__tilde__):'((-MTAUP**2 + MZ**2)*(-(epstaupmuR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) - (epstaupmuR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) + (epstaupmuR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.nup,P.nup__tilde__):'(((8*gtaupnupw3**2*MNUP**2)/cw**2 + (4*gtaupnupw3**2*MZ**2)/cw**2)*cmath.sqrt(-4*MNUP**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.taup__tilde__):'((-MTAUP**2 + MZ**2)*(-(epstauptaR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) - (epstauptaR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) + (epstauptaR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.e__plus__):'((-MTAUP**2 + MZ**2)*(-(epstaupeR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) - (epstaupeR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) + (epstaupeR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.mu__plus__):'((-MTAUP**2 + MZ**2)*(-(epstaupmuR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) - (epstaupmuR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) + (epstaupmuR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.ta__plus__):'((-MTAUP**2 + MZ**2)*(-(epstauptaR**2*MTAUP**3)/(2.*complexconjugate(MTAUP)) - (epstauptaR**2*MTAUP*MZ**2)/(2.*complexconjugate(MTAUP)) + (epstauptaR**2*MZ**4)/(MTAUP*complexconjugate(MTAUP))))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.taup__tilde__):'((8*cw**2*gtaupnupw3**2*MTAUP**2 + 4*cw**2*gtaupnupw3**2*MZ**2 - 16*cw*gtaupb*gtaupnupw3*MTAUP**2*sw - 8*cw*gtaupb*gtaupnupw3*MZ**2*sw + 8*gtaupb**2*MTAUP**2*sw**2 + 4*gtaupb**2*MZ**2*sw**2)*cmath.sqrt(-4*MTAUP**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

