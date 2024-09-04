import operator

def person_lister(f):
    def inner(people):
        people_sorted = sorted(people, key=lambda el: el[2])
        to_return = []
        for p in people_sorted:
            to_return.append(f(p))
        return to_return
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(name_format(people), sep='\n')
