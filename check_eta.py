
from eta import eta_hours

print("Case 1 — 0 km, standard:", eta_hours(0, False))
print("Case 2 — 250 km, standard:", eta_hours(250, False))
print("Case 3 — 250 km, express:", eta_hours(250, True))
print("Case 4 — 100 km, standard:", eta_hours(100, False))
