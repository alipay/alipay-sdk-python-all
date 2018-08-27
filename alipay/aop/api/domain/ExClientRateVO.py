#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExClientRateVO(object):

    def __init__(self):
        self._agreement_id = None
        self._base_ccy = None
        self._bid_rate = None
        self._client_bid_rate = None
        self._client_id = None
        self._client_offer_rate = None
        self._currency_pair = None
        self._expiry_time = None
        self._generate_date = None
        self._generate_time = None
        self._guaranteed = None
        self._maturity_date = None
        self._maximum_bid_amount = None
        self._maximum_offer_amount = None
        self._mid_rate = None
        self._minimum_bid_amount = None
        self._minimum_offer_amount = None
        self._offer_rate = None
        self._on_off_shore = None
        self._origin_rate_inst = None
        self._origin_rate_ref = None
        self._period = None
        self._profile_id = None
        self._quote_ccy = None
        self._rate_ref = None
        self._rate_time = None
        self._rate_type = None
        self._sp_bid = None
        self._sp_mid = None
        self._sp_offer = None
        self._standard_product_rate_id = None
        self._start_time = None
        self._sub_agreement_id = None
        self._threshold_time = None
        self._time_zone = None
        self._transaction_ccy_type = None
        self._valid_time = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def base_ccy(self):
        return self._base_ccy

    @base_ccy.setter
    def base_ccy(self, value):
        self._base_ccy = value
    @property
    def bid_rate(self):
        return self._bid_rate

    @bid_rate.setter
    def bid_rate(self, value):
        self._bid_rate = value
    @property
    def client_bid_rate(self):
        return self._client_bid_rate

    @client_bid_rate.setter
    def client_bid_rate(self, value):
        self._client_bid_rate = value
    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value
    @property
    def client_offer_rate(self):
        return self._client_offer_rate

    @client_offer_rate.setter
    def client_offer_rate(self, value):
        self._client_offer_rate = value
    @property
    def currency_pair(self):
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, value):
        self._currency_pair = value
    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def generate_date(self):
        return self._generate_date

    @generate_date.setter
    def generate_date(self, value):
        self._generate_date = value
    @property
    def generate_time(self):
        return self._generate_time

    @generate_time.setter
    def generate_time(self, value):
        self._generate_time = value
    @property
    def guaranteed(self):
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, value):
        self._guaranteed = value
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
    def mid_rate(self):
        return self._mid_rate

    @mid_rate.setter
    def mid_rate(self, value):
        self._mid_rate = value
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
    def offer_rate(self):
        return self._offer_rate

    @offer_rate.setter
    def offer_rate(self, value):
        self._offer_rate = value
    @property
    def on_off_shore(self):
        return self._on_off_shore

    @on_off_shore.setter
    def on_off_shore(self, value):
        self._on_off_shore = value
    @property
    def origin_rate_inst(self):
        return self._origin_rate_inst

    @origin_rate_inst.setter
    def origin_rate_inst(self, value):
        self._origin_rate_inst = value
    @property
    def origin_rate_ref(self):
        return self._origin_rate_ref

    @origin_rate_ref.setter
    def origin_rate_ref(self, value):
        self._origin_rate_ref = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def profile_id(self):
        return self._profile_id

    @profile_id.setter
    def profile_id(self, value):
        self._profile_id = value
    @property
    def quote_ccy(self):
        return self._quote_ccy

    @quote_ccy.setter
    def quote_ccy(self, value):
        self._quote_ccy = value
    @property
    def rate_ref(self):
        return self._rate_ref

    @rate_ref.setter
    def rate_ref(self, value):
        self._rate_ref = value
    @property
    def rate_time(self):
        return self._rate_time

    @rate_time.setter
    def rate_time(self, value):
        self._rate_time = value
    @property
    def rate_type(self):
        return self._rate_type

    @rate_type.setter
    def rate_type(self, value):
        self._rate_type = value
    @property
    def sp_bid(self):
        return self._sp_bid

    @sp_bid.setter
    def sp_bid(self, value):
        self._sp_bid = value
    @property
    def sp_mid(self):
        return self._sp_mid

    @sp_mid.setter
    def sp_mid(self, value):
        self._sp_mid = value
    @property
    def sp_offer(self):
        return self._sp_offer

    @sp_offer.setter
    def sp_offer(self, value):
        self._sp_offer = value
    @property
    def standard_product_rate_id(self):
        return self._standard_product_rate_id

    @standard_product_rate_id.setter
    def standard_product_rate_id(self, value):
        self._standard_product_rate_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_agreement_id(self):
        return self._sub_agreement_id

    @sub_agreement_id.setter
    def sub_agreement_id(self, value):
        self._sub_agreement_id = value
    @property
    def threshold_time(self):
        return self._threshold_time

    @threshold_time.setter
    def threshold_time(self, value):
        self._threshold_time = value
    @property
    def time_zone(self):
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        self._time_zone = value
    @property
    def transaction_ccy_type(self):
        return self._transaction_ccy_type

    @transaction_ccy_type.setter
    def transaction_ccy_type(self, value):
        self._transaction_ccy_type = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_id:
            if hasattr(self.agreement_id, 'to_alipay_dict'):
                params['agreement_id'] = self.agreement_id.to_alipay_dict()
            else:
                params['agreement_id'] = self.agreement_id
        if self.base_ccy:
            if hasattr(self.base_ccy, 'to_alipay_dict'):
                params['base_ccy'] = self.base_ccy.to_alipay_dict()
            else:
                params['base_ccy'] = self.base_ccy
        if self.bid_rate:
            if hasattr(self.bid_rate, 'to_alipay_dict'):
                params['bid_rate'] = self.bid_rate.to_alipay_dict()
            else:
                params['bid_rate'] = self.bid_rate
        if self.client_bid_rate:
            if hasattr(self.client_bid_rate, 'to_alipay_dict'):
                params['client_bid_rate'] = self.client_bid_rate.to_alipay_dict()
            else:
                params['client_bid_rate'] = self.client_bid_rate
        if self.client_id:
            if hasattr(self.client_id, 'to_alipay_dict'):
                params['client_id'] = self.client_id.to_alipay_dict()
            else:
                params['client_id'] = self.client_id
        if self.client_offer_rate:
            if hasattr(self.client_offer_rate, 'to_alipay_dict'):
                params['client_offer_rate'] = self.client_offer_rate.to_alipay_dict()
            else:
                params['client_offer_rate'] = self.client_offer_rate
        if self.currency_pair:
            if hasattr(self.currency_pair, 'to_alipay_dict'):
                params['currency_pair'] = self.currency_pair.to_alipay_dict()
            else:
                params['currency_pair'] = self.currency_pair
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.generate_date:
            if hasattr(self.generate_date, 'to_alipay_dict'):
                params['generate_date'] = self.generate_date.to_alipay_dict()
            else:
                params['generate_date'] = self.generate_date
        if self.generate_time:
            if hasattr(self.generate_time, 'to_alipay_dict'):
                params['generate_time'] = self.generate_time.to_alipay_dict()
            else:
                params['generate_time'] = self.generate_time
        if self.guaranteed:
            if hasattr(self.guaranteed, 'to_alipay_dict'):
                params['guaranteed'] = self.guaranteed.to_alipay_dict()
            else:
                params['guaranteed'] = self.guaranteed
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
        if self.mid_rate:
            if hasattr(self.mid_rate, 'to_alipay_dict'):
                params['mid_rate'] = self.mid_rate.to_alipay_dict()
            else:
                params['mid_rate'] = self.mid_rate
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
        if self.offer_rate:
            if hasattr(self.offer_rate, 'to_alipay_dict'):
                params['offer_rate'] = self.offer_rate.to_alipay_dict()
            else:
                params['offer_rate'] = self.offer_rate
        if self.on_off_shore:
            if hasattr(self.on_off_shore, 'to_alipay_dict'):
                params['on_off_shore'] = self.on_off_shore.to_alipay_dict()
            else:
                params['on_off_shore'] = self.on_off_shore
        if self.origin_rate_inst:
            if hasattr(self.origin_rate_inst, 'to_alipay_dict'):
                params['origin_rate_inst'] = self.origin_rate_inst.to_alipay_dict()
            else:
                params['origin_rate_inst'] = self.origin_rate_inst
        if self.origin_rate_ref:
            if hasattr(self.origin_rate_ref, 'to_alipay_dict'):
                params['origin_rate_ref'] = self.origin_rate_ref.to_alipay_dict()
            else:
                params['origin_rate_ref'] = self.origin_rate_ref
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.profile_id:
            if hasattr(self.profile_id, 'to_alipay_dict'):
                params['profile_id'] = self.profile_id.to_alipay_dict()
            else:
                params['profile_id'] = self.profile_id
        if self.quote_ccy:
            if hasattr(self.quote_ccy, 'to_alipay_dict'):
                params['quote_ccy'] = self.quote_ccy.to_alipay_dict()
            else:
                params['quote_ccy'] = self.quote_ccy
        if self.rate_ref:
            if hasattr(self.rate_ref, 'to_alipay_dict'):
                params['rate_ref'] = self.rate_ref.to_alipay_dict()
            else:
                params['rate_ref'] = self.rate_ref
        if self.rate_time:
            if hasattr(self.rate_time, 'to_alipay_dict'):
                params['rate_time'] = self.rate_time.to_alipay_dict()
            else:
                params['rate_time'] = self.rate_time
        if self.rate_type:
            if hasattr(self.rate_type, 'to_alipay_dict'):
                params['rate_type'] = self.rate_type.to_alipay_dict()
            else:
                params['rate_type'] = self.rate_type
        if self.sp_bid:
            if hasattr(self.sp_bid, 'to_alipay_dict'):
                params['sp_bid'] = self.sp_bid.to_alipay_dict()
            else:
                params['sp_bid'] = self.sp_bid
        if self.sp_mid:
            if hasattr(self.sp_mid, 'to_alipay_dict'):
                params['sp_mid'] = self.sp_mid.to_alipay_dict()
            else:
                params['sp_mid'] = self.sp_mid
        if self.sp_offer:
            if hasattr(self.sp_offer, 'to_alipay_dict'):
                params['sp_offer'] = self.sp_offer.to_alipay_dict()
            else:
                params['sp_offer'] = self.sp_offer
        if self.standard_product_rate_id:
            if hasattr(self.standard_product_rate_id, 'to_alipay_dict'):
                params['standard_product_rate_id'] = self.standard_product_rate_id.to_alipay_dict()
            else:
                params['standard_product_rate_id'] = self.standard_product_rate_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_agreement_id:
            if hasattr(self.sub_agreement_id, 'to_alipay_dict'):
                params['sub_agreement_id'] = self.sub_agreement_id.to_alipay_dict()
            else:
                params['sub_agreement_id'] = self.sub_agreement_id
        if self.threshold_time:
            if hasattr(self.threshold_time, 'to_alipay_dict'):
                params['threshold_time'] = self.threshold_time.to_alipay_dict()
            else:
                params['threshold_time'] = self.threshold_time
        if self.time_zone:
            if hasattr(self.time_zone, 'to_alipay_dict'):
                params['time_zone'] = self.time_zone.to_alipay_dict()
            else:
                params['time_zone'] = self.time_zone
        if self.transaction_ccy_type:
            if hasattr(self.transaction_ccy_type, 'to_alipay_dict'):
                params['transaction_ccy_type'] = self.transaction_ccy_type.to_alipay_dict()
            else:
                params['transaction_ccy_type'] = self.transaction_ccy_type
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExClientRateVO()
        if 'agreement_id' in d:
            o.agreement_id = d['agreement_id']
        if 'base_ccy' in d:
            o.base_ccy = d['base_ccy']
        if 'bid_rate' in d:
            o.bid_rate = d['bid_rate']
        if 'client_bid_rate' in d:
            o.client_bid_rate = d['client_bid_rate']
        if 'client_id' in d:
            o.client_id = d['client_id']
        if 'client_offer_rate' in d:
            o.client_offer_rate = d['client_offer_rate']
        if 'currency_pair' in d:
            o.currency_pair = d['currency_pair']
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'generate_date' in d:
            o.generate_date = d['generate_date']
        if 'generate_time' in d:
            o.generate_time = d['generate_time']
        if 'guaranteed' in d:
            o.guaranteed = d['guaranteed']
        if 'maturity_date' in d:
            o.maturity_date = d['maturity_date']
        if 'maximum_bid_amount' in d:
            o.maximum_bid_amount = d['maximum_bid_amount']
        if 'maximum_offer_amount' in d:
            o.maximum_offer_amount = d['maximum_offer_amount']
        if 'mid_rate' in d:
            o.mid_rate = d['mid_rate']
        if 'minimum_bid_amount' in d:
            o.minimum_bid_amount = d['minimum_bid_amount']
        if 'minimum_offer_amount' in d:
            o.minimum_offer_amount = d['minimum_offer_amount']
        if 'offer_rate' in d:
            o.offer_rate = d['offer_rate']
        if 'on_off_shore' in d:
            o.on_off_shore = d['on_off_shore']
        if 'origin_rate_inst' in d:
            o.origin_rate_inst = d['origin_rate_inst']
        if 'origin_rate_ref' in d:
            o.origin_rate_ref = d['origin_rate_ref']
        if 'period' in d:
            o.period = d['period']
        if 'profile_id' in d:
            o.profile_id = d['profile_id']
        if 'quote_ccy' in d:
            o.quote_ccy = d['quote_ccy']
        if 'rate_ref' in d:
            o.rate_ref = d['rate_ref']
        if 'rate_time' in d:
            o.rate_time = d['rate_time']
        if 'rate_type' in d:
            o.rate_type = d['rate_type']
        if 'sp_bid' in d:
            o.sp_bid = d['sp_bid']
        if 'sp_mid' in d:
            o.sp_mid = d['sp_mid']
        if 'sp_offer' in d:
            o.sp_offer = d['sp_offer']
        if 'standard_product_rate_id' in d:
            o.standard_product_rate_id = d['standard_product_rate_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_agreement_id' in d:
            o.sub_agreement_id = d['sub_agreement_id']
        if 'threshold_time' in d:
            o.threshold_time = d['threshold_time']
        if 'time_zone' in d:
            o.time_zone = d['time_zone']
        if 'transaction_ccy_type' in d:
            o.transaction_ccy_type = d['transaction_ccy_type']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        return o


