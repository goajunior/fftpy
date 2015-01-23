(* f[t_] := 129534*(Exp[-t*(2*^06/68.2)] - Exp[-t*(2*^06/0.405)]) *)
f[t_]:= Sin[100*Pi*t]+0.5*Sin[160*Pi*t]
Export["cmd.txt", $CommandLine,"Table"];
ns    =ToExpression[$CommandLine[[8]]]
(*tval = Table[N[t], {t, 0, 50*^-6, 50*^-6/ns}]*)
tval = Table[N[t], {t, 0, 600/800, 600/(ns*800)}]
fval = Table[f[t], {t, 0, 600/800, 600/(ns*800)}]
data = MapThread[{#1, #2} &, {tval, fval}] (*junta as colunas de dadosa *)
Export["data.txt", data, "Table"];
