import pandas as pd
import seaborn as sns
from argparse import ArgumentParser


# CPI-U for San Diego-Carlsbad (first half of the year). Original data source:
# https://data.bls.gov/timeseries/CUURS49ESA0
CPI = {
    2013: 258.955,
    2014: 265.251,
    2015: 267.346,
    2016: 272.628,
    2017: 281.561,
    2018: 290.076,
    2019: 298.147
}

# Annual stipend for BISB. Original data source:
# http://web.archive.org/web/*/https://bioinformatics.ucsd.edu/node/18
STIPEND = pd.DataFrame([
    (2013, 28_500, 'Nominal'),
    (2013, 28_500 / CPI[2013] * CPI[2019], '2019'),
    (2014, 28_500, 'Nominal'),
    (2014, 28_500 / CPI[2014] * CPI[2019], '2019'),
    (2015, 30_000, 'Nominal'),
    (2015, 30_000 / CPI[2015] * CPI[2019], '2019'),
    (2016, 32_000, 'Nominal'),
    (2016, 32_000 / CPI[2016] * CPI[2019], '2019'),
    (2017, 32_000, 'Nominal'),
    (2017, 32_000 / CPI[2017] * CPI[2019], '2019'),
    (2018, 32_000, 'Nominal'),
    (2018, 32_000 / CPI[2018] * CPI[2019], '2019'),
    (2019, 33_000, 'Nominal'),
    (2019, 33_000, '2019'),
], columns=['Year', 'USD', 'Dollars',])

# Median rent in San Diego-Carlsbad-San Marcos metro area. Original Data source:
# https://www.deptofnumbers.com/rent/california/san-diego/
RENT = pd.DataFrame([
    (2013, 1289, 'Nominal', 'record'),
    (2013, 1289 / CPI[2013] * CPI[2019], '2019', 'record'),
    (2014, 1373, 'Nominal', 'record'),
    (2014, 1373 / CPI[2014] * CPI[2019], '2019', 'record'),
    (2015, 1427, 'Nominal', 'record'),
    (2015, 1427 / CPI[2015] * CPI[2019], '2019', 'record'),
    (2016, 1504, 'Nominal', 'record'),
    (2016, 1504 / CPI[2016] * CPI[2019], '2019', 'record'),
    (2017, 1598, 'Nominal', 'record'),
    (2017, 1598 / CPI[2017] * CPI[2019], '2019', 'record'),
    (2017, 1598, 'Nominal', 'conservative estimate'),
    (2017, 1598 / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2018, 1646, 'Nominal', 'conservative estimate'),
    (2018, 1646 / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
    (2019, 1712, 'Nominal', 'conservative estimate'),
    (2019, 1712, '2019', 'conservative estimate')
], columns=['Year', 'USD', 'Dollars', 'Certainty'])

STIPEND_AFTER_RENT = pd.DataFrame([
    (2013, 28_500/12 - 1289/2, 'Nominal', 'record'),
    (2013, (28_500/12 - 1289/2) / CPI[2013] * CPI[2019], '2019', 'record'),
    (2014, 28_500/12 - 1373/2, 'Nominal', 'record'),
    (2014, (28_500/12 - 1373/2) / CPI[2014] * CPI[2019], '2019', 'record'),
    (2015, 30_000/12 - 1427/2, 'Nominal', 'record'),
    (2015, (30_000/12 - 1427/2) / CPI[2015] * CPI[2019], '2019', 'record'),
    (2016, 32_000/12 - 1504/2, 'Nominal', 'record'),
    (2016, (32_000/12 - 1504/2) / CPI[2016] * CPI[2019], '2019', 'record'),
    (2017, 32_000/12 - 1598/2, 'Nominal', 'record'),
    (2017, (32_000/12 - 1598/2) / CPI[2017] * CPI[2019], '2019', 'record'),
    (2017, 32_000/12 - 1598/2, 'Nominal', 'conservative estimate'),
    (2017, (32_000/12 - 1598/2) / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2018, 32_000/12 - 1646/2, 'Nominal', 'conservative estimate'),
    (2018, (32_000/12 - 1646/2) / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
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
