import subprocess
from os import listdir

def main():
    for svg in listdir("../../figures/figs/"):
        if not svg.endswith("svg"):
            print("Warning: unexpected dir entry {}".format(svg))

        out_name = svg[:-3] + "png"
        com = ["convert", '../../figures/figs/{}'.format(svg), "{}".format(out_name)]
        print("$ " + " ".join(com))
        subprocess.run(com)


if __name__ == "__main__":
    main()
