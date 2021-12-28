def content(filename):
    with open(filename, 'r') as fasta:
        seq = ""
        for line in fasta:
            if ">" in line:
                if seq != "":
                    length = len(seq)
                    print('C Content: ', round((seq.count("C")/length)*100,2),'%')
                    print('G Content: ', round((seq.count("G")/length) * 100,2),'%')
                    break
                print(line, end = "")
            else:
                line = line.rstrip("\n")
                seq = seq+line
    fasta.close()

content('sequence.fna')

