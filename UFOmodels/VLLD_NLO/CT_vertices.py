# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Mac OS X x86 (64-bit) (April 7, 2019)
# Date: Sun 17 Oct 2021 14:01:14


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV1, L.VVV2, L.VVV4, L.VVV6, L.VVV7, L.VVV8 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_149_25,(0,0,1):C.R2GC_149_26,(0,1,0):C.R2GC_152_27,(0,1,1):C.R2GC_152_28,(0,2,0):C.R2GC_152_27,(0,2,1):C.R2GC_152_28,(0,3,0):C.R2GC_149_25,(0,3,1):C.R2GC_149_26,(0,4,0):C.R2GC_149_25,(0,4,1):C.R2GC_149_26,(0,5,0):C.R2GC_152_27,(0,5,1):C.R2GC_152_28})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,0,0):C.R2GC_118_8,(2,0,1):C.R2GC_118_9,(0,0,0):C.R2GC_118_8,(0,0,1):C.R2GC_118_9,(6,0,0):C.R2GC_121_13,(6,0,1):C.R2GC_159_34,(4,0,0):C.R2GC_116_4,(4,0,1):C.R2GC_116_5,(3,0,0):C.R2GC_116_4,(3,0,1):C.R2GC_116_5,(8,0,0):C.R2GC_117_6,(8,0,1):C.R2GC_117_7,(7,0,0):C.R2GC_122_15,(7,0,1):C.R2GC_158_33,(5,0,0):C.R2GC_116_4,(5,0,1):C.R2GC_116_5,(1,0,0):C.R2GC_116_4,(1,0,1):C.R2GC_116_5,(11,0,0):C.R2GC_120_11,(11,0,1):C.R2GC_120_12,(10,0,0):C.R2GC_120_11,(10,0,1):C.R2GC_120_12,(9,0,1):C.R2GC_119_10,(2,1,0):C.R2GC_118_8,(2,1,1):C.R2GC_118_9,(0,1,0):C.R2GC_118_8,(0,1,1):C.R2GC_118_9,(4,1,0):C.R2GC_116_4,(4,1,1):C.R2GC_116_5,(3,1,0):C.R2GC_116_4,(3,1,1):C.R2GC_116_5,(8,1,0):C.R2GC_117_6,(8,1,1):C.R2GC_160_35,(6,1,0):C.R2GC_155_29,(6,1,1):C.R2GC_155_30,(7,1,0):C.R2GC_122_15,(7,1,1):C.R2GC_122_16,(5,1,0):C.R2GC_116_4,(5,1,1):C.R2GC_116_5,(1,1,0):C.R2GC_116_4,(1,1,1):C.R2GC_116_5,(11,1,0):C.R2GC_120_11,(11,1,1):C.R2GC_120_12,(10,1,0):C.R2GC_120_11,(10,1,1):C.R2GC_120_12,(9,1,1):C.R2GC_119_10,(2,2,0):C.R2GC_118_8,(2,2,1):C.R2GC_118_9,(0,2,0):C.R2GC_118_8,(0,2,1):C.R2GC_118_9,(4,2,0):C.R2GC_116_4,(4,2,1):C.R2GC_116_5,(3,2,0):C.R2GC_116_4,(3,2,1):C.R2GC_116_5,(8,2,0):C.R2GC_117_6,(8,2,1):C.R2GC_157_32,(6,2,0):C.R2GC_121_13,(6,2,1):C.R2GC_121_14,(7,2,0):C.R2GC_156_31,(7,2,1):C.R2GC_118_9,(5,2,0):C.R2GC_116_4,(5,2,1):C.R2GC_116_5,(1,2,0):C.R2GC_116_4,(1,2,1):C.R2GC_116_5,(11,2,0):C.R2GC_120_11,(11,2,1):C.R2GC_120_12,(10,2,0):C.R2GC_120_11,(10,2,1):C.R2GC_120_12,(9,2,1):C.R2GC_119_10})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_168_38})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_169_39})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_170_40})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_171_41})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_128_20})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.c, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_128_20})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_128_20})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_18})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_124_18})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_124_18})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_126_19})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_126_19})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_126_19})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_126_19})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_126_19})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_126_19})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_21})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_145_21})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_145_21})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_145_21})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_145_21})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_145_21})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_103_3,(0,1,0):C.R2GC_167_37})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_103_3,(0,1,0):C.R2GC_167_37})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_103_3,(0,1,0):C.R2GC_167_37})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_86_45})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_86_45})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_100_1,(0,1,0):C.R2GC_86_45})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_123_17})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_17})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_164_36,(0,2,0):C.R2GC_164_36,(0,1,0):C.R2GC_123_17,(0,3,0):C.R2GC_123_17})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_17})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_123_17})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_123_17})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.R2GC_148_24,(0,1,2):C.R2GC_83_42,(0,2,0):C.R2GC_147_22,(0,2,1):C.R2GC_147_23})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_84_43})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_102_2,(0,1,0):C.R2GC_102_2,(0,2,0):C.R2GC_102_2})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_94_50,(0,0,1):C.R2GC_94_51,(0,1,0):C.R2GC_94_50,(0,1,1):C.R2GC_94_51,(0,2,0):C.R2GC_94_50,(0,2,1):C.R2GC_94_51})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_97_56,(0,0,1):C.R2GC_97_57,(0,1,0):C.R2GC_97_56,(0,1,1):C.R2GC_97_57,(0,2,0):C.R2GC_97_56,(0,2,1):C.R2GC_97_57})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_92_46,(0,0,1):C.R2GC_92_47,(0,1,0):C.R2GC_92_46,(0,1,1):C.R2GC_92_47,(0,2,0):C.R2GC_92_46,(0,2,1):C.R2GC_92_47})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_96_54,(1,0,1):C.R2GC_96_55,(0,1,0):C.R2GC_95_52,(0,1,1):C.R2GC_95_53,(0,2,0):C.R2GC_95_52,(0,2,1):C.R2GC_95_53,(0,3,0):C.R2GC_95_52,(0,3,1):C.R2GC_95_53})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_93_48,(0,0,1):C.R2GC_93_49,(0,1,0):C.R2GC_93_48,(0,1,1):C.R2GC_93_49,(0,2,0):C.R2GC_93_48,(0,2,1):C.R2GC_93_49})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_85_44})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_85_44})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_85_44})

V_48 = CTVertex(name = 'V_48',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV6, L.VVV7, L.VVV8 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_149_35,(0,0,1):C.UVGC_149_36,(0,0,2):C.UVGC_115_7,(0,0,3):C.UVGC_149_37,(0,1,0):C.UVGC_152_42,(0,1,1):C.UVGC_152_43,(0,1,2):C.UVGC_152_44,(0,1,3):C.UVGC_152_45,(0,3,0):C.UVGC_152_42,(0,3,1):C.UVGC_154_48,(0,3,2):C.UVGC_114_5,(0,3,3):C.UVGC_152_45,(0,5,0):C.UVGC_149_35,(0,5,1):C.UVGC_151_40,(0,5,2):C.UVGC_151_41,(0,5,3):C.UVGC_149_37,(0,6,0):C.UVGC_149_35,(0,6,1):C.UVGC_150_38,(0,6,2):C.UVGC_150_39,(0,6,3):C.UVGC_149_37,(0,7,0):C.UVGC_152_42,(0,7,1):C.UVGC_153_46,(0,7,2):C.UVGC_153_47,(0,7,3):C.UVGC_152_45,(0,2,1):C.UVGC_114_4,(0,2,2):C.UVGC_114_5,(0,4,1):C.UVGC_115_6,(0,4,2):C.UVGC_115_7})

V_49 = CTVertex(name = 'V_49',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV4 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,0,2):C.UVGC_117_11,(2,0,3):C.UVGC_117_10,(0,0,2):C.UVGC_117_11,(0,0,3):C.UVGC_117_10,(6,0,1):C.UVGC_158_58,(6,0,2):C.UVGC_159_62,(6,0,3):C.UVGC_159_63,(6,0,4):C.UVGC_158_61,(4,0,2):C.UVGC_116_8,(4,0,3):C.UVGC_116_9,(3,0,2):C.UVGC_116_8,(3,0,3):C.UVGC_116_9,(8,0,2):C.UVGC_117_10,(8,0,3):C.UVGC_117_11,(7,0,1):C.UVGC_158_58,(7,0,2):C.UVGC_158_59,(7,0,3):C.UVGC_158_60,(7,0,4):C.UVGC_158_61,(5,0,2):C.UVGC_116_8,(5,0,3):C.UVGC_116_9,(1,0,2):C.UVGC_116_8,(1,0,3):C.UVGC_116_9,(11,0,2):C.UVGC_120_14,(11,0,3):C.UVGC_120_15,(10,0,2):C.UVGC_120_14,(10,0,3):C.UVGC_120_15,(9,0,2):C.UVGC_119_12,(9,0,3):C.UVGC_119_13,(2,1,2):C.UVGC_117_11,(2,1,3):C.UVGC_117_10,(0,1,2):C.UVGC_117_11,(0,1,3):C.UVGC_117_10,(4,1,2):C.UVGC_116_8,(4,1,3):C.UVGC_116_9,(3,1,2):C.UVGC_116_8,(3,1,3):C.UVGC_116_9,(8,1,1):C.UVGC_160_64,(8,1,2):C.UVGC_160_65,(8,1,3):C.UVGC_160_66,(8,1,4):C.UVGC_160_67,(6,1,2):C.UVGC_155_49,(6,1,3):C.UVGC_155_50,(6,1,4):C.UVGC_155_51,(7,1,0):C.UVGC_121_16,(7,1,2):C.UVGC_122_18,(7,1,3):C.UVGC_122_19,(5,1,2):C.UVGC_116_8,(5,1,3):C.UVGC_116_9,(1,1,2):C.UVGC_116_8,(1,1,3):C.UVGC_116_9,(11,1,2):C.UVGC_120_14,(11,1,3):C.UVGC_120_15,(10,1,2):C.UVGC_120_14,(10,1,3):C.UVGC_120_15,(9,1,2):C.UVGC_119_12,(9,1,3):C.UVGC_119_13,(2,2,2):C.UVGC_117_11,(2,2,3):C.UVGC_117_10,(0,2,2):C.UVGC_117_11,(0,2,3):C.UVGC_117_10,(4,2,2):C.UVGC_116_8,(4,2,3):C.UVGC_116_9,(3,2,2):C.UVGC_116_8,(3,2,3):C.UVGC_116_9,(8,2,1):C.UVGC_157_54,(8,2,2):C.UVGC_157_55,(8,2,3):C.UVGC_157_56,(8,2,4):C.UVGC_157_57,(6,2,0):C.UVGC_121_16,(6,2,2):C.UVGC_121_17,(6,2,3):C.UVGC_119_12,(7,2,2):C.UVGC_156_52,(7,2,3):C.UVGC_156_53,(7,2,4):C.UVGC_155_51,(5,2,2):C.UVGC_116_8,(5,2,3):C.UVGC_116_9,(1,2,2):C.UVGC_116_8,(1,2,3):C.UVGC_116_9,(11,2,2):C.UVGC_120_14,(11,2,3):C.UVGC_120_15,(10,2,2):C.UVGC_120_14,(10,2,3):C.UVGC_120_15,(9,2,2):C.UVGC_119_12,(9,2,3):C.UVGC_119_13})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS4 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_168_75,(0,0,2):C.UVGC_168_76,(0,0,1):C.UVGC_168_77})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_169_78,(0,0,2):C.UVGC_169_79,(0,0,1):C.UVGC_169_80})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_170_81})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_171_82})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_128_28,(0,1,0):C.UVGC_107_3,(0,2,0):C.UVGC_107_3})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_128_28,(0,1,0):C.UVGC_107_3,(0,2,0):C.UVGC_107_3})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_128_28,(0,1,0):C.UVGC_162_69,(0,2,0):C.UVGC_162_69})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_124_21,(0,1,0):C.UVGC_105_2,(0,2,0):C.UVGC_105_2})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_124_21,(0,1,0):C.UVGC_105_2,(0,2,0):C.UVGC_105_2})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_124_21,(0,1,0):C.UVGC_105_2,(0,2,0):C.UVGC_105_2})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_126_27,(0,1,0):C.UVGC_125_22,(0,1,1):C.UVGC_125_23,(0,1,2):C.UVGC_125_24,(0,1,4):C.UVGC_125_25,(0,1,3):C.UVGC_125_26,(0,2,0):C.UVGC_125_22,(0,2,1):C.UVGC_125_23,(0,2,2):C.UVGC_125_24,(0,2,4):C.UVGC_125_25,(0,2,3):C.UVGC_125_26})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_126_27,(0,1,0):C.UVGC_125_22,(0,1,2):C.UVGC_125_23,(0,1,3):C.UVGC_125_24,(0,1,4):C.UVGC_125_25,(0,1,1):C.UVGC_125_26,(0,2,0):C.UVGC_125_22,(0,2,2):C.UVGC_125_23,(0,2,3):C.UVGC_125_24,(0,2,4):C.UVGC_125_25,(0,2,1):C.UVGC_125_26})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_126_27,(0,1,0):C.UVGC_125_22,(0,1,1):C.UVGC_125_23,(0,1,2):C.UVGC_125_24,(0,1,4):C.UVGC_125_25,(0,1,3):C.UVGC_163_70,(0,2,0):C.UVGC_125_22,(0,2,1):C.UVGC_125_23,(0,2,2):C.UVGC_125_24,(0,2,4):C.UVGC_125_25,(0,2,3):C.UVGC_163_70})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_126_27,(0,1,0):C.UVGC_125_22,(0,1,2):C.UVGC_125_23,(0,1,3):C.UVGC_125_24,(0,1,4):C.UVGC_125_25,(0,1,1):C.UVGC_125_26,(0,2,0):C.UVGC_125_22,(0,2,2):C.UVGC_125_23,(0,2,3):C.UVGC_125_24,(0,2,4):C.UVGC_125_25,(0,2,1):C.UVGC_125_26})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,3):C.UVGC_126_27,(0,1,0):C.UVGC_125_22,(0,1,1):C.UVGC_125_23,(0,1,2):C.UVGC_125_24,(0,1,4):C.UVGC_125_25,(0,1,3):C.UVGC_125_26,(0,2,0):C.UVGC_125_22,(0,2,1):C.UVGC_125_23,(0,2,2):C.UVGC_125_24,(0,2,4):C.UVGC_125_25,(0,2,3):C.UVGC_125_26})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.u] ], [ [P.b, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_126_27,(0,1,0):C.UVGC_125_22,(0,1,2):C.UVGC_125_23,(0,1,3):C.UVGC_125_24,(0,1,4):C.UVGC_125_25,(0,1,1):C.UVGC_125_26,(0,2,0):C.UVGC_125_22,(0,2,2):C.UVGC_125_23,(0,2,3):C.UVGC_125_24,(0,2,4):C.UVGC_125_25,(0,2,1):C.UVGC_125_26})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_145_29,(0,0,1):C.UVGC_145_30})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_145_29,(0,0,1):C.UVGC_145_30})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_145_29,(0,0,2):C.UVGC_165_72,(0,0,1):C.UVGC_145_30})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_145_29,(0,0,1):C.UVGC_145_30})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_145_29,(0,0,1):C.UVGC_145_30})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_145_29,(0,0,2):C.UVGC_165_72,(0,0,1):C.UVGC_145_30})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_166_73,(0,1,0):C.UVGC_167_74})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_164_71,(0,2,0):C.UVGC_164_71,(0,1,0):C.UVGC_161_68,(0,3,0):C.UVGC_161_68})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_123_20,(0,1,0):C.UVGC_104_1,(0,2,0):C.UVGC_104_1})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_148_32,(0,0,1):C.UVGC_148_33,(0,0,2):C.UVGC_148_34,(0,1,2):C.UVGC_147_31})

