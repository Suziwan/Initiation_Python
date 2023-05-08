# écrire un programme qui demande à l'utilisateur de saisir son âge et affiche 'vous êtes majeur !' 
# si l'âge est supérieur ou égal à 18 et 'vous êtes mineur' sinon
age = input('Quel âge avez-vous? >')

if int(age) >= 18:
    print('vous êtes majeur !')
else:
    print('vous êtes mineur')

# écrire un programme qui demande à l'utilisateur de saisir un nombre et affiche 'a est pair' 
# si la valeur de a est paire et 'a est impair' sinon
number = input('Entrez un nombre entier >')

if int(number)%2 == 0:
    print('a est pair')
else:
    print('a est impair')