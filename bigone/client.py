from . base import Request


class BigOneClient(Request):
    #  public methods
    
    def get_ticker(self, market):
        """Fetches ticker info of given asset pair.

        Args:
            asset_pair_name: asset pair id, e.g.: BTC-USDT

        Returns:
            Ticker info

        Doc: 
            https://open.bigone.com/docs/spot_tickers.html#ticker-of-one-asset-pair
        """
        return self.public_get('asset_pairs/%s/ticker' % market, 'Ticker')

    def get_multi_tickers(self, pair_names):
        """Fetches tickers info of multiple given asset pairs.

        Args:
            pair_names: names of asset pair, separated by comma, e.g.: BTC-USDT,PCX-BTC,GXC-USDT

        Returns:
            Tickers info

        Doc: 
            https://open.bigone.com/docs/spot_tickers.html#ticker-of-multiple-asset-pairs
        """
        params = {
            'pair_names': pair_names,
        }
        return self.public_get('asset_pairs/tickers', 'Ticker', params)
    
    def get_order_book(self, market, **page_options):
        """Fetches order book of given asset pair.

        Args:
            asset_pair_name: path arg, names of asset pair, e.g.: BTC-USDT
            limit: parameter arg, default 50, max 200

        Returns:
            Order book

        Doc: 
            https://open.bigone.com/docs/spot_order_books.html#orderbook-of-a-asset-pair
        """
        return self.public_get('asset_pairs/%s/depth' % market, 'OrderBook', page_options)
    
    def get_trades(self, market):
        """Fetches trades of given asset pair.

        Only returns 50 latest trades

        Args:
            asset_pair_name: path arg, names of asset pair, e.g.: BTC-USDT

        Returns:
            Trades info

        Doc: 
            https://open.bigone.com/docs/spot_asset_pair_trade.html#trades-of-a-asset-pair
        """
        return self.public_get('asset_pairs/%s/trades' % market, 'Trade')
    
    def get_candles(self, market, **page_options):
        """Fetches candles of given asset pair.

        Args:
            asset_pair_name: path arg, names of asset pair, e.g.: BTC-USDT
            period: day1, hour1, hour12, hour3, hour4, hour6, min1, min15, min30, min5, month1, week1
            time: latest time of candle, use current time by default, ISO 8601 format
            limit: default 100, max 500

        Returns:
            Candles info

        Doc: 
            https://open.bigone.com/docs/spot_asset_pair_candle.html#candles-of-a-asset-pair
        """
        return self.public_get('asset_pairs/%s/candles' % market, 'Candle')
    
    def get_asset_pairs(self):
        """Fetches all asset pairs.

        Returns:
            AssetPair info

        Doc: 
            https://open.bigone.com/docs/spot_asset_pair.html#all-assetpairs
        """
        return self.public_get('asset_pairs', 'Market')

    # private methods

    def spot_account_assets_balance(self):
        """Fetches spot account balance of all assets.

        Returns:
            Account balance info

        Doc: 
            https://open.bigone.com/docs/spot_accounts.html#balance-of-all-assets
        """
        return self.private_get('viewer/accounts', 'Account')
    
    def spot_account_asset_balance(self, asset):
        """Fetches spot account balance of given asset.

        Args:
            asset_symbol: path arg, e.g.: BTC

        Returns:
            Account balance info

        Doc: 
            https://open.bigone.com/docs/spot_accounts.html#balance-of-one-asset
        """
        return self.private_get('viewer/accounts/%s' % asset, 'Account')
    
    def fund_account_assets_balance(self):
        """Fetches fund account balance of all assets.

        Returns:
            Account balance info

        Doc: 
            https://open.bigone.com/docs/fund_accounts.html#balance-of-all-assets
        """
        return self.private_get('viewer/fund/accounts', 'Account')
    
    def fund_account_asset_balance(self, asset):
        """Fetches fund account balance of given asset.

        Args:
            asset_symbol: path arg, e.g.: BTC

        Returns:
            Account balance info

        Doc: 
            https://open.bigone.com/docs/fund_accounts.html#balance-of-one-asset
        """
        return self.private_get('viewer/fund/accounts/%s' % asset, 'Account')
    
    def get_orders(self, market=None, side=None, state=None, 
            **page_options):
        """Fetches user orders.

        Args:
            asset_pair_name: e.g.: BTC-USDT
            side: order side, one of `ASK`,`BID`
            state: order state, one of `PENDING`,`OPENING`,`CLOSED`,`NONE_FILLED`,`ALL`. default is `PENDING`. `CLOSED` as a query parameter indicates order state `FILLED` and `CANCELLED`. `OPENING` or `PENDING` as a query parameter indicates order state `FIRED` and `PENDING`; `NONE_FILLED` is used for querying the orders which state is closed and filled amount is zero. ALL return customer all orders
            page_token: request page after this page token
            limit: default 20, max 200

        Returns:
            Order info

        Doc: 
            https://open.bigone.com/docs/spot_orders.html#get-user-orders-in-one-asset-pair
        """
        params = {
            'side': side,
            'state': state,
            'asset_pair_name': market
        }
        params.update(page_options)
        return self.private_get('viewer/orders', 'Order', params)
    
    def order_detail(self, order_id):
        """Fetches order by id.

        Args:
            id: path arg. order id

        Returns:
            Order info

        Doc: 
            https://open.bigone.com/docs/spot_orders.html#get-one-order
        """
        return self.private_get('viewer/orders/%s' % order_id, 'Order')
    
    def create_order(self, market, side, price, amount, type, stop_price, operator, immediate_or_cancel, post_only, client_order_id):
        """Create order.

        Args:
            asset_pair_name:  asset pair name, e.g.: BTC-USDT
            side: order side, one of ASK,BID    
            price: order price    
            amount:  must larger than 0    
            type:  order type, one of LIMIT,MARKET,STOP_LIMIT,STOP_MARKET, default LIMIT    
            stop_price:  must larger than 0, only for stop order. in BID side, price cannot be higher than 110% of the stop_price; in ASK side, price cannot be lower than 90% of the stop_price    
            operator:  operator, one of GTE,LTE, only for stop order, GTE(>=) – greater than or equal to, LTE(<=) – less than or equal to    
            immediate_or_cancel:  only use with LIMIT type, must be false when post_only is true    
            post_only:  only use with LIMIT type, must be false when immediate_or_cancel is true    
            client_order_id:  must match ^[a-zA-Z0-9-_]{1,36}$ this regex. client_order_id is unique in 24 hours, If created 24 hours later and the order closed, it will be released and can be reused

        Returns:
            Order info

        Doc: 
            https://open.bigone.com/docs/spot_orders.html#create-order
        """
        return self.private_post('viewer/orders', 'Order', {
            'asset_pair_name': market,
            'side': side,
            'price': price,
            'amount': amount,
            "type": type,
            "stop_price": stop_price,
            "operator": operator,
            "immediate_or_cancel": immediate_or_cancel,
            "post_only": post_only,
            "client_order_id": client_order_id,
        })
    
    def cancel_order(self, order_id):
        """Cancel order by id.

        Args:
            id: path arg. order id

        Returns:
            Order info

        Doc: 
            https://open.bigone.com/docs/spot_orders.html#cancel-order
        """
        return self.private_post('viewer/orders/%s/cancel' % order_id,
                                 'Order')
    
    def cancel_all_order(self, market):
        """Cancel all given asset pair orders.

        Args:
            asset_pair_name: e.g.: BTC-USDT

        Returns:
            Order info

        Doc: 
            https://open.bigone.com/docs/spot_orders.html#cancel-all-orders
        """
        params = {
            'asset_pair_name': market
        }
        return self.private_post('viewer/orders/cancel_all', 'Order', params)
    
    def my_trades(self, market=None, **page_options):
        """Fetches user trades of given asset pair.

        Args:
            asset_pair_name: names of asset pair, e.g.: BTC-USDT
            page_token: request page after this page token
            limit: default 20, max 200

        Returns:
            Trades info

        Doc: 
            https://open.bigone.com/docs/spot_asset_pair_trade.html#trades-of-a-asset-pair
        """
        params = {
            'asset_pair_name': market
        }
        params.update(page_options)
        return self.private_get('viewer/trades', 'Trade', params)

    def my_withdrawals(self, asset_symbol, kind, **page_options):
        params = {
            'asset_symbol': asset_symbol,
            "kind": kind,
        }
        params.update(page_options)
        return self.private_get('viewer/withdrawals', 'Withdrawal',
                                params)
    
    def get_withdrawal(self, id):
        return self.private_get('viewer/withdrawals/%s' % id, 'Withdrawal')
    
    def create_withdrawal(self, symbol, target_address, amount, memo, guid, gateway_name):
        params = {
            "symbol": symbol,
            "target_address": target_address,
            "amount": amount,
            "memo": memo,
            "guid": guid,
            "gateway_name": gateway_name,
        }
        return self.private_post('viewer/withdrawals', 'Withdrawal', params)
    
    def cancel_withdrawal(self, id):
        return self.private_post('viewer/withdrawals/%s/cancel' % id, 'Common')
    
    def my_deposits(self, asset_symbol, kind, **page_options):
        params = {
            'asset_symbol': asset_symbol,
            "kind": kind,
        }
        params.update(page_options)
        return self.private_get('viewer/deposits', 'Deposit', params)
    
    def get_deposit_address(self, asset_symbol):
        return self.private_get('viewer/assets/%s/address' % asset_symbol, 'DepositAddress')
    
    def my_transfer(self, symbol, amount, guid, from_acc_type, to_acc_type, type, sub_account):
        params = {
            'symbol': symbol,
            "amount": amount,
            "guid": guid,
            "from": from_acc_type,
            "to": to_acc_type,
            "type": type,
            "sub_account": sub_account,
        }
        return self.private_get('viewer/transfer', 'Common', params)
    
    def my_trading_fee(self, asset_pair_names):
        params = {
            'asset_pair_names': asset_pair_names,
        }
        return self.private_get('/viewer/trading_fees', 'TradingFee', params)
