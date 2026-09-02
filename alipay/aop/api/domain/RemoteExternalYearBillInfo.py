#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RemoteExternalBillDetail import RemoteExternalBillDetail


class RemoteExternalYearBillInfo(object):

    def __init__(self):
        self._external_bill_details = None
        self._total_amount = None
        self._year = None

    @property
    def external_bill_details(self):
        return self._external_bill_details

    @external_bill_details.setter
    def external_bill_details(self, value):
        if isinstance(value, list):
            self._external_bill_details = list()
            for i in value:
                if isinstance(i, RemoteExternalBillDetail):
                    self._external_bill_details.append(i)
                else:
                    self._external_bill_details.append(RemoteExternalBillDetail.from_alipay_dict(i))
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_bill_details:
            if isinstance(self.external_bill_details, list):
                for i in range(0, len(self.external_bill_details)):
                    element = self.external_bill_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.external_bill_details[i] = element.to_alipay_dict()
            if hasattr(self.external_bill_details, 'to_alipay_dict'):
                params['external_bill_details'] = self.external_bill_details.to_alipay_dict()
            else:
                params['external_bill_details'] = self.external_bill_details
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.year:
            if hasattr(self.year, 'to_alipay_dict'):
                params['year'] = self.year.to_alipay_dict()
            else:
                params['year'] = self.year
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RemoteExternalYearBillInfo()
        if 'external_bill_details' in d:
            o.external_bill_details = d['external_bill_details']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'year' in d:
            o.year = d['year']
        return o


