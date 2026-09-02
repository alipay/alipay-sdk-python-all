#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RemoteExternalBillDetail import RemoteExternalBillDetail


class RemoteExternalBillGroupInfo(object):

    def __init__(self):
        self._bill_info_title = None
        self._external_bill_details = None
        self._total_amount = None

    @property
    def bill_info_title(self):
        return self._bill_info_title

    @bill_info_title.setter
    def bill_info_title(self, value):
        self._bill_info_title = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.bill_info_title:
            if hasattr(self.bill_info_title, 'to_alipay_dict'):
                params['bill_info_title'] = self.bill_info_title.to_alipay_dict()
            else:
                params['bill_info_title'] = self.bill_info_title
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RemoteExternalBillGroupInfo()
        if 'bill_info_title' in d:
            o.bill_info_title = d['bill_info_title']
        if 'external_bill_details' in d:
            o.external_bill_details = d['external_bill_details']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


