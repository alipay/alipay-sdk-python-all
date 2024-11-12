#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditIsvwithdrawQueryModel(object):

    def __init__(self):
        self._alipay_pay_no = None
        self._enterprise_id = None

    @property
    def alipay_pay_no(self):
        return self._alipay_pay_no

    @alipay_pay_no.setter
    def alipay_pay_no(self, value):
        self._alipay_pay_no = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_pay_no:
            if hasattr(self.alipay_pay_no, 'to_alipay_dict'):
                params['alipay_pay_no'] = self.alipay_pay_no.to_alipay_dict()
            else:
                params['alipay_pay_no'] = self.alipay_pay_no
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditIsvwithdrawQueryModel()
        if 'alipay_pay_no' in d:
            o.alipay_pay_no = d['alipay_pay_no']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        return o


