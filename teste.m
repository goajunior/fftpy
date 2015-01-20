f[t_] := 129534*(Exp[-t*(2*^06/68.2)] - Exp[-t*(2*^06/0.405)])
tval = Table[N[t], {t, 0, 50*^-6, 50*^-6/25}]
fval = Table[f[t], {t, 0, 50*^-6, 50*^-6/25}]
data = MapThread[{#1, #2} &, {tval, fval}] (*junta as colunas de dadosa *)
Export["data.txt", data, "Table"];
