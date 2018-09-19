#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayYebLqdDataResult(object):

    def __init__(self):
        self._predict_purchase_amt = None
        self._predict_redeem_amt = None
        self._target_date = None

    @property
    def predict_purchase_amt(self):
        return self._predict_purchase_amt

    @predict_purchase_amt.setter
    def predict_purchase_amt(self, value):
        self._predict_purchase_amt = value
    @property
    def predict_redeem_amt(self):
        return self._predict_redeem_amt

    @predict_redeem_amt.setter
    def predict_redeem_amt(self, value):
        self._predict_redeem_amt = value
    @property
    def target_date(self):
        return self._target_date

    @target_date.setter
    def target_date(self, value):
        self._target_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.predict_purchase_amt:
            if hasattr(self.predict_purchase_amt, 'to_alipay_dict'):
                params['predict_purchase_amt'] = self.predict_purchase_amt.to_alipay_dict()
            else:
                params['predict_purchase_amt'] = self.predict_purchase_amt
        if self.predict_redeem_amt:
            if hasattr(self.predict_redeem_amt, 'to_alipay_dict'):
                params['predict_redeem_amt'] = self.predict_redeem_amt.to_alipay_dict()
            else:
                params['predict_redeem_amt'] = self.predict_redeem_amt
        if self.target_date:
            if hasattr(self.target_date, 'to_alipay_dict'):
                params['target_date'] = self.target_date.to_alipay_dict()
            else:
                params['target_date'] = self.target_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayYebLqdDataResult()
        if 'predict_purchase_amt' in d:
            o.predict_purchase_amt = d['predict_purchase_amt']
        if 'predict_redeem_amt' in d:
            o.predict_redeem_amt = d['predict_redeem_amt']
        if 'target_date' in d:
            o.target_date = d['target_date']
        return o


