#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceArrivalDetailDTO import InvoiceArrivalDetailDTO


class InvoiceArrivalDTO(object):

    def __init__(self):
        self._invoice_arrival_detail_dtos = None
        self._invoice_bill_id = None
        self._invoice_bill_no = None
        self._use_amount = None
        self._wht_amount = None
        self._wht_rate = None

    @property
    def invoice_arrival_detail_dtos(self):
        return self._invoice_arrival_detail_dtos

    @invoice_arrival_detail_dtos.setter
    def invoice_arrival_detail_dtos(self, value):
        if isinstance(value, list):
            self._invoice_arrival_detail_dtos = list()
            for i in value:
                if isinstance(i, InvoiceArrivalDetailDTO):
                    self._invoice_arrival_detail_dtos.append(i)
                else:
                    self._invoice_arrival_detail_dtos.append(InvoiceArrivalDetailDTO.from_alipay_dict(i))
    @property
    def invoice_bill_id(self):
        return self._invoice_bill_id

    @invoice_bill_id.setter
    def invoice_bill_id(self, value):
        self._invoice_bill_id = value
    @property
    def invoice_bill_no(self):
        return self._invoice_bill_no

    @invoice_bill_no.setter
    def invoice_bill_no(self, value):
        self._invoice_bill_no = value
    @property
    def use_amount(self):
        return self._use_amount

    @use_amount.setter
    def use_amount(self, value):
        self._use_amount = value
    @property
    def wht_amount(self):
        return self._wht_amount

    @wht_amount.setter
    def wht_amount(self, value):
        self._wht_amount = value
    @property
    def wht_rate(self):
        return self._wht_rate

    @wht_rate.setter
    def wht_rate(self, value):
        self._wht_rate = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_arrival_detail_dtos:
            if isinstance(self.invoice_arrival_detail_dtos, list):
                for i in range(0, len(self.invoice_arrival_detail_dtos)):
                    element = self.invoice_arrival_detail_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_arrival_detail_dtos[i] = element.to_alipay_dict()
            if hasattr(self.invoice_arrival_detail_dtos, 'to_alipay_dict'):
                params['invoice_arrival_detail_dtos'] = self.invoice_arrival_detail_dtos.to_alipay_dict()
            else:
                params['invoice_arrival_detail_dtos'] = self.invoice_arrival_detail_dtos
        if self.invoice_bill_id:
            if hasattr(self.invoice_bill_id, 'to_alipay_dict'):
                params['invoice_bill_id'] = self.invoice_bill_id.to_alipay_dict()
            else:
                params['invoice_bill_id'] = self.invoice_bill_id
        if self.invoice_bill_no:
            if hasattr(self.invoice_bill_no, 'to_alipay_dict'):
                params['invoice_bill_no'] = self.invoice_bill_no.to_alipay_dict()
            else:
                params['invoice_bill_no'] = self.invoice_bill_no
        if self.use_amount:
            if hasattr(self.use_amount, 'to_alipay_dict'):
                params['use_amount'] = self.use_amount.to_alipay_dict()
            else:
                params['use_amount'] = self.use_amount
        if self.wht_amount:
            if hasattr(self.wht_amount, 'to_alipay_dict'):
                params['wht_amount'] = self.wht_amount.to_alipay_dict()
            else:
                params['wht_amount'] = self.wht_amount
        if self.wht_rate:
            if hasattr(self.wht_rate, 'to_alipay_dict'):
                params['wht_rate'] = self.wht_rate.to_alipay_dict()
            else:
                params['wht_rate'] = self.wht_rate
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceArrivalDTO()
        if 'invoice_arrival_detail_dtos' in d:
            o.invoice_arrival_detail_dtos = d['invoice_arrival_detail_dtos']
        if 'invoice_bill_id' in d:
            o.invoice_bill_id = d['invoice_bill_id']
        if 'invoice_bill_no' in d:
            o.invoice_bill_no = d['invoice_bill_no']
        if 'use_amount' in d:
            o.use_amount = d['use_amount']
        if 'wht_amount' in d:
            o.wht_amount = d['wht_amount']
        if 'wht_rate' in d:
            o.wht_rate = d['wht_rate']
        return o


