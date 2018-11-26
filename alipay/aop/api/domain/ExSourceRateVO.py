#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExSourceRateVO(object):

    def __init__(self):
        self._bid = None
        self._currency_pair = None
        self._currency_unit = None
        self._expiry_time = None
        self._extended_params = None
        self._generate_date = None
        self._generate_time = None
        self._gmt_create = None
        self._gmt_modified = None
        self._guaranteed = None
        self._id = None
        self._inst = None
        self._inst_rate_reference_id = None
        self._is_exception = None
        self._is_flat = None
        self._is_formatted = None
        self._is_valid = None
        self._maturity_date = None
        self._maximum_bid_amount = None
        self._maximum_offer_amount = None
        self._memo = None
        self._mid = None
        self._minimum_bid_amount = None
        self._minimum_offer_amount = None
        self._offer = None
        self._on_off_shore = None
        self._period = None
        self._profile = None
        self._quote_type = None
        self._rate_method = None
        self._rate_source_code = None
        self._rate_type = None
        self._segment_id = None
        self._sp_bid = None
        self._sp_mid = None
        self._sp_offer = None
        self._start_time = None
        self._sub_inst = None
        self._threshold_time = None
        self._valid_time = None
        self._zone_expiry_time = None
        self._zone_generate_time = None
        self._zone_gmt_create = None
        self._zone_gmt_modified = None
        self._zone_start_time = None
        self._zone_threshold_time = None
        self._zone_valid_time = None

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def currency_pair(self):
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, value):
        self._currency_pair = value
    @property
    def currency_unit(self):
        return self._currency_unit

    @currency_unit.setter
    def currency_unit(self, value):
        self._currency_unit = value
    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def extended_params(self):
        return self._extended_params

    @extended_params.setter
    def extended_params(self, value):
        self._extended_params = value
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
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def guaranteed(self):
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, value):
        self._guaranteed = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def inst(self):
        return self._inst

    @inst.setter
    def inst(self, value):
        self._inst = value
    @property
    def inst_rate_reference_id(self):
        return self._inst_rate_reference_id

    @inst_rate_reference_id.setter
    def inst_rate_reference_id(self, value):
        self._inst_rate_reference_id = value
    @property
    def is_exception(self):
        return self._is_exception

    @is_exception.setter
    def is_exception(self, value):
        self._is_exception = value
    @property
    def is_flat(self):
        return self._is_flat

    @is_flat.setter
    def is_flat(self, value):
        self._is_flat = value
    @property
    def is_formatted(self):
        return self._is_formatted

    @is_formatted.setter
    def is_formatted(self, value):
        self._is_formatted = value
    @property
    def is_valid(self):
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value
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
    def on_off_shore(self):
        return self._on_off_shore

    @on_off_shore.setter
    def on_off_shore(self, value):
        self._on_off_shore = value
    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def profile(self):
        return self._profile

    @profile.setter
    def profile(self, value):
        self._profile = value
    @property
    def quote_type(self):
        return self._quote_type

    @quote_type.setter
    def quote_type(self, value):
        self._quote_type = value
    @property
    def rate_method(self):
        return self._rate_method

    @rate_method.setter
    def rate_method(self, value):
        self._rate_method = value
    @property
    def rate_source_code(self):
        return self._rate_source_code

    @rate_source_code.setter
    def rate_source_code(self, value):
        self._rate_source_code = value
    @property
    def rate_type(self):
        return self._rate_type

    @rate_type.setter
    def rate_type(self, value):
        self._rate_type = value
    @property
    def segment_id(self):
        return self._segment_id

    @segment_id.setter
    def segment_id(self, value):
        self._segment_id = value
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
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_inst(self):
        return self._sub_inst

    @sub_inst.setter
    def sub_inst(self, value):
        self._sub_inst = value
    @property
    def threshold_time(self):
        return self._threshold_time

    @threshold_time.setter
    def threshold_time(self, value):
        self._threshold_time = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value
    @property
    def zone_expiry_time(self):
        return self._zone_expiry_time

    @zone_expiry_time.setter
    def zone_expiry_time(self, value):
        self._zone_expiry_time = value
    @property
    def zone_generate_time(self):
        return self._zone_generate_time

    @zone_generate_time.setter
    def zone_generate_time(self, value):
        self._zone_generate_time = value
    @property
    def zone_gmt_create(self):
        return self._zone_gmt_create

    @zone_gmt_create.setter
    def zone_gmt_create(self, value):
        self._zone_gmt_create = value
    @property
    def zone_gmt_modified(self):
        return self._zone_gmt_modified

    @zone_gmt_modified.setter
    def zone_gmt_modified(self, value):
        self._zone_gmt_modified = value
    @property
    def zone_start_time(self):
        return self._zone_start_time

    @zone_start_time.setter
    def zone_start_time(self, value):
        self._zone_start_time = value
    @property
    def zone_threshold_time(self):
        return self._zone_threshold_time

    @zone_threshold_time.setter
    def zone_threshold_time(self, value):
        self._zone_threshold_time = value
    @property
    def zone_valid_time(self):
        return self._zone_valid_time

    @zone_valid_time.setter
    def zone_valid_time(self, value):
        self._zone_valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.currency_pair:
            if hasattr(self.currency_pair, 'to_alipay_dict'):
                params['currency_pair'] = self.currency_pair.to_alipay_dict()
            else:
                params['currency_pair'] = self.currency_pair
        if self.currency_unit:
            if hasattr(self.currency_unit, 'to_alipay_dict'):
                params['currency_unit'] = self.currency_unit.to_alipay_dict()
            else:
                params['currency_unit'] = self.currency_unit
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.extended_params:
            if hasattr(self.extended_params, 'to_alipay_dict'):
                params['extended_params'] = self.extended_params.to_alipay_dict()
            else:
                params['extended_params'] = self.extended_params
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
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.guaranteed:
            if hasattr(self.guaranteed, 'to_alipay_dict'):
                params['guaranteed'] = self.guaranteed.to_alipay_dict()
            else:
                params['guaranteed'] = self.guaranteed
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.inst:
            if hasattr(self.inst, 'to_alipay_dict'):
                params['inst'] = self.inst.to_alipay_dict()
            else:
                params['inst'] = self.inst
        if self.inst_rate_reference_id:
            if hasattr(self.inst_rate_reference_id, 'to_alipay_dict'):
                params['inst_rate_reference_id'] = self.inst_rate_reference_id.to_alipay_dict()
            else:
                params['inst_rate_reference_id'] = self.inst_rate_reference_id
        if self.is_exception:
            if hasattr(self.is_exception, 'to_alipay_dict'):
                params['is_exception'] = self.is_exception.to_alipay_dict()
            else:
                params['is_exception'] = self.is_exception
        if self.is_flat:
            if hasattr(self.is_flat, 'to_alipay_dict'):
                params['is_flat'] = self.is_flat.to_alipay_dict()
            else:
                params['is_flat'] = self.is_flat
        if self.is_formatted:
            if hasattr(self.is_formatted, 'to_alipay_dict'):
                params['is_formatted'] = self.is_formatted.to_alipay_dict()
            else:
                params['is_formatted'] = self.is_formatted
        if self.is_valid:
            if hasattr(self.is_valid, 'to_alipay_dict'):
                params['is_valid'] = self.is_valid.to_alipay_dict()
            else:
                params['is_valid'] = self.is_valid
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
        if self.on_off_shore:
            if hasattr(self.on_off_shore, 'to_alipay_dict'):
                params['on_off_shore'] = self.on_off_shore.to_alipay_dict()
            else:
                params['on_off_shore'] = self.on_off_shore
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.profile:
            if hasattr(self.profile, 'to_alipay_dict'):
                params['profile'] = self.profile.to_alipay_dict()
            else:
                params['profile'] = self.profile
        if self.quote_type:
            if hasattr(self.quote_type, 'to_alipay_dict'):
                params['quote_type'] = self.quote_type.to_alipay_dict()
            else:
                params['quote_type'] = self.quote_type
        if self.rate_method:
            if hasattr(self.rate_method, 'to_alipay_dict'):
                params['rate_method'] = self.rate_method.to_alipay_dict()
            else:
                params['rate_method'] = self.rate_method
        if self.rate_source_code:
            if hasattr(self.rate_source_code, 'to_alipay_dict'):
                params['rate_source_code'] = self.rate_source_code.to_alipay_dict()
            else:
                params['rate_source_code'] = self.rate_source_code
        if self.rate_type:
            if hasattr(self.rate_type, 'to_alipay_dict'):
                params['rate_type'] = self.rate_type.to_alipay_dict()
            else:
                params['rate_type'] = self.rate_type
        if self.segment_id:
            if hasattr(self.segment_id, 'to_alipay_dict'):
                params['segment_id'] = self.segment_id.to_alipay_dict()
            else:
                params['segment_id'] = self.segment_id
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
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_inst:
            if hasattr(self.sub_inst, 'to_alipay_dict'):
                params['sub_inst'] = self.sub_inst.to_alipay_dict()
            else:
                params['sub_inst'] = self.sub_inst
        if self.threshold_time:
            if hasattr(self.threshold_time, 'to_alipay_dict'):
                params['threshold_time'] = self.threshold_time.to_alipay_dict()
            else:
                params['threshold_time'] = self.threshold_time
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        if self.zone_expiry_time:
            if hasattr(self.zone_expiry_time, 'to_alipay_dict'):
                params['zone_expiry_time'] = self.zone_expiry_time.to_alipay_dict()
            else:
                params['zone_expiry_time'] = self.zone_expiry_time
        if self.zone_generate_time:
            if hasattr(self.zone_generate_time, 'to_alipay_dict'):
                params['zone_generate_time'] = self.zone_generate_time.to_alipay_dict()
            else:
                params['zone_generate_time'] = self.zone_generate_time
        if self.zone_gmt_create:
            if hasattr(self.zone_gmt_create, 'to_alipay_dict'):
                params['zone_gmt_create'] = self.zone_gmt_create.to_alipay_dict()
            else:
                params['zone_gmt_create'] = self.zone_gmt_create
        if self.zone_gmt_modified:
            if hasattr(self.zone_gmt_modified, 'to_alipay_dict'):
                params['zone_gmt_modified'] = self.zone_gmt_modified.to_alipay_dict()
            else:
                params['zone_gmt_modified'] = self.zone_gmt_modified
        if self.zone_start_time:
            if hasattr(self.zone_start_time, 'to_alipay_dict'):
                params['zone_start_time'] = self.zone_start_time.to_alipay_dict()
            else:
                params['zone_start_time'] = self.zone_start_time
        if self.zone_threshold_time:
            if hasattr(self.zone_threshold_time, 'to_alipay_dict'):
                params['zone_threshold_time'] = self.zone_threshold_time.to_alipay_dict()
            else:
                params['zone_threshold_time'] = self.zone_threshold_time
        if self.zone_valid_time:
            if hasattr(self.zone_valid_time, 'to_alipay_dict'):
                params['zone_valid_time'] = self.zone_valid_time.to_alipay_dict()
            else:
                params['zone_valid_time'] = self.zone_valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExSourceRateVO()
        if 'bid' in d:
            o.bid = d['bid']
        if 'currency_pair' in d:
            o.currency_pair = d['currency_pair']
        if 'currency_unit' in d:
            o.currency_unit = d['currency_unit']
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'extended_params' in d:
            o.extended_params = d['extended_params']
        if 'generate_date' in d:
            o.generate_date = d['generate_date']
        if 'generate_time' in d:
            o.generate_time = d['generate_time']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'guaranteed' in d:
            o.guaranteed = d['guaranteed']
        if 'id' in d:
            o.id = d['id']
        if 'inst' in d:
            o.inst = d['inst']
        if 'inst_rate_reference_id' in d:
            o.inst_rate_reference_id = d['inst_rate_reference_id']
        if 'is_exception' in d:
            o.is_exception = d['is_exception']
        if 'is_flat' in d:
            o.is_flat = d['is_flat']
        if 'is_formatted' in d:
            o.is_formatted = d['is_formatted']
        if 'is_valid' in d:
            o.is_valid = d['is_valid']
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
        if 'on_off_shore' in d:
            o.on_off_shore = d['on_off_shore']
        if 'period' in d:
            o.period = d['period']
        if 'profile' in d:
            o.profile = d['profile']
        if 'quote_type' in d:
            o.quote_type = d['quote_type']
        if 'rate_method' in d:
            o.rate_method = d['rate_method']
        if 'rate_source_code' in d:
            o.rate_source_code = d['rate_source_code']
        if 'rate_type' in d:
            o.rate_type = d['rate_type']
        if 'segment_id' in d:
            o.segment_id = d['segment_id']
        if 'sp_bid' in d:
            o.sp_bid = d['sp_bid']
        if 'sp_mid' in d:
            o.sp_mid = d['sp_mid']
        if 'sp_offer' in d:
            o.sp_offer = d['sp_offer']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_inst' in d:
            o.sub_inst = d['sub_inst']
        if 'threshold_time' in d:
            o.threshold_time = d['threshold_time']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        if 'zone_expiry_time' in d:
            o.zone_expiry_time = d['zone_expiry_time']
        if 'zone_generate_time' in d:
            o.zone_generate_time = d['zone_generate_time']
        if 'zone_gmt_create' in d:
            o.zone_gmt_create = d['zone_gmt_create']
        if 'zone_gmt_modified' in d:
            o.zone_gmt_modified = d['zone_gmt_modified']
        if 'zone_start_time' in d:
            o.zone_start_time = d['zone_start_time']
        if 'zone_threshold_time' in d:
            o.zone_threshold_time = d['zone_threshold_time']
        if 'zone_valid_time' in d:
            o.zone_valid_time = d['zone_valid_time']
        return o


