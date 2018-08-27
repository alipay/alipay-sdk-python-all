#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PricingVO(object):

    def __init__(self):
        self._bid = None
        self._currency = None
        self._currency_unit = None
        self._expiry_timestamp = None
        self._generate_timestamp = None
        self._maturity_date = None
        self._maximum_bid_amount = None
        self._maximum_offer_amount = None
        self._memo = None
        self._mid = None
        self._minimum_bid_amount = None
        self._minimum_offer_amount = None
        self._offer = None
        self._period = None
        self._rate_reference_id = None
        self._rate_type = None
        self._spot_bid = None
        self._spot_mid = None
        self._spot_offer = None
        self._start_timestamp = None
        self._symbol = None
        self._threshold_timestamp = None
        self._valid_timestamp = None

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def currency_unit(self):
        return self._currency_unit

    @currency_unit.setter
    def currency_unit(self, value):
        self._currency_unit = value
    @property
    def expiry_timestamp(self):
        return self._expiry_timestamp

    @expiry_timestamp.setter
    def expiry_timestamp(self, value):
        self._expiry_timestamp = value
    @property
    def generate_timestamp(self):
        return self._generate_timestamp

    @generate_timestamp.setter
    def generate_timestamp(self, value):
        self._generate_timestamp = value
    @property
    def maturity_date(self):
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, value):
        self._maturity_date = value
    @property
    def maximum_bid_amount(self):
        return self._maximum_bid_amount

    @maximum_bid_amount.setter
    def maximum_bid_amount(self, value):
        self._maximum_bid_amount = value
    @property
    def maximum_offer_amount(self):
        return self._maximum_offer_amount

    @maximum_offer_amount.setter
    def maximum_offer_amount(self, value):
        self._maximum_offer_amount = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def minimum_bid_amount(self):
        return self._minimum_bid_amount

    @minimum_bid_amount.setter
    def minimum_bid_amount(self, value):
        self._minimum_bid_amount = value
    @property
    def minimum_offer_amount(self):
        return self._minimum_offer_amount

    @minimum_offer_amount.setter
    def minimum_offer_amount(self, value):
        self._minimum_offer_amount = value
    @property
    def offer(self):
        return self._offer

    @offer.setter
    def offer(self, value):
        self._offer = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def rate_reference_id(self):
        return self._rate_reference_id

    @rate_reference_id.setter
    def rate_reference_id(self, value):
        self._rate_reference_id = value
    @property
    def rate_type(self):
        return self._rate_type

    @rate_type.setter
    def rate_type(self, value):
        self._rate_type = value
    @property
    def spot_bid(self):
        return self._spot_bid

    @spot_bid.setter
    def spot_bid(self, value):
        self._spot_bid = value
    @property
    def spot_mid(self):
        return self._spot_mid

    @spot_mid.setter
    def spot_mid(self, value):
        self._spot_mid = value
    @property
    def spot_offer(self):
        return self._spot_offer

    @spot_offer.setter
    def spot_offer(self, value):
        self._spot_offer = value
    @property
    def start_timestamp(self):
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, value):
        self._start_timestamp = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
    @property
    def threshold_timestamp(self):
        return self._threshold_timestamp

    @threshold_timestamp.setter
    def threshold_timestamp(self, value):
        self._threshold_timestamp = value
    @property
    def valid_timestamp(self):
        return self._valid_timestamp

    @valid_timestamp.setter
    def valid_timestamp(self, value):
        self._valid_timestamp = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.currency_unit:
            if hasattr(self.currency_unit, 'to_alipay_dict'):
                params['currency_unit'] = self.currency_unit.to_alipay_dict()
            else:
                params['currency_unit'] = self.currency_unit
        if self.expiry_timestamp:
            if hasattr(self.expiry_timestamp, 'to_alipay_dict'):
                params['expiry_timestamp'] = self.expiry_timestamp.to_alipay_dict()
            else:
                params['expiry_timestamp'] = self.expiry_timestamp
        if self.generate_timestamp:
            if hasattr(self.generate_timestamp, 'to_alipay_dict'):
                params['generate_timestamp'] = self.generate_timestamp.to_alipay_dict()
            else:
                params['generate_timestamp'] = self.generate_timestamp
        if self.maturity_date:
            if hasattr(self.maturity_date, 'to_alipay_dict'):
                params['maturity_date'] = self.maturity_date.to_alipay_dict()
            else:
                params['maturity_date'] = self.maturity_date
        if self.maximum_bid_amount:
            if hasattr(self.maximum_bid_amount, 'to_alipay_dict'):
                params['maximum_bid_amount'] = self.maximum_bid_amount.to_alipay_dict()
            else:
                params['maximum_bid_amount'] = self.maximum_bid_amount
        if self.maximum_offer_amount:
            if hasattr(self.maximum_offer_amount, 'to_alipay_dict'):
                params['maximum_offer_amount'] = self.maximum_offer_amount.to_alipay_dict()
            else:
                params['maximum_offer_amount'] = self.maximum_offer_amount
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.minimum_bid_amount:
            if hasattr(self.minimum_bid_amount, 'to_alipay_dict'):
                params['minimum_bid_amount'] = self.minimum_bid_amount.to_alipay_dict()
            else:
                params['minimum_bid_amount'] = self.minimum_bid_amount
        if self.minimum_offer_amount:
            if hasattr(self.minimum_offer_amount, 'to_alipay_dict'):
                params['minimum_offer_amount'] = self.minimum_offer_amount.to_alipay_dict()
            else:
                params['minimum_offer_amount'] = self.minimum_offer_amount
        if self.offer:
            if hasattr(self.offer, 'to_alipay_dict'):
                params['offer'] = self.offer.to_alipay_dict()
            else:
                params['offer'] = self.offer
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.rate_reference_id:
            if hasattr(self.rate_reference_id, 'to_alipay_dict'):
                params['rate_reference_id'] = self.rate_reference_id.to_alipay_dict()
            else:
                params['rate_reference_id'] = self.rate_reference_id
        if self.rate_type:
            if hasattr(self.rate_type, 'to_alipay_dict'):
                params['rate_type'] = self.rate_type.to_alipay_dict()
            else:
                params['rate_type'] = self.rate_type
        if self.spot_bid:
            if hasattr(self.spot_bid, 'to_alipay_dict'):
                params['spot_bid'] = self.spot_bid.to_alipay_dict()
            else:
                params['spot_bid'] = self.spot_bid
        if self.spot_mid:
            if hasattr(self.spot_mid, 'to_alipay_dict'):
                params['spot_mid'] = self.spot_mid.to_alipay_dict()
            else:
                params['spot_mid'] = self.spot_mid
        if self.spot_offer:
            if hasattr(self.spot_offer, 'to_alipay_dict'):
                params['spot_offer'] = self.spot_offer.to_alipay_dict()
            else:
                params['spot_offer'] = self.spot_offer
        if self.start_timestamp:
            if hasattr(self.start_timestamp, 'to_alipay_dict'):
                params['start_timestamp'] = self.start_timestamp.to_alipay_dict()
            else:
                params['start_timestamp'] = self.start_timestamp
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        if self.threshold_timestamp:
            if hasattr(self.threshold_timestamp, 'to_alipay_dict'):
                params['threshold_timestamp'] = self.threshold_timestamp.to_alipay_dict()
            else:
                params['threshold_timestamp'] = self.threshold_timestamp
        if self.valid_timestamp:
            if hasattr(self.valid_timestamp, 'to_alipay_dict'):
                params['valid_timestamp'] = self.valid_timestamp.to_alipay_dict()
            else:
                params['valid_timestamp'] = self.valid_timestamp
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PricingVO()
        if 'bid' in d:
            o.bid = d['bid']
        if 'currency' in d:
            o.currency = d['currency']
        if 'currency_unit' in d:
            o.currency_unit = d['currency_unit']
        if 'expiry_timestamp' in d:
            o.expiry_timestamp = d['expiry_timestamp']
        if 'generate_timestamp' in d:
            o.generate_timestamp = d['generate_timestamp']
        if 'maturity_date' in d:
            o.maturity_date = d['maturity_date']
        if 'maximum_bid_amount' in d:
            o.maximum_bid_amount = d['maximum_bid_amount']
        if 'maximum_offer_amount' in d:
            o.maximum_offer_amount = d['maximum_offer_amount']
        if 'memo' in d:
            o.memo = d['memo']
        if 'mid' in d:
            o.mid = d['mid']
        if 'minimum_bid_amount' in d:
            o.minimum_bid_amount = d['minimum_bid_amount']
        if 'minimum_offer_amount' in d:
            o.minimum_offer_amount = d['minimum_offer_amount']
        if 'offer' in d:
            o.offer = d['offer']
        if 'period' in d:
            o.period = d['period']
        if 'rate_reference_id' in d:
            o.rate_reference_id = d['rate_reference_id']
        if 'rate_type' in d:
            o.rate_type = d['rate_type']
        if 'spot_bid' in d:
            o.spot_bid = d['spot_bid']
        if 'spot_mid' in d:
            o.spot_mid = d['spot_mid']
        if 'spot_offer' in d:
            o.spot_offer = d['spot_offer']
        if 'start_timestamp' in d:
            o.start_timestamp = d['start_timestamp']
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'threshold_timestamp' in d:
            o.threshold_timestamp = d['threshold_timestamp']
        if 'valid_timestamp' in d:
            o.valid_timestamp = d['valid_timestamp']
        return o


