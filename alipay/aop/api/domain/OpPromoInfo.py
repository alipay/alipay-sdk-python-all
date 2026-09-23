#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpPromoInfo(object):

    def __init__(self):
        self._promo_cnt = None
        self._promo_desc = None
        self._promo_expired_time = None
        self._promo_id = None
        self._promo_name = None
        self._promo_price = None
        self._promo_type = None
        self._promo_unit = None

    @property
    def promo_cnt(self):
        return self._promo_cnt

    @promo_cnt.setter
    def promo_cnt(self, value):
        self._promo_cnt = value
    @property
    def promo_desc(self):
        return self._promo_desc

    @promo_desc.setter
    def promo_desc(self, value):
        self._promo_desc = value
    @property
    def promo_expired_time(self):
        return self._promo_expired_time

    @promo_expired_time.setter
    def promo_expired_time(self, value):
        self._promo_expired_time = value
    @property
    def promo_id(self):
        return self._promo_id

    @promo_id.setter
    def promo_id(self, value):
        self._promo_id = value
    @property
    def promo_name(self):
        return self._promo_name

    @promo_name.setter
    def promo_name(self, value):
        self._promo_name = value
    @property
    def promo_price(self):
        return self._promo_price

    @promo_price.setter
    def promo_price(self, value):
        self._promo_price = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def promo_unit(self):
        return self._promo_unit

    @promo_unit.setter
    def promo_unit(self, value):
        self._promo_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.promo_cnt:
            if hasattr(self.promo_cnt, 'to_alipay_dict'):
                params['promo_cnt'] = self.promo_cnt.to_alipay_dict()
            else:
                params['promo_cnt'] = self.promo_cnt
        if self.promo_desc:
            if hasattr(self.promo_desc, 'to_alipay_dict'):
                params['promo_desc'] = self.promo_desc.to_alipay_dict()
            else:
                params['promo_desc'] = self.promo_desc
        if self.promo_expired_time:
            if hasattr(self.promo_expired_time, 'to_alipay_dict'):
                params['promo_expired_time'] = self.promo_expired_time.to_alipay_dict()
            else:
                params['promo_expired_time'] = self.promo_expired_time
        if self.promo_id:
            if hasattr(self.promo_id, 'to_alipay_dict'):
                params['promo_id'] = self.promo_id.to_alipay_dict()
            else:
                params['promo_id'] = self.promo_id
        if self.promo_name:
            if hasattr(self.promo_name, 'to_alipay_dict'):
                params['promo_name'] = self.promo_name.to_alipay_dict()
            else:
                params['promo_name'] = self.promo_name
        if self.promo_price:
            if hasattr(self.promo_price, 'to_alipay_dict'):
                params['promo_price'] = self.promo_price.to_alipay_dict()
            else:
                params['promo_price'] = self.promo_price
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.promo_unit:
            if hasattr(self.promo_unit, 'to_alipay_dict'):
                params['promo_unit'] = self.promo_unit.to_alipay_dict()
            else:
                params['promo_unit'] = self.promo_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpPromoInfo()
        if 'promo_cnt' in d:
            o.promo_cnt = d['promo_cnt']
        if 'promo_desc' in d:
            o.promo_desc = d['promo_desc']
        if 'promo_expired_time' in d:
            o.promo_expired_time = d['promo_expired_time']
        if 'promo_id' in d:
            o.promo_id = d['promo_id']
        if 'promo_name' in d:
            o.promo_name = d['promo_name']
        if 'promo_price' in d:
            o.promo_price = d['promo_price']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'promo_unit' in d:
            o.promo_unit = d['promo_unit']
        return o


