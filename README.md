# Random Survey Results

![Python application](https://github.com/allanlykkechristensen/random_survey_results/workflows/Python%20application/badge.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/allanlykkechristensen/random_survey_results)
![GitHub contributors](https://img.shields.io/github/contributors/allanlykkechristensen/random_survey_results)
![GitHub stars](https://img.shields.io/github/stars/allanlykkechristensen/random_survey_results)
![GitHub forks](https://img.shields.io/github/forks/allanlykkechristensen/random_survey_results)

Random Survey Results is a utility that allows data people to generate random survey results.

Purpose of the utility is to quickly generate random data that appears to come from a survey and can be used for practising data wrangling and analysis.

## Using Random Survey Results

To use random_survey_results, follow these steps:

### Download the Latest Release Available

Go to the [releases page](https://github.com/allanlykkechristensen/random_survey_results/releases) and download the latest release.

### Create a Configuration File

To generate random survey results, you must provide `random_survey_results` with a configuration that specifies the desired outcome.

The configuration file is formatted using JSON:

```json
{
    "entries": 50,
    "questions": [
        {
            "question": "Timestamp",
            "answers": {
                "type": "datetime",
                "start": "20190601",
                "end": "20200630"
            }
        },
        {
            "question": "Channel",
            "answers": {
                "type": "choice",
                "choices": [
                    "Website",
                    "Mobile App (iOS)",
                    "Mobile App (Android)",
                    "Website Shop"
                ]
            }
        },
        {
            "question": "Location",
            "answers": {
                "type": "choice",
                "choices": [
                    "DK",
                    "MX",
                    "US",
                    "GB",
                    "IE",
                    "DE",
                    "ES",
                    "RU",
                    "IT"
                ]
            }
        },
        {
            "question": "Score",
            "answers": {
                "type": "int",
                "start": "0",
                "end": "10"
            }
        }
   ]
}
```

The configuration above generates random survey results for an NPS survey.

1. It generates a total of 50 entries with four questions (columns).
1. The first column contains a random time stamp for when the survey was submitted. The timestamps are between 1st June 2019 and 30th June 2020.
1. The second column is the channel where the survey was collected. We specify four possible channels and will be used at random.
1. The third column is the location where the survey was collected. We specify a number of possible country codes that will be used at random.
1. The forth and last column is the score which will contain a random integer between 0 and 10 (both inclusive).

### Generating Results

With the configuration file in place, the utility can be executed. The above configuration file is available in /samples/nps.json and will be used in the example below:

```bash
foo@bar:~$ random_survey_results --config samples/nps.json --header

Timestamp,Channel,Location,Score
2019-10-15 08:21:11,Website,IE,10
2019-12-05 11:09:38,Mobile App (Android),ES,0
2020-01-04 20:17:20,Mobile App (Android),ES,6
2019-11-09 02:50:55,Website,US,9
2020-06-17 20:36:02,Website,US,8
2020-06-12 15:13:50,Website,DE,2
2020-05-27 04:33:17,Website,MX,0
...
...
2019-06-17 15:20:35,Website,US,3
```

### Usage Options

```bash
usage: random_survey_results.py [OPTION]

Generate random survey dataset.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c CONFIG, --config CONFIG
                        JSON file containing the configuration of the survey
  --header              Include header a the top of the file
  -o OUT, --out OUT     Name of the file to output the results. If this is not specified the output will be printed on the screen
  -a, --append          If the output is redirected to a file, use this flag to if you want to append to the file, otherwise the file will be overwritten
```

## Contributing to Random Survey Results

To contribute to random_survey_results, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

- [@bigallan](https://github.com/allanlykkechristensen)

## Contact

If you want to contact me you can reach me at allan.lykke.christensen@gmail.com.

## License

This project uses the following license: [MIT](https://opensource.org/licenses/MIT).
