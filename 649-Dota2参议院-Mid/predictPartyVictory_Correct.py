def predictPartyVictory(senate: str) -> str:
    rq = list()
    dq = list()
    length = len(senate)

    for i in range(length):
        c = senate[i]
        if c == "R":
            rq.append(i)
        else:
            dq.append(i)

    while len(rq) > 0 and len(dq) > 0:
        r = rq[0]
        d = dq[0]

        if r > d:
            # 保留 r
            dq.append(d + length)
        else:
            rq.append(r + length)

        del rq[0]
        del dq[0]

    return "Dire" if len(rq) == 0 else "Radiant"

def main():
    senate = "DDRRR"
    print(predictPartyVictory(senate))

if __name__ == '__main__':
    main()