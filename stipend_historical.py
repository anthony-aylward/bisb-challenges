import pandas as pd
import seaborn as sns

from argparse import ArgumentParser

STIPEND = pd.DataFrame([
    (2013, 28_500, 'Nominal'),
    (2013, 28_500/258.955*298.147, '2019'),
    (2014, 28_500, 'Nominal'),
    (2014, 28_500/265.251*298.147, '2019'),
    (2015, 30_000, 'Nominal'),
    (2015, 30_000/267.346*298.147, '2019'),
    (2016, 32_000, 'Nominal'),
    (2016, 32_000/272.628*298.147, '2019'),
    (2017, 32_000, 'Nominal'),
    (2017, 32_000/281.561*298.147, '2019'),
    (2018, 32_000, 'Nominal'),
    (2018, 32_000/290.076*298.147, '2019'),
    (2019, 33_000, 'Nominal'),
    (2019, 33_000, '2019'),
], columns=['Year', 'USD', 'Dollars',])

RENT = pd.DataFrame([
    (2013, 1289, 'Nominal', 'record'),
    (2013, 1289/258.955*298.147, '2019', 'record'),
    (2014, 1373, 'Nominal', 'record'),
    (2014, 1373/265.251*298.147, '2019', 'record'),
    (2015, 1427, 'Nominal', 'record'),
    (2015, 1427/267.346*298.147, '2019', 'record'),
    (2016, 1504, 'Nominal', 'record'),
    (2016, 1504/272.628*298.147, '2019', 'record'),
    (2017, 1598, 'Nominal', 'record'),
    (2017, 1598/281.561*298.147, '2019', 'record'),
    (2017, 1598, 'Nominal', 'conservative estimate'),
    (2017, 1598/281.561*298.147, '2019', 'conservative estimate'),
    (2018, 1646, 'Nominal', 'conservative estimate'),
    (2018, 1646/290.076*298.147, '2019', 'conservative estimate'),
    (2019, 1712, 'Nominal', 'conservative estimate'),
    (2019, 1712, '2019', 'conservative estimate')
], columns=['Year', 'USD', 'Dollars', 'Certainty'])

CPI = pd.DataFrame([
    (2013, 258.955),
    (2014, 265.251),
    (2015, 267.346),
    (2016, 272.628),
    (2017, 281.561),
    (2018, 290.076),
    (2019, 298.147)
], columns=['Year', 'USD'])

STIPEND_AFTER_RENT = pd.DataFrame([
    (2013, 28_500/12 - 1289/2, 'Nominal', 'record'),
    (2013, (28_500/12 - 1289/2)/258.955*298.147, '2019', 'record'),
    (2014, 28_500/12 - 1373/2, 'Nominal', 'record'),
    (2014, (28_500/12 - 1373/2)/265.251*298.147, '2019', 'record'),
    (2015, 30_000/12 - 1427/2, 'Nominal', 'record'),
    (2015, (30_000/12 - 1427/2)/267.346*298.147, '2019', 'record'),
    (2016, 32_000/12 - 1504/2, 'Nominal', 'record'),
    (2016, (32_000/12 - 1504/2)/272.628*298.147, '2019', 'record'),
    (2017, 32_000/12 - 1598/2, 'Nominal', 'record'),
    (2017, (32_000/12 - 1598/2)/281.561*298.147, '2019', 'record'),
    (2017, 32_000/12 - 1598/2, 'Nominal', 'conservative estimate'),
    (2017, (32_000/12 - 1598/2)/281.561*298.147, '2019', 'conservative estimate'),
    (2018, 32_000/12 - 1646/2, 'Nominal', 'conservative estimate'),
    (2018, (32_000/12 - 1646/2)/290.076*298.147, '2019', 'conservative estimate'),
    (2019, 33_000/12 - 1712/2, 'Nominal', 'conservative estimate'),
    (2019, 33_000/12 - 1712/2, '2019', 'conservative estimate')
], columns=['Year', 'USD', 'Dollars', 'Certainty'])

def parse_arguments():
    parser = ArgumentParser(description = 'plot historical bisb stipend')
    parser.add_argument(
        'output_dir',
        metavar='<path/to/output_dir/>',
        help='path to output file'
    )
    return parser.parse_args()

def main():
    args = parse_arguments()
    sns.set(context='talk', style='white')
    
    ax = sns.lineplot(
        x='Year',
        y='USD',
        hue='Dollars',
        data=STIPEND
    )
    ax.set_title('BISB annual stipend')
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(f'{args.output_dir}/stipend.svg')
    fig.clf()

    ax = sns.lineplot(
        x='Year',
        y='USD',
        hue='Dollars',
        style='Certainty',
        data=RENT
    )
    ax.set_title('Median rent in San Diego metro area')
    ax.get_legend().remove()
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(f'{args.output_dir}/rent.svg')
    fig.clf()

    ax = sns.lineplot(
        x='Year',
        y='USD',
        hue='Dollars',
        style='Certainty',
        data=STIPEND_AFTER_RENT
    )
    ax.set_title('Monthly stipend after subtracting rent')
    ax.get_legend().remove()
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(f'{args.output_dir}/stipend-after-rent.svg')


if __name__ == '__main__':
    main()