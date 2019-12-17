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
    (2019, 33_000, '2019')
], columns=['Year', 'USD', 'Dollars',])

STIPEND_TO_2020 = pd.DataFrame([
    (2013, 28_500, 'Nominal', 'record'),
    (2013, 28_500 / CPI[2013] * CPI[2019], '2019', 'record'),
    (2014, 28_500, 'Nominal', 'record'),
    (2014, 28_500 / CPI[2014] * CPI[2019], '2019', 'record'),
    (2015, 30_000, 'Nominal', 'record'),
    (2015, 30_000 / CPI[2015] * CPI[2019], '2019', 'record'),
    (2016, 32_000, 'Nominal', 'record'),
    (2016, 32_000 / CPI[2016] * CPI[2019], '2019', 'record'),
    (2017, 32_000, 'Nominal'),
    (2017, 32_000 / CPI[2017] * CPI[2019], '2019', 'record'),
    (2018, 32_000, 'Nominal', 'record'),
    (2018, 32_000 / CPI[2018] * CPI[2019], '2019', 'record'),
    (2019, 33_000, 'Nominal', 'record'),
    (2019, 33_000, '2019', 'record'),
    (2019, 33_000, 'Nominal', 'estimate'),
    (2019, 33_000, '2019', 'estimate'),
    (2020, 33_000, 'Nominal', 'estimate'),
    (2020, 33_000 / CPI[2019] * CPI[2018], '2019', 'estimate')
], columns=['Year', 'USD', 'Dollars', 'Certainty'])

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
    (2017, 1598, 'Nominal', 'conservative estimate'),
    (2017, 1598, 'Nominal', 'conservative estimate'),
    (2017, 1598 / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2017, 1598 / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2017, 1598 / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2018, 1646, 'Nominal', 'conservative estimate'),
    (2018, 1661, 'Nominal', 'conservative estimate'),
    (2018, 1678, 'Nominal', 'conservative estimate'),
    (2018, 1646 / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
    (2018, 1661 / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
    (2018, 1678 / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
    (2019, 1695, 'Nominal', 'conservative estimate'),
    (2019, 1727, 'Nominal', 'conservative estimate'),
    (2019, 1762, 'Nominal', 'conservative estimate'),
    (2019, 1695, '2019', 'conservative estimate'),
    (2019, 1727, '2019', 'conservative estimate'),
    (2019, 1762, '2019', 'conservative estimate'),
    
    (2020, 1746, 'Nominal', 'conservative estimate'),
    (2020, 1796, 'Nominal', 'conservative estimate'),
    (2020, 1850, 'Nominal', 'conservative estimate'),
    (2020, 1746 / CPI[2019] * CPI[2018], '2019', 'conservative estimate'),
    (2020, 1796 / CPI[2019] * CPI[2018], '2019', 'conservative estimate'),
    (2020, 1850 / CPI[2019] * CPI[2018], '2019', 'conservative estimate')
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
    (2017, 32_000/12 - 1598/2, 'Nominal', 'conservative estimate'),
    (2017, 32_000/12 - 1598/2, 'Nominal', 'conservative estimate'),
    (2017, (32_000/12 - 1598/2) / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2017, (32_000/12 - 1598/2) / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2017, (32_000/12 - 1598/2) / CPI[2017] * CPI[2019], '2019', 'conservative estimate'),
    (2018, 32_000/12 - 1646/2, 'Nominal', 'conservative estimate'),
    (2018, 32_000/12 - 1661/2, 'Nominal', 'conservative estimate'),
    (2018, 32_000/12 - 1678/2, 'Nominal', 'conservative estimate'),
    (2018, (32_000/12 - 1646/2) / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
    (2018, (32_000/12 - 1661/2) / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
    (2018, (32_000/12 - 1678/2) / CPI[2018] * CPI[2019], '2019', 'conservative estimate'),
    (2019, 33_000/12 - 1695/2, 'Nominal', 'conservative estimate'),
    (2019, 33_000/12 - 1727/2, 'Nominal', 'conservative estimate'),
    (2019, 33_000/12 - 1762/2, 'Nominal', 'conservative estimate'),
    (2019, 33_000/12 - 1695/2, '2019', 'conservative estimate'),
    (2019, 33_000/12 - 1727/2, '2019', 'conservative estimate'),
    (2019, 33_000/12 - 1762/2, '2019', 'conservative estimate'),

    (2020, 33_000/12 - 1746/2, 'Nominal', 'conservative estimate'),
    (2020, 33_000/12 - 1796/2, 'Nominal', 'conservative estimate'),
    (2020, 33_000/12 - 1850/2, 'Nominal', 'conservative estimate'),
    (2020, (33_000/12 - 1746/2) / CPI[2019] * CPI[2018], '2019', 'conservative estimate'),
    (2020, (33_000/12 - 1796/2) / CPI[2019] * CPI[2018], '2019', 'conservative estimate'),
    (2020, (33_000/12 - 1850/2) / CPI[2019] * CPI[2018], '2019', 'conservative estimate'),

], columns=['Year', 'USD', 'Dollars', 'Certainty'])

RENT_AS_FRACTION = pd.DataFrame([
    (2013, (1289/2)/(28_500/12) * 100, 'record'),
    (2014, (1373/2)/(28_500/12) * 100, 'record'),
    (2015, (1427/2)/(30_000/12) * 100, 'record'),
    (2016, (1504/2)/(32_000/12) * 100, 'record'),
    (2017, (1598/2)/(32_000/12) * 100, 'record'),
    (2017, (1598/2)/(32_000/12) * 100, 'conservative estimate'),
    (2017, (1598/2)/(32_000/12) * 100, 'conservative estimate'),
    (2017, (1598/2)/(32_000/12) * 100, 'conservative estimate'),
    (2017, (1598/2)/(32_000/12) * 100, 'conservative estimate'),
    (2018, (1646/2)/(32_000/12) * 100, 'conservative estimate'),
    (2018, (1661/2)/(32_000/12) * 100, 'conservative estimate'),
    (2018, (1678/2)/(32_000/12) * 100, 'conservative estimate'),
    (2019, (1695/2)/(33_000/12) * 100, 'conservative estimate'),
    (2019, (1727/2)/(33_000/12) * 100, 'conservative estimate'),
    (2019, (1762/2)/(33_000/12) * 100, 'conservative estimate'),

    (2020, (1746/2)/(33_000/12) * 100, 'conservative estimate'),
    (2020, (1796/2)/(33_000/12) * 100, 'conservative estimate'),
    (2020, (1850/2)/(33_000/12) * 100, 'conservative estimate'),
], columns=['Year', 'Percent', 'Certainty'])

def parse_arguments():
    parser = ArgumentParser(description = 'plot historical bisb stipend')
    parser.add_argument(
        'output_dir',
        metavar='<path/to/output_dir/>',
        help='path to output directory'
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
    STIPEND.to_csv(f'{args.output_dir}/stipend.csv', index=False)

    ax = sns.lineplot(
        x='Year',
        y='USD',
        hue='Dollars',
        style='Certainty',
        data=STIPEND_TO_2020
    )
    ax.set_title('BISB annual stipend')
    ax.get_legend().remove()
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(f'{args.output_dir}/stipend-2020.svg')
    fig.clf()
    STIPEND_TO_2020.to_csv(f'{args.output_dir}/stipend-2020.csv', index=False)

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
    RENT.to_csv(f'{args.output_dir}/rent.csv', index=False)

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
    fig.clf()
    STIPEND_AFTER_RENT.to_csv(f'{args.output_dir}/stipend-after-rent.csv', index=False)

    ax = sns.lineplot(
        x='Year',
        y='Percent',
        style='Certainty',
        hue='Certainty',
        palette=[sns.color_palette()[2]] * 2,
        data=RENT_AS_FRACTION
    )
    ax.set_title('Half of median rent as fraction of monthly stipend')
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(f'{args.output_dir}/rent-as-fraction.svg')
    RENT_AS_FRACTION.to_csv(f'{args.output_dir}/rent-as-fraction.csv', index=False)


if __name__ == '__main__':
    main()
