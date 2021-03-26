import requests
import concurrent.futures
import os

def get_keyword(keyword=None, language="en", limit=500):
    result = list()
    url_base = "https://app.neilpatel.com"
    url_1 = "/api/keyword_info?keyword={}&language=en"
    url_2 = "https://app.neilpatel.com/api/match_keywords?keyword={}&locId={}&language=en&sortBy=searchVolume&sortMode=desc&limit={}&previousKey={}"
    headers = {'Accept': 'application/json, text/plain, */*',
                'X-Transaction-ID': '77f3b14367fb49adb3804e1ff25b015e',
                 'Authorization': 'Bearer app#unlogged__0d703b5bab9916c9afcc25ccaa161724ee956578'}
    req_1 = requests.get(url_base+url_1.format(keyword), headers=headers).json()
    counter = 0
    while len(result) <= limit:
        url_ku = url_2.format(keyword, req_1['locId'], "500", str(counter))
        print(url_ku)
        req_2 = requests.get(url_ku, headers=headers).json()
        for key_sugges in req_2['suggestions']:
            result.append(key_sugges['keyword'])
        counter += 1
    return result

def core(mode, output, limit):
    keywords = list()

    if mode == "manual":
        print("(press q to quit)\n")
        a = None
        while True:
            a = input("input your keyword:")
            assert a.isalpha(), "ENTER STR NOT DECIMAL"
            if a == "q": break
            keywords.append(a)
            
    elif mode == "file":
        file_in = input("Enter your keywords file name: ")
        assert os.path.isfile(file_in), "File Not Found"
        keywords.extend([x.split("\n")[0] for x in open(file_in, 'r').readlines()])
    else: raise Exception("NO MODE")

    for key in keywords:
        key_ = get_keyword(key, "en",limit)
        print(key)
        with open(output, 'a') as f:
            for x in key_:
                try:
                    f.write(x+"\n")
                except BaseException as e:
                    print(e)
                    continue

if __name__ == "__main__":
    import argparse
    arg = argparse.ArgumentParser()
    arg.add_argument('-m', '--mode', default="manual",
                    type=str, required=False, help="choose mode (manual) input or (file) input")
    arg.add_argument("-o", "--output", default="key_result.txt", type=str,
                        required=False, help="File outupt")
    arg.add_argument('-l','--limit', type=int, default=500, required=False,
                            help="limit your keywords each keyword")
    
    args = vars(arg.parse_args())
    
    core(**args)