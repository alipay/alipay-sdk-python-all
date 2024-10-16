#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMerchantcardSettleaccountBatchqueryModel(object):

    def __init__(self):
        self._support_deduct = None

    @property
    def support_deduct(self):
        return self._support_deduct

    @support_deduct.setter
    def support_deduct(self, value):
        self._support_deduct = value


    def to_alipay_dict(self):
        params = dict()
        if self.support_deduct:
            if hasattr(self.support_deduct, 'to_alipay_dict'):
                params['support_deduct'] = self.support_deduct.to_alipay_dict()
            else:
                params['support_deduct'] = self.support_deduct
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardSettleaccountBatchqueryModel()
        if 'support_deduct' in d:
            o.support_deduct = d['support_deduct']
        return o


