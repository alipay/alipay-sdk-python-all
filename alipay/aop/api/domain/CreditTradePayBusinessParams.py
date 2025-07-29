#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreditTradePayBusinessParams(object):

    def __init__(self):
        self._credit_biz_params = None

    @property
    def credit_biz_params(self):
        return self._credit_biz_params

    @credit_biz_params.setter
    def credit_biz_params(self, value):
        self._credit_biz_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_biz_params:
            if hasattr(self.credit_biz_params, 'to_alipay_dict'):
                params['credit_biz_params'] = self.credit_biz_params.to_alipay_dict()
            else:
                params['credit_biz_params'] = self.credit_biz_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreditTradePayBusinessParams()
        if 'credit_biz_params' in d:
            o.credit_biz_params = d['credit_biz_params']
        return o


