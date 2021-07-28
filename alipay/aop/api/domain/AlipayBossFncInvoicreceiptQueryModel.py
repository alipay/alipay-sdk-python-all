#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncInvoicreceiptQueryModel(object):

    def __init__(self):
        self._statement_bill_nos = None

    @property
    def statement_bill_nos(self):
        return self._statement_bill_nos

    @statement_bill_nos.setter
    def statement_bill_nos(self, value):
        if isinstance(value, list):
            self._statement_bill_nos = list()
            for i in value:
                self._statement_bill_nos.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.statement_bill_nos:
            if isinstance(self.statement_bill_nos, list):
                for i in range(0, len(self.statement_bill_nos)):
                    element = self.statement_bill_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.statement_bill_nos[i] = element.to_alipay_dict()
            if hasattr(self.statement_bill_nos, 'to_alipay_dict'):
                params['statement_bill_nos'] = self.statement_bill_nos.to_alipay_dict()
            else:
                params['statement_bill_nos'] = self.statement_bill_nos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvoicreceiptQueryModel()
        if 'statement_bill_nos' in d:
            o.statement_bill_nos = d['statement_bill_nos']
        return o


