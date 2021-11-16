from random import randint

target = input('what string do you want me to generate? ')

def verse_gen(target):
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    verse = ''
    for i in range(len(target)):
        char = alpha_list[randint(0, len(alpha_list)-1)]
        verse += char
    return verse

def verse_score(target, verse):
    score = 0

    for i in range(len(target)):
        if verse[i] == target[i]:
            score += 1
    
    return score
    
def verse_sim(target):
    
    perfect_score = len(target)
    high_score = 0
    best_verse = ''
    counter = 0
    
    while high_score < perfect_score:
        verse = verse_gen(target)
        score = verse_score(target, verse)
        
        if score > high_score:
            high_score = score
            best_verse = verse
        
        if counter % 1000 == 0:
            print(f'on try {counter}, {best_verse} is best with score {high_score}')
        
        counter += 1
    
    print(f'it took {counter} tries to match the target.')
            
verse_sim(target)