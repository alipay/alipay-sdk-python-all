#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.InvoiceAllResponseDTO import InvoiceAllResponseDTO


class BillInvoiceResponseDTO(object):

    def __init__(self):
        self._bill_relate_amount = None
        self._invoice = None

    @property
    def bill_relate_amount(self):
        return self._bill_relate_amount

    @bill_relate_amount.setter
    def bill_relate_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._bill_relate_amount = value
        else:
            self._bill_relate_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def invoice(self):
        return self._invoice

    @invoice.setter
    def invoice(self, value):
        if isinstance(value, InvoiceAllResponseDTO):
            self._invoice = value
        else:
            self._invoice = InvoiceAllResponseDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_relate_amount:
            if hasattr(self.bill_relate_amount, 'to_alipay_dict'):
                params['bill_relate_amount'] = self.bill_relate_amount.to_alipay_dict()
            else:
                params['bill_relate_amount'] = self.bill_relate_amount
        if self.invoice:
            if hasattr(self.invoice, 'to_alipay_dict'):
                params['invoice'] = self.invoice.to_alipay_dict()
            else:
                params['invoice'] = self.invoice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillInvoiceResponseDTO()
        if 'bill_relate_amount' in d:
            o.bill_relate_amount = d['bill_relate_amount']
        if 'invoice' in d:
            o.invoice = d['invoice']
        return o


