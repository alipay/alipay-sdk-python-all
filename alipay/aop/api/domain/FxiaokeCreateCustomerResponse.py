#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FxiaokeCreateCustomerResponse(object):

    def __init__(self):
        self._bid = None
        self._id = None
        self._intertrade_ou_code = None
        self._intertrade_type = None

    @property
    def bid(self):
        return self._bid

    @bid.setter
    def bid(self, value):
        self._bid = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def intertrade_ou_code(self):
        return self._intertrade_ou_code

    @intertrade_ou_code.setter
    def intertrade_ou_code(self, value):
        self._intertrade_ou_code = value
    @property
    def intertrade_type(self):
        return self._intertrade_type

    @intertrade_type.setter
    def intertrade_type(self, value):
        self._intertrade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bid:
            if hasattr(self.bid, 'to_alipay_dict'):
                params['bid'] = self.bid.to_alipay_dict()
            else:
                params['bid'] = self.bid
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.intertrade_ou_code:
            if hasattr(self.intertrade_ou_code, 'to_alipay_dict'):
                params['intertrade_ou_code'] = self.intertrade_ou_code.to_alipay_dict()
            else:
                params['intertrade_ou_code'] = self.intertrade_ou_code
        if self.intertrade_type:
            if hasattr(self.intertrade_type, 'to_alipay_dict'):
                params['intertrade_type'] = self.intertrade_type.to_alipay_dict()
            else:
                params['intertrade_type'] = self.intertrade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeCreateCustomerResponse()
        if 'bid' in d:
            o.bid = d['bid']
        if 'id' in d:
            o.id = d['id']
        if 'intertrade_ou_code' in d:
            o.intertrade_ou_code = d['intertrade_ou_code']
        if 'intertrade_type' in d:
            o.intertrade_type = d['intertrade_type']
        return o


