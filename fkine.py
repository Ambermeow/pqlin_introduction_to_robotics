import roboticstoolbox as rtb
panda = rtb.models.Panda()
Tep = panda.fkine([0, -0.3, 0, -2.2, 0, 2, 0.7854])
print(Tep)

itep_LM = panda.ikine_LM(Tep)
print(itep_LM)

Tep_again = panda.fkine(itep_LM.q)
print(Tep_again)


itep_NR = panda.ikine_NR(Tep)
print(itep_NR)

Tep_again_NR = panda.fkine(itep_NR.q)
print(Tep_again_NR)

panda.ikine