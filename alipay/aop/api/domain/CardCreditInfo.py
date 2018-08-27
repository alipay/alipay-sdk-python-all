#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardCreditInfo(object):

    def __init__(self):
        self._allowoverpay = None
        self._creditquota = None

    @property
    def allowoverpay(self):
        return self._allowoverpay

    @allowoverpay.setter
    def allowoverpay(self, value):
        self._allowoverpay = value
    @property
    def creditquota(self):
        return self._creditquota

    @creditquota.setter
    def creditquota(self, value):
        self._creditquota = value


    def to_alipay_dict(self):
        params = dict()
        if self.allowoverpay:
            if hasattr(self.allowoverpay, 'to_alipay_dict'):
                params['allowoverpay'] = self.allowoverpay.to_alipay_dict()
            else:
                params['allowoverpay'] = self.allowoverpay
        if self.creditquota:
            if hasattr(self.creditquota, 'to_alipay_dict'):
                params['creditquota'] = self.creditquota.to_alipay_dict()
            else:
                params['creditquota'] = self.creditquota
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardCreditInfo()
        if 'allowoverpay' in d:
            o.allowoverpay = d['allowoverpay']
        if 'creditquota' in d:
            o.creditquota = d['creditquota']
        return o


