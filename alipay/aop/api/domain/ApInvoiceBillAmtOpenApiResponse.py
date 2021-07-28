#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApBillAmtOpenApiResponse import ApBillAmtOpenApiResponse


class ApInvoiceBillAmtOpenApiResponse(object):

    def __init__(self):
        self._ap_bill_amt_list = None
        self._invoice_id = None

    @property
    def ap_bill_amt_list(self):
        return self._ap_bill_amt_list

    @ap_bill_amt_list.setter
    def ap_bill_amt_list(self, value):
        if isinstance(value, list):
            self._ap_bill_amt_list = list()
            for i in value:
                if isinstance(i, ApBillAmtOpenApiResponse):
                    self._ap_bill_amt_list.append(i)
                else:
                    self._ap_bill_amt_list.append(ApBillAmtOpenApiResponse.from_alipay_dict(i))
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ap_bill_amt_list:
            if isinstance(self.ap_bill_amt_list, list):
                for i in range(0, len(self.ap_bill_amt_list)):
                    element = self.ap_bill_amt_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ap_bill_amt_list[i] = element.to_alipay_dict()
            if hasattr(self.ap_bill_amt_list, 'to_alipay_dict'):
                params['ap_bill_amt_list'] = self.ap_bill_amt_list.to_alipay_dict()
            else:
                params['ap_bill_amt_list'] = self.ap_bill_amt_list
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApInvoiceBillAmtOpenApiResponse()
        if 'ap_bill_amt_list' in d:
            o.ap_bill_amt_list = d['ap_bill_amt_list']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        return o


