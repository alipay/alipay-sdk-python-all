#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BizExtInfo import BizExtInfo


class BizOrderInfo(object):

    def __init__(self):
        self._amount = None
        self._ext_params = None
        self._partner_id = None
        self._seller_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        if isinstance(value, BizExtInfo):
            self._ext_params = value
        else:
            self._ext_params = BizExtInfo.from_alipay_dict(value)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizOrderInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        return o


