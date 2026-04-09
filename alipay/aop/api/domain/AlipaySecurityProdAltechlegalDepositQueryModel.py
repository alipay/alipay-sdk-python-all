#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdAltechlegalDepositQueryModel(object):

    def __init__(self):
        self._deposit_no = None

    @property
    def deposit_no(self):
        return self._deposit_no

    @deposit_no.setter
    def deposit_no(self, value):
        self._deposit_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.deposit_no:
            if hasattr(self.deposit_no, 'to_alipay_dict'):
                params['deposit_no'] = self.deposit_no.to_alipay_dict()
            else:
                params['deposit_no'] = self.deposit_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdAltechlegalDepositQueryModel()
        if 'deposit_no' in d:
            o.deposit_no = d['deposit_no']
        return o


