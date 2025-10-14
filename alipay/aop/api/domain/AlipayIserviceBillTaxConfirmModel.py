#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserBillTaxDetail import UserBillTaxDetail


class AlipayIserviceBillTaxConfirmModel(object):

    def __init__(self):
        self._bill_end = None
        self._bill_start = None
        self._tenant_bill_no = None
        self._user_bill_tax_details = None

    @property
    def bill_end(self):
        return self._bill_end

    @bill_end.setter
    def bill_end(self, value):
        self._bill_end = value
    @property
    def bill_start(self):
        return self._bill_start

    @bill_start.setter
    def bill_start(self, value):
        self._bill_start = value
    @property
    def tenant_bill_no(self):
        return self._tenant_bill_no

    @tenant_bill_no.setter
    def tenant_bill_no(self, value):
        self._tenant_bill_no = value
    @property
    def user_bill_tax_details(self):
        return self._user_bill_tax_details

    @user_bill_tax_details.setter
    def user_bill_tax_details(self, value):
        if isinstance(value, list):
            self._user_bill_tax_details = list()
            for i in value:
                if isinstance(i, UserBillTaxDetail):
                    self._user_bill_tax_details.append(i)
                else:
                    self._user_bill_tax_details.append(UserBillTaxDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.bill_end:
            if hasattr(self.bill_end, 'to_alipay_dict'):
                params['bill_end'] = self.bill_end.to_alipay_dict()
            else:
                params['bill_end'] = self.bill_end
        if self.bill_start:
            if hasattr(self.bill_start, 'to_alipay_dict'):
                params['bill_start'] = self.bill_start.to_alipay_dict()
            else:
                params['bill_start'] = self.bill_start
        if self.tenant_bill_no:
            if hasattr(self.tenant_bill_no, 'to_alipay_dict'):
                params['tenant_bill_no'] = self.tenant_bill_no.to_alipay_dict()
            else:
                params['tenant_bill_no'] = self.tenant_bill_no
        if self.user_bill_tax_details:
            if isinstance(self.user_bill_tax_details, list):
                for i in range(0, len(self.user_bill_tax_details)):
                    element = self.user_bill_tax_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_bill_tax_details[i] = element.to_alipay_dict()
            if hasattr(self.user_bill_tax_details, 'to_alipay_dict'):
                params['user_bill_tax_details'] = self.user_bill_tax_details.to_alipay_dict()
            else:
                params['user_bill_tax_details'] = self.user_bill_tax_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceBillTaxConfirmModel()
        if 'bill_end' in d:
            o.bill_end = d['bill_end']
        if 'bill_start' in d:
            o.bill_start = d['bill_start']
        if 'tenant_bill_no' in d:
            o.tenant_bill_no = d['tenant_bill_no']
        if 'user_bill_tax_details' in d:
            o.user_bill_tax_details = d['user_bill_tax_details']
        return o


