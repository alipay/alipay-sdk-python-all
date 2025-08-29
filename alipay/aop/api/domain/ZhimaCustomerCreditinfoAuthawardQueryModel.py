#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerCreditinfoAuthawardQueryModel(object):

    def __init__(self):
        self._out_agreement_no = None

    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value


    def to_alipay_dict(self):
        params = dict()
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
        o = ZhimaCustomerCreditinfoAuthawardQueryModel()
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        return o


