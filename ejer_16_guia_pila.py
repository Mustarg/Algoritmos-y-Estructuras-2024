"""Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
bos episodios."""

from pila import Stack

pilaPersonajesEpisodioVII = Stack()
pilaPersonajesEpisodioV = Stack()
listaMixta=[]

class Personaje:

    def __init__(self, nombre, episodioDeAparicion):
        self.nombre = nombre
        self.episodioDeAparicion = episodioDeAparicion

    def __str__(self):
        return f"{self.nombre} - {self.episodioDeAparicion}"


personajes = [
    Personaje("4-LOM", 5),
    Personaje("4B-EG-6", 7),
    Personaje("1138", 7),
    Personaje("Agua Jabosa Dillifay Glon", 7),
    Personaje("Allium", 7),
    Personaje("Anakin Skywalker", 7),
    Personaje("Anophe Dengue", 7),
    Personaje("Ap'lek", 7),
    Personaje("Armitage Hux", 7),
    Personaje("Athgar Heece", 7),
    Personaje("Avga Rosene", 7),
    Personaje("B-U4D", 7),
    Personaje("Bala-Tik", 7),
    Personaje("Bastian", 7),
    Personaje("Bazine Netal", 7),
    Personaje("BB-8", 7),
    Personaje("Bewil", 5),
    Personaje("Blass Tyran", 7),
    Personaje("Boba Fett", 5),
    Personaje("Bobbajo", 7),
    Personaje("Bolivar Denai", 7),
    Personaje("Bollie Prindel", 7),
    Personaje("Bossk'wassak'Cradossk", 5),
    Personaje("Bren Derlin", 5),
    Personaje("C'ai Threnalli", 7),
    Personaje("C-3PO", 5),
    Personaje("C-3PO", 7),
    Personaje("Cabbel", 5),
    Personaje("Cal Alder", 5),
    Personaje("Caluan Ematt", 7),
    Personaje("Canonhaus", 5),
    Personaje("Cardo", 7),
    Personaje("Carlist Rieekan", 5),
    Personaje("Chase Wilsorr", 5),
    Personaje("Chewbacca", 5),
    Personaje("Chewbacca", 7),
    Personaje("Chiffonage", 5),
    Personaje("Ciena Ree", 5),
    Personaje("CR978", 5),
    Personaje("Cratinus", 7),
    Personaje("Crokind Shand", 7),
    Personaje("Cypress", 7),
    Personaje("Dak Ralter", 5),
    Personaje("Darth Sidious", 7),
    Personaje("Darth Vader", 5),
    Personaje("Dasha Promenti", 7),
    Personaje("Davan Marak", 7),
    Personaje("Deena Lorn", 5),
    Personaje("Dengar", 5),
    Personaje("Derek Klivian", 5),
    Personaje("Divis Scaldz", 7),
    Personaje("Dopheld Mitaka", 7),
    Personaje("Drego", 7),
    Personaje("Durteel Haza", 7),
    Personaje("E-3PO", 5),
    Personaje("EGL-21", 7),
    Personaje("Ello Asty", 7),
    Personaje("Erich S. Datoo", 7),
    Personaje("Finn", 7),
    Personaje("Firmus Piett", 5),
    Personaje("FN-417", 7),
    Personaje("FN-1824", 7),
    Personaje("FN-2003", 7),
    Personaje("FN-2199", 7),
    Personaje("FN-3181", 7),
    Personaje("FN-9330", 7),
    Personaje("FS-451", 5),
    Personaje("Furillo", 7),
    Personaje("FX-7", 5),
    Personaje("GA-97", 7),
    Personaje("Gadde Neshurrion", 7),
    Personaje("Goss Toowers", 7),
    Personaje("Grevoth Prana IX", 7),
    Personaje("Grummgar", 7),
    Personaje("GTAW-74", 7),
    Personaje("Guich", 7),
    Personaje("Gwellis Bagnoro", 7),
    Personaje("Han Solo", 5),
    Personaje("Han Solo", 7),
    Personaje("Harter Kalonia", 7),
    Personaje("Helder Spinoza", 5),
    Personaje("Hobin Carsamba", 7),
    Personaje("Hoogenz", 7),
    Personaje("HURID-327", 7),
    Personaje("IG-88B", 5),
    Personaje("Ilco Munica", 7),
    Personaje("Infrablue Zedbeddy Coggins", 7),
    Personaje("Isdam Edian", 5),
    Personaje("IT-000-XZ 1594", 7),
    Personaje("Izby", 7),
    Personaje("J'Rrosch", 7),
    Personaje("JA189", 5),
    Personaje("Jabba Desilijic Tiure", 5),
    Personaje("Jashco Phurus", 7),
    Personaje("Jessika Pava", 7),
    Personaje("Juhrah Yani", 7),
    Personaje("K-3PO", 5),
    Personaje("Kaplan", 7),
    Personaje("Kaydel Ko Connix", 7),
    Personaje("Kendal Ozzel ", 5),
    Personaje("Kesin Ommis", 5),
    Personaje("Kit Valent", 5),
    Personaje("Korr Sella", 7),
    Personaje("KT-310", 7),
    Personaje("Kuruk", 7),
    Personaje("Kylo Ren", 7),
    Personaje("L3-37", 5),
    Personaje("Landonis Balthazar Calrissian", 5),
    Personaje("Lanever Villecham", 7),
    Personaje("Laparo", 7),
    Personaje("Lastok", 5),
    Personaje("Ledick Firest", 5),
    Personaje("Leia Organa", 5),
    Personaje("Leia Organa", 7),
    Personaje("Lema Eelyak", 7),
    Personaje("Lennox", 5),
    Personaje("Lobot", 5),
    Personaje("Lor San Tekka", 7),
    Personaje("Lorth Needa", 5),
    Personaje("Luke Skywalker", 5),
    Personaje("Luke Skywalker", 7),
    Personaje("M6-15R", 7),
    Personaje("M9-G8", 7),
    Personaje("M'Kae", 5),
    Personaje("Mandetat", 7),
    Personaje("Maximilian Veers", 5),
    Personaje("Maz Kanata", 7),
    Personaje("ME-8D9", 7),
    Personaje("Meta", 7),
    Personaje("Mi'no Teest", 7),
    Personaje("Min Sakul", 7),
    Personaje("Monn Tatth", 7),
    Personaje("Munduri", 7),
    Personaje("Murra", 5),
    Personaje("Nahani Gillen", 7),
    Personaje("Nash Windrider", 5),
    Personaje("Nastia Unamo", 7),
    Personaje("Nemet", 5),
    Personaje("Nevar ", 5),
    Personaje("Nien Nunb", 7),
    Personaje("Niv Lek", 7),
    Personaje("Obi-Wan Kenobi", 5),
    Personaje("Obi-Wan Kenobi", 7),
    Personaje("OL701 ", 5),
    Personaje("Omalin Fisker", 7),
    Personaje("Oskus Stooratt", 7),
    Personaje("Pammich Nerro Goode", 7),
    Personaje("Penrie", 5),
    Personaje("Pharl McQuarrie", 5),
    Personaje("Phasma", 7),
    Personaje("Poe Dameron", 7),
    Personaje("Prashee", 7),
    Personaje("Praster Ommlen", 7),
    Personaje("Pru Sweevant", 7),
    Personaje("PZ-4CO", 7),
    Personaje("Quiggold", 7),
    Personaje("R0-4L0", 7),
    Personaje("R0-H2", 7),
    Personaje("R1", 7),
    Personaje("R2-D2", 5),
    Personaje("R2-D2", 7),
    Personaje("R2-KT", 7),
    Personaje("R3-A2", 5),
    Personaje("R3-Y2", 5),
    Personaje("R5-M2", 5),
    Personaje("R6-D8", 7),
    Personaje("R-3DO", 7),
    Personaje("R-3PO", 5),
    Personaje("Razoo Qin-Fee", 7),
    Personaje("Resdox", 7),
    Personaje("Rey", 7),
    Personaje("Reyé Hollis", 5),
    Personaje("Riba", 5),
    Personaje("Risueño", 5),
    Personaje("Rodinon", 7),
    Personaje("Romas Navander", 5),
    Personaje("Roodown", 7),
    Personaje("Rosser Weno", 7),
    Personaje("RP-G0", 7),
    Personaje("Sache Skareet", 7),
    Personaje("Sarco Plank", 7),
    Personaje("Scrapjaw Motito", 7),
    Personaje("Sheckil", 5),
    Personaje("Sheev Palpatine", 5),
    Personaje("Sidon Ithano", 7),
    Personaje("Skorr", 5),
    Personaje("Snoke", 7),
    Personaje("Sonsigo", 7),
    Personaje("Starck", 5),
    Personaje("Streehn", 7),
    Personaje("Strono Tuggs", 7),
    Personaje("Suba", 5),
    Personaje("Sy-O", 5),
    Personaje("Tabala Zo", 7),
    Personaje("Tarrin", 5),
    Personaje("Taryish Juhden", 7),
    Personaje("Taslin Brance", 7),
    Personaje("Tasu Leech", 7),
    Personaje("Taybin Ralorsa", 7),
    Personaje("Teedo", 7),
    Personaje("Temmin Wexley", 7),
    Personaje("Thadlé Berenko", 7),
    Personaje("Thanisson", 7),
    Personaje("Thanlis Depallo", 7),
    Personaje("Thromba", 7),
    Personaje("Tiaan Jerjerrod", 5),
    Personaje("Tig", 5),
    Personaje("Tigran Jamiro", 5),
    Personaje("TK-338", 7),
    Personaje("TK-5187", 5),
    Personaje("Tolomar Reez", 7),
    Personaje("Toryn Farr", 5),
    Personaje("Treadwell", 5),
    Personaje("Trey Callum", 5),
    Personaje("Trinto Duaba", 7),
    Personaje("Trudgen", 7),
    Personaje("TS-4068", 5),
    Personaje("Ubert Quaril", 7),
    Personaje("Ugloste", 5),
    Personaje("Unkar Plutt", 7),
    Personaje("Ushar", 7),
    Personaje("Ushos O. Statura", 7),
    Personaje("Venalo Wintz", 7),
    Personaje("Vicrul", 7),
    Personaje("Vober Dand", 7),
    Personaje("Volzang Li-Thrull", 7),
    Personaje("Wedge Antilles", 5),
    Personaje("Wes Janson", 5),
    Personaje("Wi'ba Tuyll", 7),
    Personaje("Will Scotian", 5),
    Personaje("Willrow Hood", 5),
    Personaje("Wollivan", 7),
    Personaje("Wright", 7),
    Personaje("Wyron Serper", 5),
    Personaje("XJ9-CS14", 5),
    Personaje("Yoda", 5),
    Personaje("Yoda", 7),
    Personaje("Yolo Ziff", 7),
    Personaje("Yoxgit", 5),
    Personaje("Zev Senesca", 5),
    Personaje("Zuckuss", 5),
    Personaje("Zuvio", 7),
    Personaje("Zygli Bruss", 7),
    Personaje("2-1B", 5),
]

print(personajes)

for pjs in personajes:
    if pjs.episodioDeAparicion == 5:
        pilaPersonajesEpisodioV.push(pjs)
    else:
        pilaPersonajesEpisodioVII.push(pjs)

print(pilaPersonajesEpisodioV.size())
print(pilaPersonajesEpisodioVII.size())

while (pilaPersonajesEpisodioV.size() > 0):
    pj = pilaPersonajesEpisodioV.pop().nombre
    if ((listaMixta.count(pj) == 0)):
        listaMixta.append(pj)

while (pilaPersonajesEpisodioVII.size() > 0):
    pj2 = pilaPersonajesEpisodioVII.pop().nombre
    if ((listaMixta.count(pj2) == 0)):
        listaMixta.append(pj2)

print(listaMixta)

print(pilaPersonajesEpisodioV.size())
