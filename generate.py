from faker import Faker
import numpy as np
import pandas as pd
import datetime
import argparse
import json

fake = Faker()


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION]",
        description="Generate random survey dataset."
    )

    parser.add_argument("-v", "--version", action="version",
                        version=f"{parser.prog} version 1.0.0")
    parser.add_argument("-c", "--config", required="true", type=str,
                        help="JSON file containing the configuration of the survey")
    parser.add_argument(
        "--header", help="Include header a the top of the file", action="store_true")
    parser.add_argument("-o", "--out", type=str,
                        help="Name of the file to output the results. If this is not specified the output will be printed on the screen")
    parser.add_argument(
        "-a", "--append", help="If the output is redirected to a file, use this flag to if you want to append to the file, otherwise the file will be overwritten", action="store_true")

    return parser


def random_date(start, end, entries):
    '''Returns a list of random dates between the start and end dates provided.

    Parameters
    ----------
    start : datetime
        Earliest possible date
    end : datetime
        Latest possible date
    entries : int
        Number of entries to generate

    Returns
    -------
    list
        Random dates between the start and end dates
    '''
    random_dates = list()
    while 0 < entries:
        random_dates.append(fake.date_time_between(
            start_date=start, end_date=end))
        entries -= 1
    return random_dates


def generate_entries(config):
    entries = config['entries']

    columns = []
    rows = []

    for q in config['questions']:
        columns.append(q['question'])

    for q in config['questions']:
        if q['answers']['type'] == 'int':
            decoded_start = int(q['answers']['start'])
            decoded_end = int(q['answers']['end'])
            row_column_int = np.random.randint(
                decoded_start, decoded_end + 1, size=entries)
            rows.append(row_column_int)
        elif q['answers']['type'] == "datetime":
            decoded_start_date = datetime.datetime.strptime(
                q['answers']['start'], "%Y%m%d")
            decoded_end_date = datetime.datetime.strptime(
                q['answers']['end'], "%Y%m%d")
            row_column_datetime = random_date(
                decoded_start_date, decoded_end_date, entries)
            rows.append(row_column_datetime)
        elif q['answers']['type'] == "choice":
            choices = q['answers']['choices']
            row_column_choice = np.random.choice(choices, size=entries)
            rows.append(row_column_choice)

    data = list(zip(*rows))
    df = pd.DataFrame(data, columns=columns)
    return df


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    config = args.config

    with open(config) as json_file:
        data = json.load(json_file)
        random_entries = generate_entries(data)
        result = pd.concat([random_entries])

        if not args.out:
            print(result.to_csv(index=False))
        else:
            mode = 'w'
            if (args.append):
                mode = 'a'

            result.to_csv(args.out, mode=mode, index=False, header=args.header)


if __name__ == "__main__":
    main()
