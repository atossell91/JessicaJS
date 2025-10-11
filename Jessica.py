from argparse import ArgumentParser

from ProjectCreator import create_project
from ComponentCreator import create_component
from ProjectBuilder import build_project

# JessicaJS AddComponent --name CompName [--output OutputDir]
# JessicaJS NewProject --name ProjName

def AddComponent(args):
    create_component(args.name, ".")

def AddProject(args):
    create_project(args.name)

def StitchProject(args):
    build_project("index.html", ".", "out")

def init_parser():
    parser = ArgumentParser("JessicaJS")
    subparsers = parser.add_subparsers()

    stitch = subparsers.add_parser("Stitch")
    stitch.set_defaults(func=StitchProject)

    addComp = subparsers.add_parser("AddComponent")
    addComp.set_defaults(func=AddComponent)
    addComp.add_argument(
        "name",
        help="The component name"
    )
    addComp.add_argument(
        "--output",
        help="The component output directory"
    )

    addProj = subparsers.add_parser("NewProject")
    addProj.set_defaults(func=AddProject)
    addProj.set_defaults()
    addProj.add_argument(
        "name",
        help="The Project name"
    )
    addProj.add_argument(
        "--output",
        help="The project output directory"
    )

    return parser

def main():
    #parser.add_argument("Action", help="The type of action to run", choices=["AddComponent", "NewProject"])
    parser = init_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
