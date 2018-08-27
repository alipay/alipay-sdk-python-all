#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Member import Member


class MybankCreditSupplychainPrepaymentCancelModel(object):

    def __init__(self):
        self._buyer = None
        self._prepay_apply_no = None
        self._request_id = None

    @property
    def buyer(self):
        return self._buyer

    @buyer.setter
    def buyer(self, value):
        if isinstance(value, Member):
            self._buyer = value
        else:
            self._buyer = Member.from_alipay_dict(value)
    @property
    def prepay_apply_no(self):
        return self._prepay_apply_no

    @prepay_apply_no.setter
    def prepay_apply_no(self, value):
        self._prepay_apply_no = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer:
            if hasattr(self.buyer, 'to_alipay_dict'):
                params['buyer'] = self.buyer.to_alipay_dict()
            else:
                params['buyer'] = self.buyer
        if self.prepay_apply_no:
            if hasattr(self.prepay_apply_no, 'to_alipay_dict'):
                params['prepay_apply_no'] = self.prepay_apply_no.to_alipay_dict()
            else:
                params['prepay_apply_no'] = self.prepay_apply_no
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditSupplychainPrepaymentCancelModel()
        if 'buyer' in d:
            o.buyer = d['buyer']
        if 'prepay_apply_no' in d:
            o.prepay_apply_no = d['prepay_apply_no']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


