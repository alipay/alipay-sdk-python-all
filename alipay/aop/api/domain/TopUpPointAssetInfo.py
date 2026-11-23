#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TopUpPointAssetInfo(object):

    def __init__(self):
        self._amount = None
        self._pre_consult_id = None
        self._top_up_point_amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def pre_consult_id(self):
        return self._pre_consult_id

    @pre_consult_id.setter
    def pre_consult_id(self, value):
        self._pre_consult_id = value
    @property
    def top_up_point_amount(self):
        return self._top_up_point_amount

    @top_up_point_amount.setter
    def top_up_point_amount(self, value):
        self._top_up_point_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.pre_consult_id:
            if hasattr(self.pre_consult_id, 'to_alipay_dict'):
                params['pre_consult_id'] = self.pre_consult_id.to_alipay_dict()
            else:
                params['pre_consult_id'] = self.pre_consult_id
        if self.top_up_point_amount:
            if hasattr(self.top_up_point_amount, 'to_alipay_dict'):
                params['top_up_point_amount'] = self.top_up_point_amount.to_alipay_dict()
            else:
                params['top_up_point_amount'] = self.top_up_point_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TopUpPointAssetInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'pre_consult_id' in d:
            o.pre_consult_id = d['pre_consult_id']
        if 'top_up_point_amount' in d:
            o.top_up_point_amount = d['top_up_point_amount']
        return o


