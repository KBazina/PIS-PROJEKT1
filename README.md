# PIS-PROJEKT1

--KAKO POKRENUTI-------------
- klonirati kod sa mog githuba u neku datoteku
- trebate imati instaliran docker
- upisati komandu -- docker container run -d -p 5000:5000 karlovk/hey-python-flask:0.0.1.RELEASE
- pokrenuti na localhostu -- localhost:5000


------------------------------------------

Ovaj projekt predstavlja stranicu jednog autosalona na kojem vlasnik objavljuje aute koji su trenutno u prodaji

--------------------------
Vlasnik mora ispuniti formular koji se sastoji od marke, modela, godišta, kilometraže, motora, snage motora, kubikaže, cijene i na kraju slike 
(ako se ne izabere niti jedna slika automatski se stavlja defaultna slika)
nakon ispunjavanja dodaje se novi auto u baze te se objavljuje na stranicu i vide se podatci o njemu
na gumb uredi- vlasnik moze mjenjati cijenu i kilometrazu auta no sve ostale stavke ostaju iste
kada se auto proda vlasnik klikom obrisi i potvrdom na vrhu ekrana da ga želi obirsati briše auto iz baze podataka i samimi time se miče sa stranice
