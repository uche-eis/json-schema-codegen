#!/usr/bin/env python3

from argparse import ArgumentParser
import sys

import generators


LANGUAGES = {
    "python2": generators.Python2Generator,
    "javascript": generators.JavaScriptGenerator,
    "flow": generators.FlowGenerator,
}


def get_generator(language):
    try:
        return LANGUAGES[language]
    except KeyError:
        raise ValueError("Language {} not supported".format(language))


def main():
    # Validating parameters
    parser = ArgumentParser(description="Generates code from a JSON-schema definition")
    parser.add_argument("--prefix", "-p", help="Optional prefix for generated classes")
    parser.add_argument("--language", "-l", help="Output language. Default is python2")
    parser.add_argument("--output", "-o", help="Output filename for the generated code")
    parser.add_argument("schema", help="Definition of the PRD as JSON schema")

    args = parser.parse_args()

    # Load schema
    with open(args.schema) as f:
        schema = generators.load_schema(f.read())

    # Generate code
    generator = get_generator(args.language)
    code = generator(schema, prefix=args.prefix).generate().as_code()

    # Output code
    if args.output:
        with open(args.output, "w") as f:
            f.write(code)
    else:
        sys.stdout.write(code)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
