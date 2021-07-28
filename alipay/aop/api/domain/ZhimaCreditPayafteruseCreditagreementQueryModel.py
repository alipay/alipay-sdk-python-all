#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPayafteruseCreditagreementQueryModel(object):

    def __init__(self):
        self._credit_agreement_id = None
        self._out_agreement_no = None

    @property
    def credit_agreement_id(self):
        return self._credit_agreement_id

    @credit_agreement_id.setter
    def credit_agreement_id(self, value):
        self._credit_agreement_id = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_agreement_id:
            if hasattr(self.credit_agreement_id, 'to_alipay_dict'):
                params['credit_agreement_id'] = self.credit_agreement_id.to_alipay_dict()
            else:
                params['credit_agreement_id'] = self.credit_agreement_id
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditPayafteruseCreditagreementQueryModel()
        if 'credit_agreement_id' in d:
            o.credit_agreement_id = d['credit_agreement_id']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        return o


