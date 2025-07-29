#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeAgentPayModel(object):

    def __init__(self):
        self._agreement_no = None
        self._prepay_id = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def prepay_id(self):
        return self._prepay_id

    @prepay_id.setter
    def prepay_id(self, value):
        self._prepay_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.prepay_id:
            if hasattr(self.prepay_id, 'to_alipay_dict'):
                params['prepay_id'] = self.prepay_id.to_alipay_dict()
            else:
                params['prepay_id'] = self.prepay_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeAgentPayModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'prepay_id' in d:
            o.prepay_id = d['prepay_id']
        return o


