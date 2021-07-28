#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayAccountClearingcenterPayoffQueryModel(object):

    def __init__(self):
        self._currency = None
        self._instid = None
        self._status = None

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def instid(self):
        return self._instid

    @instid.setter
    def instid(self, value):
        self._instid = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.instid:
            if hasattr(self.instid, 'to_alipay_dict'):
                params['instid'] = self.instid.to_alipay_dict()
            else:
                params['instid'] = self.instid
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountClearingcenterPayoffQueryModel()
        if 'currency' in d:
            o.currency = d['currency']
        if 'instid' in d:
            o.instid = d['instid']
        if 'status' in d:
            o.status = d['status']
        return o


