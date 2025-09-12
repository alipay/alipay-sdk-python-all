#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpInteopOrderCreateModel(object):

    def __init__(self):
        self._account = None
        self._service_market_order_no = None

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        self._account = value
    @property
    def service_market_order_no(self):
        return self._service_market_order_no

    @service_market_order_no.setter
    def service_market_order_no(self, value):
        self._service_market_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.account:
            if hasattr(self.account, 'to_alipay_dict'):
                params['account'] = self.account.to_alipay_dict()
            else:
                params['account'] = self.account
        if self.service_market_order_no:
            if hasattr(self.service_market_order_no, 'to_alipay_dict'):
                params['service_market_order_no'] = self.service_market_order_no.to_alipay_dict()
            else:
                params['service_market_order_no'] = self.service_market_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopOrderCreateModel()
        if 'account' in d:
            o.account = d['account']
        if 'service_market_order_no' in d:
            o.service_market_order_no = d['service_market_order_no']
        return o


