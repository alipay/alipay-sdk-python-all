#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ForbbidenTime import ForbbidenTime
from alipay.aop.api.domain.UseTime import UseTime


class VoucherDetailInfo(object):

    def __init__(self):
        self._asset_id = None
        self._effect_time = None
        self._ext_info = None
        self._forbbiden_time = None
        self._invalid_time = None
        self._sku_codes = None
        self._time_rules = None
        self._use_condition = None
        self._voucher_desc = None
        self._voucher_type = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def forbbiden_time(self):
        return self._forbbiden_time

    @forbbiden_time.setter
    def forbbiden_time(self, value):
        if isinstance(value, ForbbidenTime):
            self._forbbiden_time = value
        else:
            self._forbbiden_time = ForbbidenTime.from_alipay_dict(value)
    @property
    def invalid_time(self):
        return self._invalid_time

    @invalid_time.setter
    def invalid_time(self, value):
        self._invalid_time = value
    @property
    def sku_codes(self):
        return self._sku_codes

    @sku_codes.setter
    def sku_codes(self, value):
        self._sku_codes = value
    @property
    def time_rules(self):
        return self._time_rules

    @time_rules.setter
    def time_rules(self, value):
        if isinstance(value, list):
            self._time_rules = list()
            for i in value:
                if isinstance(i, UseTime):
                    self._time_rules.append(i)
                else:
                    self._time_rules.append(UseTime.from_alipay_dict(i))
    @property
    def use_condition(self):
        return self._use_condition

    @use_condition.setter
    def use_condition(self, value):
        self._use_condition = value
    @property
    def voucher_desc(self):
        return self._voucher_desc

    @voucher_desc.setter
    def voucher_desc(self, value):
        self._voucher_desc = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.forbbiden_time:
            if hasattr(self.forbbiden_time, 'to_alipay_dict'):
                params['forbbiden_time'] = self.forbbiden_time.to_alipay_dict()
            else:
                params['forbbiden_time'] = self.forbbiden_time
        if self.invalid_time:
            if hasattr(self.invalid_time, 'to_alipay_dict'):
                params['invalid_time'] = self.invalid_time.to_alipay_dict()
            else:
                params['invalid_time'] = self.invalid_time
        if self.sku_codes:
            if hasattr(self.sku_codes, 'to_alipay_dict'):
                params['sku_codes'] = self.sku_codes.to_alipay_dict()
            else:
                params['sku_codes'] = self.sku_codes
        if self.time_rules:
            if isinstance(self.time_rules, list):
                for i in range(0, len(self.time_rules)):
                    element = self.time_rules[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.time_rules[i] = element.to_alipay_dict()
            if hasattr(self.time_rules, 'to_alipay_dict'):
                params['time_rules'] = self.time_rules.to_alipay_dict()
            else:
                params['time_rules'] = self.time_rules
        if self.use_condition:
            if hasattr(self.use_condition, 'to_alipay_dict'):
                params['use_condition'] = self.use_condition.to_alipay_dict()
            else:
                params['use_condition'] = self.use_condition
        if self.voucher_desc:
            if hasattr(self.voucher_desc, 'to_alipay_dict'):
                params['voucher_desc'] = self.voucher_desc.to_alipay_dict()
            else:
                params['voucher_desc'] = self.voucher_desc
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherDetailInfo()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'forbbiden_time' in d:
            o.forbbiden_time = d['forbbiden_time']
        if 'invalid_time' in d:
            o.invalid_time = d['invalid_time']
        if 'sku_codes' in d:
            o.sku_codes = d['sku_codes']
        if 'time_rules' in d:
            o.time_rules = d['time_rules']
        if 'use_condition' in d:
            o.use_condition = d['use_condition']
        if 'voucher_desc' in d:
            o.voucher_desc = d['voucher_desc']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


