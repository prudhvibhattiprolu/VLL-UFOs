# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Mac OS X x86 (64-bit) (April 7, 2019)
# Date: Thu 30 Sep 2021 10:08:01


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.e__minus__,P.taup__tilde__):'((MH**2 - MTAUP**2)*((gtaupeLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2 - (gtaupeLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.taup__tilde__):'((MH**2 - MTAUP**2)*((gtaupmuLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2 - (gtaupmuLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.taup__tilde__):'((MH**2 - MTAUP**2)*((gtauptaLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2 - (gtauptaLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.taup,P.e__plus__):'((MH**2 - MTAUP**2)*((gtaupeLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2 - (gtaupeLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.taup,P.mu__plus__):'((MH**2 - MTAUP**2)*((gtaupmuLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2 - (gtaupmuLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.taup,P.ta__plus__):'((MH**2 - MTAUP**2)*((gtauptaLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2 - (gtauptaLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_nup = Decay(name = 'Decay_nup',
                  particle = P.nup,
                  partial_widths = {(P.W__plus__,P.taup):'((2*gwtaupnup**2*MNUP**2 - 12*gwtaupnup**2*MNUP*MTAUP + 2*gwtaupnup**2*MTAUP**2 + (2*gwtaupnup**2*MNUP**4)/MW**2 - (4*gwtaupnup**2*MNUP**2*MTAUP**2)/MW**2 + (2*gwtaupnup**2*MTAUP**4)/MW**2 - 4*gwtaupnup**2*MW**2)*cmath.sqrt(MNUP**4 - 2*MNUP**2*MTAUP**2 + MTAUP**4 - 2*MNUP**2*MW**2 - 2*MTAUP**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MNUP)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'((MT**2 - MW**2)*((3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2))/(96.*cmath.pi*abs(MT)**3)'})

Decay_taup = Decay(name = 'Decay_taup',
                   particle = P.taup,
                   partial_widths = {(P.H,P.e__minus__):'((-MH**2 + MTAUP**2)*(-((gtaupeLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2) + (gtaupeLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.H,P.mu__minus__):'((-MH**2 + MTAUP**2)*(-((gtaupmuLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2) + (gtaupmuLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.H,P.ta__minus__):'((-MH**2 + MTAUP**2)*(-((gtauptaLh**2*MH**2*MTAUP*complexconjugate(MTAUP))/vev**2) + (gtauptaLh**2*MTAUP**3*complexconjugate(MTAUP))/vev**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.W__minus__,P.nup):'((2*gwtaupnup**2*MNUP**2 - 12*gwtaupnup**2*MNUP*MTAUP + 2*gwtaupnup**2*MTAUP**2 + (2*gwtaupnup**2*MNUP**4)/MW**2 - (4*gwtaupnup**2*MNUP**2*MTAUP**2)/MW**2 + (2*gwtaupnup**2*MTAUP**4)/MW**2 - 4*gwtaupnup**2*MW**2)*cmath.sqrt(MNUP**4 - 2*MNUP**2*MTAUP**2 + MTAUP**4 - 2*MNUP**2*MW**2 - 2*MTAUP**2*MW**2 + MW**4))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.W__minus__,P.ve):'((MTAUP**2 - MW**2)*(gtaupveLw**2*MTAUP**2 + (gtaupveLw**2*MTAUP**4)/MW**2 - 2*gtaupveLw**2*MW**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.W__minus__,P.vm):'((MTAUP**2 - MW**2)*(gtaupvmLw**2*MTAUP**2 + (gtaupvmLw**2*MTAUP**4)/MW**2 - 2*gtaupvmLw**2*MW**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.W__minus__,P.vt):'((MTAUP**2 - MW**2)*(gtaupvtLw**2*MTAUP**2 + (gtaupvtLw**2*MTAUP**4)/MW**2 - 2*gtaupvtLw**2*MW**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.Z,P.e__minus__):'((MTAUP**2 - MZ**2)*(gtaupeLz**2*MTAUP**2 + (gtaupeLz**2*MTAUP**4)/MZ**2 - 2*gtaupeLz**2*MZ**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.Z,P.mu__minus__):'((MTAUP**2 - MZ**2)*(gtaupmuLz**2*MTAUP**2 + (gtaupmuLz**2*MTAUP**4)/MZ**2 - 2*gtaupmuLz**2*MZ**2))/(32.*cmath.pi*abs(MTAUP)**3)',
                                     (P.Z,P.ta__minus__):'((MTAUP**2 - MZ**2)*(gtauptaLz**2*MTAUP**2 + (gtauptaLz**2*MTAUP**4)/MZ**2 - 2*gtauptaLz**2*MZ**2))/(32.*cmath.pi*abs(MTAUP)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.nup,P.taup__tilde__):'((-2*gwtaupnup**2*MNUP**2 + 12*gwtaupnup**2*MNUP*MTAUP - 2*gwtaupnup**2*MTAUP**2 - (2*gwtaupnup**2*MNUP**4)/MW**2 + (4*gwtaupnup**2*MNUP**2*MTAUP**2)/MW**2 - (2*gwtaupnup**2*MTAUP**4)/MW**2 + 4*gwtaupnup**2*MW**2)*cmath.sqrt(MNUP**4 - 2*MNUP**2*MTAUP**2 + MTAUP**4 - 2*MNUP**2*MW**2 - 2*MTAUP**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'((-MT**2 + MW**2)*((-3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.taup__tilde__):'((-MTAUP**2 + MW**2)*(-(gtaupveLw**2*MTAUP**2) - (gtaupveLw**2*MTAUP**4)/MW**2 + 2*gtaupveLw**2*MW**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.taup__tilde__):'((-MTAUP**2 + MW**2)*(-(gtaupvmLw**2*MTAUP**2) - (gtaupvmLw**2*MTAUP**4)/MW**2 + 2*gtaupvmLw**2*MW**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.taup__tilde__):'((-MTAUP**2 + MW**2)*(-(gtaupvtLw**2*MTAUP**2) - (gtaupvtLw**2*MTAUP**4)/MW**2 + 2*gtaupvtLw**2*MW**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.taup__tilde__):'((-MTAUP**2 + MZ**2)*(-(gtaupeLz**2*MTAUP**2) - (gtaupeLz**2*MTAUP**4)/MZ**2 + 2*gtaupeLz**2*MZ**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.taup__tilde__):'((-MTAUP**2 + MZ**2)*(-(gtaupmuLz**2*MTAUP**2) - (gtaupmuLz**2*MTAUP**4)/MZ**2 + 2*gtaupmuLz**2*MZ**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.nup,P.nup__tilde__):'((8*cw**2*gtaupnupw3**2*MNUP**2 + 4*cw**2*gtaupnupw3**2*MZ**2 + 16*cw*gnupb*gtaupnupw3*MNUP**2*sw + 8*cw*gnupb*gtaupnupw3*MZ**2*sw + 8*gnupb**2*MNUP**2*sw**2 + 4*gnupb**2*MZ**2*sw**2)*cmath.sqrt(-4*MNUP**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.taup__tilde__):'((-MTAUP**2 + MZ**2)*(-(gtauptaLz**2*MTAUP**2) - (gtauptaLz**2*MTAUP**4)/MZ**2 + 2*gtauptaLz**2*MZ**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.e__plus__):'((-MTAUP**2 + MZ**2)*(-(gtaupeLz**2*MTAUP**2) - (gtaupeLz**2*MTAUP**4)/MZ**2 + 2*gtaupeLz**2*MZ**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.mu__plus__):'((-MTAUP**2 + MZ**2)*(-(gtaupmuLz**2*MTAUP**2) - (gtaupmuLz**2*MTAUP**4)/MZ**2 + 2*gtaupmuLz**2*MZ**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.ta__plus__):'((-MTAUP**2 + MZ**2)*(-(gtauptaLz**2*MTAUP**2) - (gtauptaLz**2*MTAUP**4)/MZ**2 + 2*gtauptaLz**2*MZ**2))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.taup,P.taup__tilde__):'((8*cw**2*gtaupnupw3**2*MTAUP**2 + 4*cw**2*gtaupnupw3**2*MZ**2 - 16*cw*gtaupb*gtaupnupw3*MTAUP**2*sw - 8*cw*gtaupb*gtaupnupw3*MZ**2*sw + 8*gtaupb**2*MTAUP**2*sw**2 + 4*gtaupb**2*MZ**2*sw**2)*cmath.sqrt(-4*MTAUP**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

