Nume: Robert Gogete
Grupă: 331CB

# Tema 1 

Organizare
-
1. Explicație pentru soluția aleasă:

Solutia a urmat scheletul de cod folosit, functiile facand exact ceea ce scria
in descrierea din schelet. Producatorul produce la infinit, cat timp mai exista
consumatori, dupa care se opreste. Acest lucru este masurat incrementand o
variabila care se afla in spatele unui lock (pentru a numara cati consumatori
sunt) si drecrementand-o la final (cand au terminat de consumat). 

Consumatorii, dupa ce isi creeaza un cos nou, incep sa adauge / scoata produse
din cos (obiect adaugat in plus de mine care are doar o lista cu produse si
functiile aferente adaugarii si stergerii).

Consider ca tema a fost una interesanta, cu o dificultate nu prea crescuta si
o implementare eleganta.
Cea mai dificila parte a fost intelegerea scheletelui si a datelor de intrare,
ceea ce mi se pare foarte practic, intrucat simuleaza situatii cu care ne-am
intal-nii la un job (unde trebuie sa dezvoltam folosind diferite API uri).

Implementare
-
Tema este implementata partial, deoarece am optat sa folosesc o singura coada,
nu cate una individuala pentru fiecare producator - testele nu reflecta acest
lucru.

O dificultate peste care am dat a fost importarea de fisiere locale precum
cart.py. Am reusit sa rezolv importand in schimb tema.cart, care insa
apare da eroare in pylint (asta nu am reusit sa rezolv).

Resurse utilizate
-

* https://www.w3schools.com/
* https://stackoverflow.com/
* laborator 2 asc

Git
-
1. https://github.com/gogeterobert/Tema1ASC.git
