#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AssetEcoFeeDetail(object):

    def __init__(self):
        self._bill_entity = None
        self._fee_price = None
        self._fee_time = None
        self._fee_type = None
        self._unbill_reason = None

    @property
    def bill_entity(self):
        return self._bill_entity

    @bill_entity.setter
    def bill_entity(self, value):
        self._bill_entity = value
    @property
    def fee_price(self):
        return self._fee_price

    @fee_price.setter
    def fee_price(self, value):
        self._fee_price = value
    @property
    def fee_time(self):
        return self._fee_time

    @fee_time.setter
    def fee_time(self, value):
        self._fee_time = value
    @property
    def fee_type(self):
        return self._fee_type

    @fee_type.setter
    def fee_type(self, value):
        self._fee_type = value
    @property
    def unbill_reason(self):
        return self._unbill_reason

    @unbill_reason.setter
    def unbill_reason(self, value):
        self._unbill_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_entity:
            if hasattr(self.bill_entity, 'to_alipay_dict'):
                params['bill_entity'] = self.bill_entity.to_alipay_dict()
            else:
                params['bill_entity'] = self.bill_entity
        if self.fee_price:
            if hasattr(self.fee_price, 'to_alipay_dict'):
                params['fee_price'] = self.fee_price.to_alipay_dict()
            else:
                params['fee_price'] = self.fee_price
        if self.fee_time:
            if hasattr(self.fee_time, 'to_alipay_dict'):
                params['fee_time'] = self.fee_time.to_alipay_dict()
            else:
                params['fee_time'] = self.fee_time
        if self.fee_type:
            if hasattr(self.fee_type, 'to_alipay_dict'):
                params['fee_type'] = self.fee_type.to_alipay_dict()
            else:
                params['fee_type'] = self.fee_type
        if self.unbill_reason:
            if hasattr(self.unbill_reason, 'to_alipay_dict'):
                params['unbill_reason'] = self.unbill_reason.to_alipay_dict()
            else:
                params['unbill_reason'] = self.unbill_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AssetEcoFeeDetail()
        if 'bill_entity' in d:
            o.bill_entity = d['bill_entity']
        if 'fee_price' in d:
            o.fee_price = d['fee_price']
        if 'fee_time' in d:
            o.fee_time = d['fee_time']
        if 'fee_type' in d:
            o.fee_type = d['fee_type']
        if 'unbill_reason' in d:
            o.unbill_reason = d['unbill_reason']
        return o


