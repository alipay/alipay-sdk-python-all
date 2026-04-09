#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LtOrderDTO import LtOrderDTO
from alipay.aop.api.domain.LtOrderDTO import LtOrderDTO
from alipay.aop.api.domain.LtBidAskLevelDTO import LtBidAskLevelDTO
from alipay.aop.api.domain.LtBidAskLevelDTO import LtBidAskLevelDTO


class LtSnapshotDTO(object):

    def __init__(self):
        self._after_market_amount = None
        self._after_market_buy_orders = None
        self._after_market_buy_volume = None
        self._after_market_price = None
        self._after_market_sell_orders = None
        self._after_market_sell_volume = None
        self._after_market_trade_time = None
        self._after_market_trading_phase = None
        self._after_market_transactions = None
        self._after_market_volume = None
        self._amount = None
        self._asks = None
        self._belong_day = None
        self._bids = None
        self._big_order_volume = None
        self._change_percent = None
        self._change_price = None
        self._change_price_status = None
        self._channel_exchange = None
        self._channel_level = None
        self._close_price = None
        self._date = None
        self._down_price = None
        self._high_price = None
        self._iopv = None
        self._iopv_tm_1 = None
        self._limit_state = None
        self._low_price = None
        self._market_state = None
        self._market_state_desc = None
        self._max_buy_limit_price = None
        self._max_sell_limit_price = None
        self._min_buy_limit_price = None
        self._min_sell_limit_price = None
        self._name = None
        self._open_price = None
        self._premium_rate = None
        self._previous_close = None
        self._price = None
        self._range_percent = None
        self._situation = None
        self._snapshot_date = None
        self._suspension_state = None
        self._symbol = None
        self._tick_size = None
        self._time_zone = None
        self._total_ask_volume = None
        self._total_bid_volume = None
        self._trade_state = None
        self._up_price = None
        self._volume = None
        self._weighted_ask_price = None
        self._weighted_bid_price = None

    @property
    def after_market_amount(self):
        return self._after_market_amount

    @after_market_amount.setter
    def after_market_amount(self, value):
        self._after_market_amount = value
    @property
    def after_market_buy_orders(self):
        return self._after_market_buy_orders

    @after_market_buy_orders.setter
    def after_market_buy_orders(self, value):
        if isinstance(value, list):
            self._after_market_buy_orders = list()
            for i in value:
                if isinstance(i, LtOrderDTO):
                    self._after_market_buy_orders.append(i)
                else:
                    self._after_market_buy_orders.append(LtOrderDTO.from_alipay_dict(i))
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
    def after_market_sell_orders(self):
        return self._after_market_sell_orders

    @after_market_sell_orders.setter
    def after_market_sell_orders(self, value):
        if isinstance(value, list):
            self._after_market_sell_orders = list()
            for i in value:
                if isinstance(i, LtOrderDTO):
                    self._after_market_sell_orders.append(i)
                else:
                    self._after_market_sell_orders.append(LtOrderDTO.from_alipay_dict(i))
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
    def after_market_transactions(self):
        return self._after_market_transactions

    @after_market_transactions.setter
    def after_market_transactions(self, value):
        self._after_market_transactions = value
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
    def asks(self):
        return self._asks

    @asks.setter
    def asks(self, value):
        if isinstance(value, list):
            self._asks = list()
            for i in value:
                if isinstance(i, LtBidAskLevelDTO):
                    self._asks.append(i)
                else:
                    self._asks.append(LtBidAskLevelDTO.from_alipay_dict(i))
    @property
    def belong_day(self):
        return self._belong_day

    @belong_day.setter
    def belong_day(self, value):
        self._belong_day = value
    @property
    def bids(self):
        return self._bids

    @bids.setter
    def bids(self, value):
        if isinstance(value, list):
            self._bids = list()
            for i in value:
                if isinstance(i, LtBidAskLevelDTO):
                    self._bids.append(i)
                else:
                    self._bids.append(LtBidAskLevelDTO.from_alipay_dict(i))
    @property
    def big_order_volume(self):
        return self._big_order_volume

    @big_order_volume.setter
    def big_order_volume(self, value):
        self._big_order_volume = value
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
    def change_price_status(self):
        return self._change_price_status

    @change_price_status.setter
    def change_price_status(self, value):
        self._change_price_status = value
    @property
    def channel_exchange(self):
        return self._channel_exchange

    @channel_exchange.setter
    def channel_exchange(self, value):
        self._channel_exchange = value
    @property
    def channel_level(self):
        return self._channel_level

    @channel_level.setter
    def channel_level(self, value):
        self._channel_level = value
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
    def iopv(self):
        return self._iopv

    @iopv.setter
    def iopv(self, value):
        self._iopv = value
    @property
    def iopv_tm_1(self):
        return self._iopv_tm_1

    @iopv_tm_1.setter
    def iopv_tm_1(self, value):
        self._iopv_tm_1 = value
    @property
    def limit_state(self):
        return self._limit_state

    @limit_state.setter
    def limit_state(self, value):
        self._limit_state = value
    @property
    def low_price(self):
        return self._low_price

    @low_price.setter
    def low_price(self, value):
        self._low_price = value
    @property
    def market_state(self):
        return self._market_state

    @market_state.setter
    def market_state(self, value):
        self._market_state = value
    @property
    def market_state_desc(self):
        return self._market_state_desc

    @market_state_desc.setter
    def market_state_desc(self, value):
        self._market_state_desc = value
    @property
    def max_buy_limit_price(self):
        return self._max_buy_limit_price

    @max_buy_limit_price.setter
    def max_buy_limit_price(self, value):
        self._max_buy_limit_price = value
    @property
    def max_sell_limit_price(self):
        return self._max_sell_limit_price

    @max_sell_limit_price.setter
    def max_sell_limit_price(self, value):
        self._max_sell_limit_price = value
    @property
    def min_buy_limit_price(self):
        return self._min_buy_limit_price

    @min_buy_limit_price.setter
    def min_buy_limit_price(self, value):
        self._min_buy_limit_price = value
    @property
    def min_sell_limit_price(self):
        return self._min_sell_limit_price

    @min_sell_limit_price.setter
    def min_sell_limit_price(self, value):
        self._min_sell_limit_price = value
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
    def premium_rate(self):
        return self._premium_rate

    @premium_rate.setter
    def premium_rate(self, value):
        self._premium_rate = value
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
    def range_percent(self):
        return self._range_percent

    @range_percent.setter
    def range_percent(self, value):
        self._range_percent = value
    @property
    def situation(self):
        return self._situation

    @situation.setter
    def situation(self, value):
        self._situation = value
    @property
    def snapshot_date(self):
        return self._snapshot_date

    @snapshot_date.setter
    def snapshot_date(self, value):
        self._snapshot_date = value
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
    def tick_size(self):
        return self._tick_size

    @tick_size.setter
    def tick_size(self, value):
        self._tick_size = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value
    @property
    def total_ask_volume(self):
        return self._total_ask_volume

    @total_ask_volume.setter
    def total_ask_volume(self, value):
        self._total_ask_volume = value
    @property
    def total_bid_volume(self):
        return self._total_bid_volume

    @total_bid_volume.setter
    def total_bid_volume(self, value):
        self._total_bid_volume = value
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
    @property
    def weighted_ask_price(self):
        return self._weighted_ask_price

    @weighted_ask_price.setter
    def weighted_ask_price(self, value):
        self._weighted_ask_price = value
    @property
    def weighted_bid_price(self):
        return self._weighted_bid_price

    @weighted_bid_price.setter
    def weighted_bid_price(self, value):
        self._weighted_bid_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.after_market_amount:
            if hasattr(self.after_market_amount, 'to_alipay_dict'):
                params['after_market_amount'] = self.after_market_amount.to_alipay_dict()
            else:
                params['after_market_amount'] = self.after_market_amount
        if self.after_market_buy_orders:
            if isinstance(self.after_market_buy_orders, list):
                for i in range(0, len(self.after_market_buy_orders)):
                    element = self.after_market_buy_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.after_market_buy_orders[i] = element.to_alipay_dict()
            if hasattr(self.after_market_buy_orders, 'to_alipay_dict'):
                params['after_market_buy_orders'] = self.after_market_buy_orders.to_alipay_dict()
            else:
                params['after_market_buy_orders'] = self.after_market_buy_orders
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
        if self.after_market_sell_orders:
            if isinstance(self.after_market_sell_orders, list):
                for i in range(0, len(self.after_market_sell_orders)):
                    element = self.after_market_sell_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.after_market_sell_orders[i] = element.to_alipay_dict()
            if hasattr(self.after_market_sell_orders, 'to_alipay_dict'):
                params['after_market_sell_orders'] = self.after_market_sell_orders.to_alipay_dict()
            else:
                params['after_market_sell_orders'] = self.after_market_sell_orders
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
        if self.after_market_transactions:
            if hasattr(self.after_market_transactions, 'to_alipay_dict'):
                params['after_market_transactions'] = self.after_market_transactions.to_alipay_dict()
            else:
                params['after_market_transactions'] = self.after_market_transactions
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
        if self.asks:
            if isinstance(self.asks, list):
                for i in range(0, len(self.asks)):
                    element = self.asks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.asks[i] = element.to_alipay_dict()
            if hasattr(self.asks, 'to_alipay_dict'):
                params['asks'] = self.asks.to_alipay_dict()
            else:
                params['asks'] = self.asks
        if self.belong_day:
            if hasattr(self.belong_day, 'to_alipay_dict'):
                params['belong_day'] = self.belong_day.to_alipay_dict()
            else:
                params['belong_day'] = self.belong_day
        if self.bids:
            if isinstance(self.bids, list):
                for i in range(0, len(self.bids)):
                    element = self.bids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bids[i] = element.to_alipay_dict()
            if hasattr(self.bids, 'to_alipay_dict'):
                params['bids'] = self.bids.to_alipay_dict()
            else:
                params['bids'] = self.bids
        if self.big_order_volume:
            if hasattr(self.big_order_volume, 'to_alipay_dict'):
                params['big_order_volume'] = self.big_order_volume.to_alipay_dict()
            else:
                params['big_order_volume'] = self.big_order_volume
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
        if self.change_price_status:
            if hasattr(self.change_price_status, 'to_alipay_dict'):
                params['change_price_status'] = self.change_price_status.to_alipay_dict()
            else:
                params['change_price_status'] = self.change_price_status
        if self.channel_exchange:
            if hasattr(self.channel_exchange, 'to_alipay_dict'):
                params['channel_exchange'] = self.channel_exchange.to_alipay_dict()
            else:
                params['channel_exchange'] = self.channel_exchange
        if self.channel_level:
            if hasattr(self.channel_level, 'to_alipay_dict'):
                params['channel_level'] = self.channel_level.to_alipay_dict()
            else:
                params['channel_level'] = self.channel_level
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
        if self.iopv:
            if hasattr(self.iopv, 'to_alipay_dict'):
                params['iopv'] = self.iopv.to_alipay_dict()
            else:
                params['iopv'] = self.iopv
        if self.iopv_tm_1:
            if hasattr(self.iopv_tm_1, 'to_alipay_dict'):
                params['iopv_tm_1'] = self.iopv_tm_1.to_alipay_dict()
            else:
                params['iopv_tm_1'] = self.iopv_tm_1
        if self.limit_state:
            if hasattr(self.limit_state, 'to_alipay_dict'):
                params['limit_state'] = self.limit_state.to_alipay_dict()
            else:
                params['limit_state'] = self.limit_state
        if self.low_price:
            if hasattr(self.low_price, 'to_alipay_dict'):
                params['low_price'] = self.low_price.to_alipay_dict()
            else:
                params['low_price'] = self.low_price
        if self.market_state:
            if hasattr(self.market_state, 'to_alipay_dict'):
                params['market_state'] = self.market_state.to_alipay_dict()
            else:
                params['market_state'] = self.market_state
        if self.market_state_desc:
            if hasattr(self.market_state_desc, 'to_alipay_dict'):
                params['market_state_desc'] = self.market_state_desc.to_alipay_dict()
            else:
                params['market_state_desc'] = self.market_state_desc
        if self.max_buy_limit_price:
            if hasattr(self.max_buy_limit_price, 'to_alipay_dict'):
                params['max_buy_limit_price'] = self.max_buy_limit_price.to_alipay_dict()
            else:
                params['max_buy_limit_price'] = self.max_buy_limit_price
        if self.max_sell_limit_price:
            if hasattr(self.max_sell_limit_price, 'to_alipay_dict'):
                params['max_sell_limit_price'] = self.max_sell_limit_price.to_alipay_dict()
            else:
                params['max_sell_limit_price'] = self.max_sell_limit_price
        if self.min_buy_limit_price:
            if hasattr(self.min_buy_limit_price, 'to_alipay_dict'):
                params['min_buy_limit_price'] = self.min_buy_limit_price.to_alipay_dict()
            else:
                params['min_buy_limit_price'] = self.min_buy_limit_price
        if self.min_sell_limit_price:
            if hasattr(self.min_sell_limit_price, 'to_alipay_dict'):
                params['min_sell_limit_price'] = self.min_sell_limit_price.to_alipay_dict()
            else:
                params['min_sell_limit_price'] = self.min_sell_limit_price
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
        if self.premium_rate:
            if hasattr(self.premium_rate, 'to_alipay_dict'):
                params['premium_rate'] = self.premium_rate.to_alipay_dict()
            else:
                params['premium_rate'] = self.premium_rate
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
        if self.range_percent:
            if hasattr(self.range_percent, 'to_alipay_dict'):
                params['range_percent'] = self.range_percent.to_alipay_dict()
            else:
                params['range_percent'] = self.range_percent
        if self.situation:
            if hasattr(self.situation, 'to_alipay_dict'):
                params['situation'] = self.situation.to_alipay_dict()
            else:
                params['situation'] = self.situation
        if self.snapshot_date:
            if hasattr(self.snapshot_date, 'to_alipay_dict'):
                params['snapshot_date'] = self.snapshot_date.to_alipay_dict()
            else:
                params['snapshot_date'] = self.snapshot_date
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
        if self.tick_size:
            if hasattr(self.tick_size, 'to_alipay_dict'):
                params['tick_size'] = self.tick_size.to_alipay_dict()
            else:
                params['tick_size'] = self.tick_size
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        if self.total_ask_volume:
            if hasattr(self.total_ask_volume, 'to_alipay_dict'):
                params['total_ask_volume'] = self.total_ask_volume.to_alipay_dict()
            else:
                params['total_ask_volume'] = self.total_ask_volume
        if self.total_bid_volume:
            if hasattr(self.total_bid_volume, 'to_alipay_dict'):
                params['total_bid_volume'] = self.total_bid_volume.to_alipay_dict()
            else:
                params['total_bid_volume'] = self.total_bid_volume
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
        if self.weighted_ask_price:
            if hasattr(self.weighted_ask_price, 'to_alipay_dict'):
                params['weighted_ask_price'] = self.weighted_ask_price.to_alipay_dict()
            else:
                params['weighted_ask_price'] = self.weighted_ask_price
        if self.weighted_bid_price:
            if hasattr(self.weighted_bid_price, 'to_alipay_dict'):
                params['weighted_bid_price'] = self.weighted_bid_price.to_alipay_dict()
            else:
                params['weighted_bid_price'] = self.weighted_bid_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LtSnapshotDTO()
        if 'after_market_amount' in d:
            o.after_market_amount = d['after_market_amount']
        if 'after_market_buy_orders' in d:
            o.after_market_buy_orders = d['after_market_buy_orders']
        if 'after_market_buy_volume' in d:
            o.after_market_buy_volume = d['after_market_buy_volume']
        if 'after_market_price' in d:
            o.after_market_price = d['after_market_price']
        if 'after_market_sell_orders' in d:
            o.after_market_sell_orders = d['after_market_sell_orders']
        if 'after_market_sell_volume' in d:
            o.after_market_sell_volume = d['after_market_sell_volume']
        if 'after_market_trade_time' in d:
            o.after_market_trade_time = d['after_market_trade_time']
        if 'after_market_trading_phase' in d:
            o.after_market_trading_phase = d['after_market_trading_phase']
        if 'after_market_transactions' in d:
            o.after_market_transactions = d['after_market_transactions']
        if 'after_market_volume' in d:
            o.after_market_volume = d['after_market_volume']
        if 'amount' in d:
            o.amount = d['amount']
        if 'asks' in d:
            o.asks = d['asks']
        if 'belong_day' in d:
            o.belong_day = d['belong_day']
        if 'bids' in d:
            o.bids = d['bids']
        if 'big_order_volume' in d:
            o.big_order_volume = d['big_order_volume']
        if 'change_percent' in d:
            o.change_percent = d['change_percent']
        if 'change_price' in d:
            o.change_price = d['change_price']
        if 'change_price_status' in d:
            o.change_price_status = d['change_price_status']
        if 'channel_exchange' in d:
            o.channel_exchange = d['channel_exchange']
        if 'channel_level' in d:
            o.channel_level = d['channel_level']
        if 'close_price' in d:
            o.close_price = d['close_price']
        if 'date' in d:
            o.date = d['date']
        if 'down_price' in d:
            o.down_price = d['down_price']
        if 'high_price' in d:
            o.high_price = d['high_price']
        if 'iopv' in d:
            o.iopv = d['iopv']
        if 'iopv_tm_1' in d:
            o.iopv_tm_1 = d['iopv_tm_1']
        if 'limit_state' in d:
            o.limit_state = d['limit_state']
        if 'low_price' in d:
            o.low_price = d['low_price']
        if 'market_state' in d:
            o.market_state = d['market_state']
        if 'market_state_desc' in d:
            o.market_state_desc = d['market_state_desc']
        if 'max_buy_limit_price' in d:
            o.max_buy_limit_price = d['max_buy_limit_price']
        if 'max_sell_limit_price' in d:
            o.max_sell_limit_price = d['max_sell_limit_price']
        if 'min_buy_limit_price' in d:
            o.min_buy_limit_price = d['min_buy_limit_price']
        if 'min_sell_limit_price' in d:
            o.min_sell_limit_price = d['min_sell_limit_price']
        if 'name' in d:
            o.name = d['name']
        if 'open_price' in d:
            o.open_price = d['open_price']
        if 'premium_rate' in d:
            o.premium_rate = d['premium_rate']
        if 'previous_close' in d:
            o.previous_close = d['previous_close']
        if 'price' in d:
            o.price = d['price']
        if 'range_percent' in d:
            o.range_percent = d['range_percent']
        if 'situation' in d:
            o.situation = d['situation']
        if 'snapshot_date' in d:
            o.snapshot_date = d['snapshot_date']
        if 'suspension_state' in d:
            o.suspension_state = d['suspension_state']
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'tick_size' in d:
            o.tick_size = d['tick_size']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        if 'total_ask_volume' in d:
            o.total_ask_volume = d['total_ask_volume']
        if 'total_bid_volume' in d:
            o.total_bid_volume = d['total_bid_volume']
        if 'trade_state' in d:
            o.trade_state = d['trade_state']
        if 'up_price' in d:
            o.up_price = d['up_price']
        if 'volume' in d:
            o.volume = d['volume']
        if 'weighted_ask_price' in d:
            o.weighted_ask_price = d['weighted_ask_price']
        if 'weighted_bid_price' in d:
            o.weighted_bid_price = d['weighted_bid_price']
        return o


