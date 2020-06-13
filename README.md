# Random Survey Results

![GitHub repo size](https://img.shields.io/github/repo-size/allanlykkechristensen/random_survey_results)
![GitHub contributors](https://img.shields.io/github/contributors/allanlykkechristensen/random_survey_results)
![GitHub stars](https://img.shields.io/github/stars/allanlykkechristensen/random_survey_results)
![GitHub forks](https://img.shields.io/github/forks/allanlykkechristensen/random_survey_results)

Random Survey Results is a utility that allows data people to do generate random survey results based on a configuration file.

Purpose of the application is to quickly generate some random data that appears to come from a survey and can be used for practising data wrangling and analysis.

The current version support the random generation of a survey that contains the following column types:
- datetime (a column with a date and time in a given range)
- int (a column with a random integer in a given range)
- choice (a column with a random value from a choice of possible values)

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed the latest version of Python 3

## Installing the Python Prerequisites

To install random_survey_results, follow these steps:

```
git clone https://github.com/allanlykkechristensen/random_survey_results
cd random_survey_results
pip install -f requirements.txt
```

## Using Random Survey Results

To use random_survey_results, follow these steps:

```
python generate.py --config sample/nps.json --header
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

* [@bigallan](https://github.com/allanlykkechristensen)

## Contact

If you want to contact me you can reach me at allan.lykke.christensen@gmail.com.

## License

This project uses the following license: [MIT](https://opensource.org/licenses/MIT).
