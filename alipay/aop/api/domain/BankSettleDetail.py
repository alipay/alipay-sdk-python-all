#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BankSettleDetail(object):

    def __init__(self):
        self._royalty_type = None
        self._settle_amt = None

    @property
    def royalty_type(self):
        return self._royalty_type

    @royalty_type.setter
    def royalty_type(self, value):
        self._royalty_type = value
    @property
    def settle_amt(self):
        return self._settle_amt

    @settle_amt.setter
    def settle_amt(self, value):
        self._settle_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalty_type:
            if hasattr(self.royalty_type, 'to_alipay_dict'):
                params['royalty_type'] = self.royalty_type.to_alipay_dict()
            else:
                params['royalty_type'] = self.royalty_type
        if self.settle_amt:
            if hasattr(self.settle_amt, 'to_alipay_dict'):
                params['settle_amt'] = self.settle_amt.to_alipay_dict()
            else:
                params['settle_amt'] = self.settle_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BankSettleDetail()
        if 'royalty_type' in d:
            o.royalty_type = d['royalty_type']
        if 'settle_amt' in d:
            o.settle_amt = d['settle_amt']
        return o


