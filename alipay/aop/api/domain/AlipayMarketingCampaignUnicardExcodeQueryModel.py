#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignUnicardExcodeQueryModel(object):

    def __init__(self):
        self._exchange_code = None

    @property
    def exchange_code(self):
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, value):
        self._exchange_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.exchange_code:
            if hasattr(self.exchange_code, 'to_alipay_dict'):
                params['exchange_code'] = self.exchange_code.to_alipay_dict()
            else:
                params['exchange_code'] = self.exchange_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignUnicardExcodeQueryModel()
        if 'exchange_code' in d:
            o.exchange_code = d['exchange_code']
        return o


