#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SnapshotDTO(object):

    def __init__(self):
        self._after_market_amount = None
        self._after_market_buy_volume = None
        self._after_market_price = None
        self._after_market_sell_volume = None
        self._after_market_trade_time = None
        self._after_market_trading_phase = None
        self._after_market_volume = None
        self._amount = None
        self._ask_price_1 = None
        self._ask_price_10 = None
        self._ask_price_2 = None
        self._ask_price_3 = None
        self._ask_price_4 = None
        self._ask_price_5 = None
        self._ask_price_6 = None
        self._ask_price_7 = None
        self._ask_price_8 = None
        self._ask_price_9 = None
        self._ask_volume_1 = None
        self._ask_volume_10 = None
        self._ask_volume_2 = None
        self._ask_volume_3 = None
        self._ask_volume_4 = None
        self._ask_volume_5 = None
        self._ask_volume_6 = None
        self._ask_volume_7 = None
        self._ask_volume_8 = None
        self._ask_volume_9 = None
        self._bid_price_1 = None
        self._bid_price_10 = None
        self._bid_price_2 = None
        self._bid_price_3 = None
        self._bid_price_4 = None
        self._bid_price_5 = None
        self._bid_price_6 = None
        self._bid_price_7 = None
        self._bid_price_8 = None
        self._bid_price_9 = None
        self._bid_volume_1 = None
        self._bid_volume_10 = None
        self._bid_volume_2 = None
        self._bid_volume_3 = None
        self._bid_volume_4 = None
        self._bid_volume_5 = None
        self._bid_volume_6 = None
        self._bid_volume_7 = None
        self._bid_volume_8 = None
        self._bid_volume_9 = None
        self._change_percent = None
        self._change_price = None
        self._close_price = None
        self._date = None
        self._down_price = None
        self._high_price = None
        self._low_price = None
        self._name = None
        self._open_price = None
        self._previous_close = None
        self._price = None
        self._suspension_state = None
        self._symbol = None
        self._trade_state = None
        self._up_price = None
        self._volume = None

    @property
    def after_market_amount(self):
        return self._after_market_amount

    @after_market_amount.setter
    def after_market_amount(self, value):
        self._after_market_amount = value
    @property
    def after_market_buy_volume(self):
        return self._after_market_buy_volume

    @after_market_buy_volume.setter
    def after_market_buy_volume(self, value):
        self._after_market_buy_volume = value
    @property
    def after_market_price(self):
        return self._after_market_price

    @after_market_price.setter
    def after_market_price(self, value):
        self._after_market_price = value
    @property
    def after_market_sell_volume(self):
        return self._after_market_sell_volume

    @after_market_sell_volume.setter
    def after_market_sell_volume(self, value):
        self._after_market_sell_volume = value
    @property
    def after_market_trade_time(self):
        return self._after_market_trade_time

    @after_market_trade_time.setter
    def after_market_trade_time(self, value):
        self._after_market_trade_time = value
    @property
    def after_market_trading_phase(self):
        return self._after_market_trading_phase

    @after_market_trading_phase.setter
    def after_market_trading_phase(self, value):
        self._after_market_trading_phase = value
    @property
    def after_market_volume(self):
        return self._after_market_volume

    @after_market_volume.setter
    def after_market_volume(self, value):
        self._after_market_volume = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ask_price_1(self):
        return self._ask_price_1

    @ask_price_1.setter
    def ask_price_1(self, value):
        self._ask_price_1 = value
    @property
    def ask_price_10(self):
        return self._ask_price_10

    @ask_price_10.setter
    def ask_price_10(self, value):
        self._ask_price_10 = value
    @property
    def ask_price_2(self):
        return self._ask_price_2

    @ask_price_2.setter
    def ask_price_2(self, value):
        self._ask_price_2 = value
    @property
    def ask_price_3(self):
        return self._ask_price_3

    @ask_price_3.setter
    def ask_price_3(self, value):
        self._ask_price_3 = value
    @property
    def ask_price_4(self):
        return self._ask_price_4

    @ask_price_4.setter
    def ask_price_4(self, value):
        self._ask_price_4 = value
    @property
    def ask_price_5(self):
        return self._ask_price_5

    @ask_price_5.setter
    def ask_price_5(self, value):
        self._ask_price_5 = value
    @property
    def ask_price_6(self):
        return self._ask_price_6

    @ask_price_6.setter
    def ask_price_6(self, value):
        self._ask_price_6 = value
    @property
    def ask_price_7(self):
        return self._ask_price_7

    @ask_price_7.setter
    def ask_price_7(self, value):
        self._ask_price_7 = value
    @property
    def ask_price_8(self):
        return self._ask_price_8

    @ask_price_8.setter
    def ask_price_8(self, value):
        self._ask_price_8 = value
    @property
    def ask_price_9(self):
        return self._ask_price_9

    @ask_price_9.setter
    def ask_price_9(self, value):
        self._ask_price_9 = value
    @property
    def ask_volume_1(self):
        return self._ask_volume_1

    @ask_volume_1.setter
    def ask_volume_1(self, value):
        self._ask_volume_1 = value
    @property
    def ask_volume_10(self):
        return self._ask_volume_10

    @ask_volume_10.setter
    def ask_volume_10(self, value):
        self._ask_volume_10 = value
    @property
    def ask_volume_2(self):
        return self._ask_volume_2

    @ask_volume_2.setter
    def ask_volume_2(self, value):
        self._ask_volume_2 = value
    @property
    def ask_volume_3(self):
        return self._ask_volume_3

    @ask_volume_3.setter
    def ask_volume_3(self, value):
        self._ask_volume_3 = value
    @property
    def ask_volume_4(self):
        return self._ask_volume_4

    @ask_volume_4.setter
    def ask_volume_4(self, value):
        self._ask_volume_4 = value
    @property
    def ask_volume_5(self):
        return self._ask_volume_5

    @ask_volume_5.setter
    def ask_volume_5(self, value):
        self._ask_volume_5 = value
    @property
    def ask_volume_6(self):
        return self._ask_volume_6

    @ask_volume_6.setter
    def ask_volume_6(self, value):
        self._ask_volume_6 = value
    @property
    def ask_volume_7(self):
        return self._ask_volume_7

    @ask_volume_7.setter
    def ask_volume_7(self, value):
        self._ask_volume_7 = value
    @property
    def ask_volume_8(self):
        return self._ask_volume_8

    @ask_volume_8.setter
    def ask_volume_8(self, value):
        self._ask_volume_8 = value
    @property
    def ask_volume_9(self):
        return self._ask_volume_9

    @ask_volume_9.setter
    def ask_volume_9(self, value):
        self._ask_volume_9 = value
    @property
    def bid_price_1(self):
        return self._bid_price_1

    @bid_price_1.setter
    def bid_price_1(self, value):
        self._bid_price_1 = value
    @property
    def bid_price_10(self):
        return self._bid_price_10

    @bid_price_10.setter
    def bid_price_10(self, value):
        self._bid_price_10 = value
    @property
    def bid_price_2(self):
        return self._bid_price_2

    @bid_price_2.setter
    def bid_price_2(self, value):
        self._bid_price_2 = value
    @property
    def bid_price_3(self):
        return self._bid_price_3

    @bid_price_3.setter
    def bid_price_3(self, value):
        self._bid_price_3 = value
    @property
    def bid_price_4(self):
        return self._bid_price_4

    @bid_price_4.setter
    def bid_price_4(self, value):
        self._bid_price_4 = value
    @property
    def bid_price_5(self):
        return self._bid_price_5

    @bid_price_5.setter
    def bid_price_5(self, value):
        self._bid_price_5 = value
    @property
    def bid_price_6(self):
        return self._bid_price_6

    @bid_price_6.setter
    def bid_price_6(self, value):
        self._bid_price_6 = value
    @property
    def bid_price_7(self):
        return self._bid_price_7

    @bid_price_7.setter
    def bid_price_7(self, value):
        self._bid_price_7 = value
    @property
    def bid_price_8(self):
        return self._bid_price_8

    @bid_price_8.setter
    def bid_price_8(self, value):
        self._bid_price_8 = value
    @property
    def bid_price_9(self):
        return self._bid_price_9

    @bid_price_9.setter
    def bid_price_9(self, value):
        self._bid_price_9 = value
    @property
    def bid_volume_1(self):
        return self._bid_volume_1

    @bid_volume_1.setter
    def bid_volume_1(self, value):
        self._bid_volume_1 = value
    @property
    def bid_volume_10(self):
        return self._bid_volume_10

    @bid_volume_10.setter
    def bid_volume_10(self, value):
        self._bid_volume_10 = value
    @property
    def bid_volume_2(self):
        return self._bid_volume_2

    @bid_volume_2.setter
    def bid_volume_2(self, value):
        self._bid_volume_2 = value
    @property
    def bid_volume_3(self):
        return self._bid_volume_3

    @bid_volume_3.setter
    def bid_volume_3(self, value):
        self._bid_volume_3 = value
    @property
    def bid_volume_4(self):
        return self._bid_volume_4

    @bid_volume_4.setter
    def bid_volume_4(self, value):
        self._bid_volume_4 = value
    @property
    def bid_volume_5(self):
        return self._bid_volume_5

    @bid_volume_5.setter
    def bid_volume_5(self, value):
        self._bid_volume_5 = value
    @property
    def bid_volume_6(self):
        return self._bid_volume_6

    @bid_volume_6.setter
    def bid_volume_6(self, value):
        self._bid_volume_6 = value
    @property
    def bid_volume_7(self):
        return self._bid_volume_7

    @bid_volume_7.setter
    def bid_volume_7(self, value):
        self._bid_volume_7 = value
    @property
    def bid_volume_8(self):
        return self._bid_volume_8

    @bid_volume_8.setter
    def bid_volume_8(self, value):
        self._bid_volume_8 = value
    @property
    def bid_volume_9(self):
        return self._bid_volume_9

    @bid_volume_9.setter
    def bid_volume_9(self, value):
        self._bid_volume_9 = value
    @property
    def change_percent(self):
        return self._change_percent

    @change_percent.setter
    def change_percent(self, value):
        self._change_percent = value
    @property
    def change_price(self):
        return self._change_price

    @change_price.setter
    def change_price(self, value):
        self._change_price = value
    @property
    def close_price(self):
        return self._close_price

    @close_price.setter
    def close_price(self, value):
        self._close_price = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def down_price(self):
        return self._down_price

    @down_price.setter
    def down_price(self, value):
        self._down_price = value
    @property
    def high_price(self):
        return self._high_price

    @high_price.setter
    def high_price(self, value):
        self._high_price = value
    @property
    def low_price(self):
        return self._low_price

    @low_price.setter
    def low_price(self, value):
        self._low_price = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def open_price(self):
        return self._open_price

    @open_price.setter
    def open_price(self, value):
        self._open_price = value
    @property
    def previous_close(self):
        return self._previous_close

    @previous_close.setter
    def previous_close(self, value):
        self._previous_close = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def suspension_state(self):
        return self._suspension_state

    @suspension_state.setter
    def suspension_state(self, value):
        self._suspension_state = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
    @property
    def trade_state(self):
        return self._trade_state

    @trade_state.setter
    def trade_state(self, value):
        self._trade_state = value
    @property
    def up_price(self):
        return self._up_price

    @up_price.setter
    def up_price(self, value):
        self._up_price = value
    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        self._volume = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_market_amount:
            if hasattr(self.after_market_amount, 'to_alipay_dict'):
                params['after_market_amount'] = self.after_market_amount.to_alipay_dict()
            else:
                params['after_market_amount'] = self.after_market_amount
        if self.after_market_buy_volume:
            if hasattr(self.after_market_buy_volume, 'to_alipay_dict'):
                params['after_market_buy_volume'] = self.after_market_buy_volume.to_alipay_dict()
            else:
                params['after_market_buy_volume'] = self.after_market_buy_volume
        if self.after_market_price:
            if hasattr(self.after_market_price, 'to_alipay_dict'):
                params['after_market_price'] = self.after_market_price.to_alipay_dict()
            else:
                params['after_market_price'] = self.after_market_price
        if self.after_market_sell_volume:
            if hasattr(self.after_market_sell_volume, 'to_alipay_dict'):
                params['after_market_sell_volume'] = self.after_market_sell_volume.to_alipay_dict()
            else:
                params['after_market_sell_volume'] = self.after_market_sell_volume
        if self.after_market_trade_time:
            if hasattr(self.after_market_trade_time, 'to_alipay_dict'):
                params['after_market_trade_time'] = self.after_market_trade_time.to_alipay_dict()
            else:
                params['after_market_trade_time'] = self.after_market_trade_time
        if self.after_market_trading_phase:
            if hasattr(self.after_market_trading_phase, 'to_alipay_dict'):
                params['after_market_trading_phase'] = self.after_market_trading_phase.to_alipay_dict()
            else:
                params['after_market_trading_phase'] = self.after_market_trading_phase
        if self.after_market_volume:
            if hasattr(self.after_market_volume, 'to_alipay_dict'):
                params['after_market_volume'] = self.after_market_volume.to_alipay_dict()
            else:
                params['after_market_volume'] = self.after_market_volume
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ask_price_1:
            if hasattr(self.ask_price_1, 'to_alipay_dict'):
                params['ask_price_1'] = self.ask_price_1.to_alipay_dict()
            else:
                params['ask_price_1'] = self.ask_price_1
        if self.ask_price_10:
            if hasattr(self.ask_price_10, 'to_alipay_dict'):
                params['ask_price_10'] = self.ask_price_10.to_alipay_dict()
            else:
                params['ask_price_10'] = self.ask_price_10
        if self.ask_price_2:
            if hasattr(self.ask_price_2, 'to_alipay_dict'):
                params['ask_price_2'] = self.ask_price_2.to_alipay_dict()
            else:
                params['ask_price_2'] = self.ask_price_2
        if self.ask_price_3:
            if hasattr(self.ask_price_3, 'to_alipay_dict'):
                params['ask_price_3'] = self.ask_price_3.to_alipay_dict()
            else:
                params['ask_price_3'] = self.ask_price_3
        if self.ask_price_4:
            if hasattr(self.ask_price_4, 'to_alipay_dict'):
                params['ask_price_4'] = self.ask_price_4.to_alipay_dict()
            else:
                params['ask_price_4'] = self.ask_price_4
        if self.ask_price_5:
            if hasattr(self.ask_price_5, 'to_alipay_dict'):
                params['ask_price_5'] = self.ask_price_5.to_alipay_dict()
            else:
                params['ask_price_5'] = self.ask_price_5
        if self.ask_price_6:
            if hasattr(self.ask_price_6, 'to_alipay_dict'):
                params['ask_price_6'] = self.ask_price_6.to_alipay_dict()
            else:
                params['ask_price_6'] = self.ask_price_6
        if self.ask_price_7:
            if hasattr(self.ask_price_7, 'to_alipay_dict'):
                params['ask_price_7'] = self.ask_price_7.to_alipay_dict()
            else:
                params['ask_price_7'] = self.ask_price_7
        if self.ask_price_8:
            if hasattr(self.ask_price_8, 'to_alipay_dict'):
                params['ask_price_8'] = self.ask_price_8.to_alipay_dict()
            else:
                params['ask_price_8'] = self.ask_price_8
        if self.ask_price_9:
            if hasattr(self.ask_price_9, 'to_alipay_dict'):
                params['ask_price_9'] = self.ask_price_9.to_alipay_dict()
            else:
                params['ask_price_9'] = self.ask_price_9
        if self.ask_volume_1:
            if hasattr(self.ask_volume_1, 'to_alipay_dict'):
                params['ask_volume_1'] = self.ask_volume_1.to_alipay_dict()
            else:
                params['ask_volume_1'] = self.ask_volume_1
        if self.ask_volume_10:
            if hasattr(self.ask_volume_10, 'to_alipay_dict'):
                params['ask_volume_10'] = self.ask_volume_10.to_alipay_dict()
            else:
                params['ask_volume_10'] = self.ask_volume_10
        if self.ask_volume_2:
            if hasattr(self.ask_volume_2, 'to_alipay_dict'):
                params['ask_volume_2'] = self.ask_volume_2.to_alipay_dict()
            else:
                params['ask_volume_2'] = self.ask_volume_2
        if self.ask_volume_3:
            if hasattr(self.ask_volume_3, 'to_alipay_dict'):
                params['ask_volume_3'] = self.ask_volume_3.to_alipay_dict()
            else:
                params['ask_volume_3'] = self.ask_volume_3
        if self.ask_volume_4:
            if hasattr(self.ask_volume_4, 'to_alipay_dict'):
                params['ask_volume_4'] = self.ask_volume_4.to_alipay_dict()
            else:
                params['ask_volume_4'] = self.ask_volume_4
        if self.ask_volume_5:
            if hasattr(self.ask_volume_5, 'to_alipay_dict'):
                params['ask_volume_5'] = self.ask_volume_5.to_alipay_dict()
            else:
                params['ask_volume_5'] = self.ask_volume_5
        if self.ask_volume_6:
            if hasattr(self.ask_volume_6, 'to_alipay_dict'):
                params['ask_volume_6'] = self.ask_volume_6.to_alipay_dict()
            else:
                params['ask_volume_6'] = self.ask_volume_6
        if self.ask_volume_7:
            if hasattr(self.ask_volume_7, 'to_alipay_dict'):
                params['ask_volume_7'] = self.ask_volume_7.to_alipay_dict()
            else:
                params['ask_volume_7'] = self.ask_volume_7
        if self.ask_volume_8:
            if hasattr(self.ask_volume_8, 'to_alipay_dict'):
                params['ask_volume_8'] = self.ask_volume_8.to_alipay_dict()
            else:
                params['ask_volume_8'] = self.ask_volume_8
        if self.ask_volume_9:
            if hasattr(self.ask_volume_9, 'to_alipay_dict'):
                params['ask_volume_9'] = self.ask_volume_9.to_alipay_dict()
            else:
                params['ask_volume_9'] = self.ask_volume_9
        if self.bid_price_1:
            if hasattr(self.bid_price_1, 'to_alipay_dict'):
                params['bid_price_1'] = self.bid_price_1.to_alipay_dict()
            else:
                params['bid_price_1'] = self.bid_price_1
        if self.bid_price_10:
            if hasattr(self.bid_price_10, 'to_alipay_dict'):
                params['bid_price_10'] = self.bid_price_10.to_alipay_dict()
            else:
                params['bid_price_10'] = self.bid_price_10
        if self.bid_price_2:
            if hasattr(self.bid_price_2, 'to_alipay_dict'):
                params['bid_price_2'] = self.bid_price_2.to_alipay_dict()
            else:
                params['bid_price_2'] = self.bid_price_2
        if self.bid_price_3:
            if hasattr(self.bid_price_3, 'to_alipay_dict'):
                params['bid_price_3'] = self.bid_price_3.to_alipay_dict()
            else:
                params['bid_price_3'] = self.bid_price_3
        if self.bid_price_4:
            if hasattr(self.bid_price_4, 'to_alipay_dict'):
                params['bid_price_4'] = self.bid_price_4.to_alipay_dict()
            else:
                params['bid_price_4'] = self.bid_price_4
        if self.bid_price_5:
            if hasattr(self.bid_price_5, 'to_alipay_dict'):
                params['bid_price_5'] = self.bid_price_5.to_alipay_dict()
            else:
                params['bid_price_5'] = self.bid_price_5
        if self.bid_price_6:
            if hasattr(self.bid_price_6, 'to_alipay_dict'):
                params['bid_price_6'] = self.bid_price_6.to_alipay_dict()
            else:
                params['bid_price_6'] = self.bid_price_6
        if self.bid_price_7:
            if hasattr(self.bid_price_7, 'to_alipay_dict'):
                params['bid_price_7'] = self.bid_price_7.to_alipay_dict()
            else:
                params['bid_price_7'] = self.bid_price_7
        if self.bid_price_8:
            if hasattr(self.bid_price_8, 'to_alipay_dict'):
                params['bid_price_8'] = self.bid_price_8.to_alipay_dict()
            else:
                params['bid_price_8'] = self.bid_price_8
        if self.bid_price_9:
            if hasattr(self.bid_price_9, 'to_alipay_dict'):
                params['bid_price_9'] = self.bid_price_9.to_alipay_dict()
            else:
                params['bid_price_9'] = self.bid_price_9
        if self.bid_volume_1:
            if hasattr(self.bid_volume_1, 'to_alipay_dict'):
                params['bid_volume_1'] = self.bid_volume_1.to_alipay_dict()
            else:
                params['bid_volume_1'] = self.bid_volume_1
        if self.bid_volume_10:
            if hasattr(self.bid_volume_10, 'to_alipay_dict'):
                params['bid_volume_10'] = self.bid_volume_10.to_alipay_dict()
            else:
                params['bid_volume_10'] = self.bid_volume_10
        if self.bid_volume_2:
            if hasattr(self.bid_volume_2, 'to_alipay_dict'):
                params['bid_volume_2'] = self.bid_volume_2.to_alipay_dict()
            else:
                params['bid_volume_2'] = self.bid_volume_2
        if self.bid_volume_3:
            if hasattr(self.bid_volume_3, 'to_alipay_dict'):
                params['bid_volume_3'] = self.bid_volume_3.to_alipay_dict()
            else:
                params['bid_volume_3'] = self.bid_volume_3
        if self.bid_volume_4:
            if hasattr(self.bid_volume_4, 'to_alipay_dict'):
                params['bid_volume_4'] = self.bid_volume_4.to_alipay_dict()
            else:
                params['bid_volume_4'] = self.bid_volume_4
        if self.bid_volume_5:
            if hasattr(self.bid_volume_5, 'to_alipay_dict'):
                params['bid_volume_5'] = self.bid_volume_5.to_alipay_dict()
            else:
                params['bid_volume_5'] = self.bid_volume_5
        if self.bid_volume_6:
            if hasattr(self.bid_volume_6, 'to_alipay_dict'):
                params['bid_volume_6'] = self.bid_volume_6.to_alipay_dict()
            else:
                params['bid_volume_6'] = self.bid_volume_6
        if self.bid_volume_7:
            if hasattr(self.bid_volume_7, 'to_alipay_dict'):
                params['bid_volume_7'] = self.bid_volume_7.to_alipay_dict()
            else:
                params['bid_volume_7'] = self.bid_volume_7
        if self.bid_volume_8:
            if hasattr(self.bid_volume_8, 'to_alipay_dict'):
                params['bid_volume_8'] = self.bid_volume_8.to_alipay_dict()
            else:
                params['bid_volume_8'] = self.bid_volume_8
        if self.bid_volume_9:
            if hasattr(self.bid_volume_9, 'to_alipay_dict'):
                params['bid_volume_9'] = self.bid_volume_9.to_alipay_dict()
            else:
                params['bid_volume_9'] = self.bid_volume_9
        if self.change_percent:
            if hasattr(self.change_percent, 'to_alipay_dict'):
                params['change_percent'] = self.change_percent.to_alipay_dict()
            else:
                params['change_percent'] = self.change_percent
        if self.change_price:
            if hasattr(self.change_price, 'to_alipay_dict'):
                params['change_price'] = self.change_price.to_alipay_dict()
            else:
                params['change_price'] = self.change_price
        if self.close_price:
            if hasattr(self.close_price, 'to_alipay_dict'):
                params['close_price'] = self.close_price.to_alipay_dict()
            else:
                params['close_price'] = self.close_price
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.down_price:
            if hasattr(self.down_price, 'to_alipay_dict'):
                params['down_price'] = self.down_price.to_alipay_dict()
            else:
                params['down_price'] = self.down_price
        if self.high_price:
            if hasattr(self.high_price, 'to_alipay_dict'):
                params['high_price'] = self.high_price.to_alipay_dict()
            else:
                params['high_price'] = self.high_price
        if self.low_price:
            if hasattr(self.low_price, 'to_alipay_dict'):
                params['low_price'] = self.low_price.to_alipay_dict()
            else:
                params['low_price'] = self.low_price
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.open_price:
            if hasattr(self.open_price, 'to_alipay_dict'):
                params['open_price'] = self.open_price.to_alipay_dict()
            else:
                params['open_price'] = self.open_price
        if self.previous_close:
            if hasattr(self.previous_close, 'to_alipay_dict'):
                params['previous_close'] = self.previous_close.to_alipay_dict()
            else:
                params['previous_close'] = self.previous_close
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.suspension_state:
            if hasattr(self.suspension_state, 'to_alipay_dict'):
                params['suspension_state'] = self.suspension_state.to_alipay_dict()
            else:
                params['suspension_state'] = self.suspension_state
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        if self.trade_state:
            if hasattr(self.trade_state, 'to_alipay_dict'):
                params['trade_state'] = self.trade_state.to_alipay_dict()
            else:
                params['trade_state'] = self.trade_state
        if self.up_price:
            if hasattr(self.up_price, 'to_alipay_dict'):
                params['up_price'] = self.up_price.to_alipay_dict()
            else:
                params['up_price'] = self.up_price
        if self.volume:
            if hasattr(self.volume, 'to_alipay_dict'):
                params['volume'] = self.volume.to_alipay_dict()
            else:
                params['volume'] = self.volume
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SnapshotDTO()
        if 'after_market_amount' in d:
            o.after_market_amount = d['after_market_amount']
        if 'after_market_buy_volume' in d:
            o.after_market_buy_volume = d['after_market_buy_volume']
        if 'after_market_price' in d:
            o.after_market_price = d['after_market_price']
        if 'after_market_sell_volume' in d:
            o.after_market_sell_volume = d['after_market_sell_volume']
        if 'after_market_trade_time' in d:
            o.after_market_trade_time = d['after_market_trade_time']
        if 'after_market_trading_phase' in d:
            o.after_market_trading_phase = d['after_market_trading_phase']
        if 'after_market_volume' in d:
            o.after_market_volume = d['after_market_volume']
        if 'amount' in d:
            o.amount = d['amount']
        if 'ask_price_1' in d:
            o.ask_price_1 = d['ask_price_1']
        if 'ask_price_10' in d:
            o.ask_price_10 = d['ask_price_10']
        if 'ask_price_2' in d:
            o.ask_price_2 = d['ask_price_2']
        if 'ask_price_3' in d:
            o.ask_price_3 = d['ask_price_3']
        if 'ask_price_4' in d:
            o.ask_price_4 = d['ask_price_4']
        if 'ask_price_5' in d:
            o.ask_price_5 = d['ask_price_5']
        if 'ask_price_6' in d:
            o.ask_price_6 = d['ask_price_6']
        if 'ask_price_7' in d:
            o.ask_price_7 = d['ask_price_7']
        if 'ask_price_8' in d:
            o.ask_price_8 = d['ask_price_8']
        if 'ask_price_9' in d:
            o.ask_price_9 = d['ask_price_9']
        if 'ask_volume_1' in d:
            o.ask_volume_1 = d['ask_volume_1']
        if 'ask_volume_10' in d:
            o.ask_volume_10 = d['ask_volume_10']
        if 'ask_volume_2' in d:
            o.ask_volume_2 = d['ask_volume_2']
        if 'ask_volume_3' in d:
            o.ask_volume_3 = d['ask_volume_3']
        if 'ask_volume_4' in d:
            o.ask_volume_4 = d['ask_volume_4']
        if 'ask_volume_5' in d:
            o.ask_volume_5 = d['ask_volume_5']
        if 'ask_volume_6' in d:
            o.ask_volume_6 = d['ask_volume_6']
        if 'ask_volume_7' in d:
            o.ask_volume_7 = d['ask_volume_7']
        if 'ask_volume_8' in d:
            o.ask_volume_8 = d['ask_volume_8']
        if 'ask_volume_9' in d:
            o.ask_volume_9 = d['ask_volume_9']
        if 'bid_price_1' in d:
            o.bid_price_1 = d['bid_price_1']
        if 'bid_price_10' in d:
            o.bid_price_10 = d['bid_price_10']
        if 'bid_price_2' in d:
            o.bid_price_2 = d['bid_price_2']
        if 'bid_price_3' in d:
            o.bid_price_3 = d['bid_price_3']
        if 'bid_price_4' in d:
            o.bid_price_4 = d['bid_price_4']
        if 'bid_price_5' in d:
            o.bid_price_5 = d['bid_price_5']
        if 'bid_price_6' in d:
            o.bid_price_6 = d['bid_price_6']
        if 'bid_price_7' in d:
            o.bid_price_7 = d['bid_price_7']
        if 'bid_price_8' in d:
            o.bid_price_8 = d['bid_price_8']
        if 'bid_price_9' in d:
            o.bid_price_9 = d['bid_price_9']
        if 'bid_volume_1' in d:
            o.bid_volume_1 = d['bid_volume_1']
        if 'bid_volume_10' in d:
            o.bid_volume_10 = d['bid_volume_10']
        if 'bid_volume_2' in d:
            o.bid_volume_2 = d['bid_volume_2']
        if 'bid_volume_3' in d:
            o.bid_volume_3 = d['bid_volume_3']
        if 'bid_volume_4' in d:
            o.bid_volume_4 = d['bid_volume_4']
        if 'bid_volume_5' in d:
            o.bid_volume_5 = d['bid_volume_5']
        if 'bid_volume_6' in d:
            o.bid_volume_6 = d['bid_volume_6']
        if 'bid_volume_7' in d:
            o.bid_volume_7 = d['bid_volume_7']
        if 'bid_volume_8' in d:
            o.bid_volume_8 = d['bid_volume_8']
        if 'bid_volume_9' in d:
            o.bid_volume_9 = d['bid_volume_9']
        if 'change_percent' in d:
            o.change_percent = d['change_percent']
        if 'change_price' in d:
            o.change_price = d['change_price']
        if 'close_price' in d:
            o.close_price = d['close_price']
        if 'date' in d:
            o.date = d['date']
        if 'down_price' in d:
            o.down_price = d['down_price']
        if 'high_price' in d:
            o.high_price = d['high_price']
        if 'low_price' in d:
            o.low_price = d['low_price']
        if 'name' in d:
            o.name = d['name']
        if 'open_price' in d:
            o.open_price = d['open_price']
        if 'previous_close' in d:
            o.previous_close = d['previous_close']
        if 'price' in d:
            o.price = d['price']
        if 'suspension_state' in d:
            o.suspension_state = d['suspension_state']
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'trade_state' in d:
            o.trade_state = d['trade_state']
        if 'up_price' in d:
            o.up_price = d['up_price']
        if 'volume' in d:
            o.volume = d['volume']
        return o


