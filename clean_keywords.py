from random import choice

def core(file_in, file_out):
    with open(file_in, 'r') as f:
        with open(file_out, 'w') as w:
            for x in f.readlines():
                f_ = x.split()
                if len(f_) >= 3:
                    f1 = choice(f_)
                    f2 = choice(f_)
                    while f1 == f2:
                        f2 = choice(f_)
                    x = "%s %s" % (f1,f2)
                    w.write(x+"\n")
                else:
                    w.write(x)
    print("DONE")
    
if __name__ == '__main__':
    import argparse
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--file_in', type=str, default="keywords.txt", required=False)
    arg.add_argument('-o', '--file_out', type=str, default='keywords_clean.txt', required=False)
    args = vars(arg.parse_args())
    core(**args)