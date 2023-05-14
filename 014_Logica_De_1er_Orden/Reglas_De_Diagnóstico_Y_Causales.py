% Reglas de diagnóstico y causales en Prolog

% Si el aire acondicionado no enciende, puede ser debido a un problema en el termostato o en el suministro eléctrico
causa_noenciende(X) :- problema_termostato(X).
causa_noenciende(X) :- problema_suministro(X).

% Si el termostato no funciona, el aire acondicionado no encenderá
problema_termostato(X) :- falla_termostato(X).

% Si hay un problema en el suministro eléctrico, el aire acondicionado no encenderá
problema_suministro(X) :- falla_suministro(X).

% Hechos
falla_termostato(termostato1).
falla_suministro(suministro1).
