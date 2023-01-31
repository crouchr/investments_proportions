# Notes
#

from pprint import pprint
import time


def main(funds):

    target = {}
    sipp_investec = {}
    safe = {}

    # ----------
    # Categories
    # ----------
    # High risk = 20%
    target['crypto_category'] = funds * 0.05                # high risk
    target['foreign_indices_category'] = 0.02 * funds       # high risk
    target['silver_gold_miners_category'] = 0.1 * funds     # high risk

    # Medium risk = 80%
    target['uranium_category'] = 0.08 * funds               # medium risk
    target['electrification_category'] = 0.05 * funds       # medium risk
    target['gold_silver_base_category'] = 0.7 * funds       # medium risk

    # --------------
    # Sub-Categories
    # --------------
    # Base gold and silver
    target['gdx_etf'] = 0.20 * target['gold_silver_base_category']
    target['gdxj_etf'] = 0.20 * target['gold_silver_base_category']
    target['paas_silver_producer'] = 0.20 * target['gold_silver_base_category']
    target['hecla_silver_producer'] = 0.20 * target['gold_silver_base_category']
    target['silg_etf'] = 0.20 * target['gold_silver_base_category']

    # Risky gold / silver miners
    target['gold_miners_individual_shares'] = target['silver_gold_miners_category'] * 0.25
    target['gold_miner_X_of_5'] = target['gold_miners_individual_shares'] * 0.2
    target['silver_miners_individual_shares'] = target['silver_gold_miners_category'] * 0.75
    target['silver_miner_X_of_10'] = target['silver_miners_individual_shares'] * 0.1

    # Crypto (Risky)
    target['btc'] = target['crypto_category'] * 0.6
    target['xmr'] = target['crypto_category'] * 0.4

    # Uranium
    target['uranium_sprott_physical_trust'] = target['uranium_category'] * 0.35
    target['uranium_etf'] = target['uranium_category'] * 0.65

    # Foreign ETFs - Market Sniper YouTube episode
    target['israel_etf'] = target['foreign_indices_category'] * 0.3        # tech
    target['singapore_etf'] = target['foreign_indices_category'] * 0.3     # china
    target['saudi_etf'] = target['foreign_indices_category'] * 0.2
    target['turkey_etf'] = target['foreign_indices_category'] * 0.2

    # Electrification / Green
    target['ev_battery_etf'] = target['electrification_category'] * 0.5
    target['copper_miners_etf'] = target['electrification_category'] * 0.5

    sipp_investec['sipp_vaulted_gold'] = 50000
    safe['gold_bullion'] = 20000
    safe['silver_bullion'] = 5000
    safe['cash_gbp'] = 4000

    return target, sipp_investec, safe


if __name__ == '__main__':
    hl_sipp = 50000
    hl_stocks = 250
    march_shares = 0

    funds = hl_sipp + hl_stocks + march_shares

    target, sipp_investacc, safe = main(funds)

    # Display results
    print()
    print(time.ctime())
    print()
    print(f'H&L SIPP          : {hl_sipp}')
    print(f'H&L Stocks        : {hl_stocks}')
    print(f'March Shares      : {march_shares}')
    print('-------------------------')
    print(f'TOTAL funds (GBP) : {funds}')
    print('-------------------------')
    print()
    print('allocation targets (GBP)')
    print('------------------------')
    pprint(target)
    print()
    print('assets (GBP)')
    print('------------')
    print(safe)
    print(sipp_investacc)