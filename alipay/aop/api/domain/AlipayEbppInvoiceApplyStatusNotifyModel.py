#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceUkDTO import InvoiceUkDTO


class AlipayEbppInvoiceApplyStatusNotifyModel(object):

    def __init__(self):
        self._apply_id = None
        self._apply_status = None
        self._invoice_uks = None
        self._message = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def invoice_uks(self):
        return self._invoice_uks

    @invoice_uks.setter
    def invoice_uks(self, value):
        if isinstance(value, list):
            self._invoice_uks = list()
            for i in value:
                if isinstance(i, InvoiceUkDTO):
                    self._invoice_uks.append(i)
                else:
                    self._invoice_uks.append(InvoiceUkDTO.from_alipay_dict(i))
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.invoice_uks:
            if isinstance(self.invoice_uks, list):
                for i in range(0, len(self.invoice_uks)):
                    element = self.invoice_uks[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_uks[i] = element.to_alipay_dict()
            if hasattr(self.invoice_uks, 'to_alipay_dict'):
                params['invoice_uks'] = self.invoice_uks.to_alipay_dict()
            else:
                params['invoice_uks'] = self.invoice_uks
        if self.message:
            if hasattr(self.message, 'to_alipay_dict'):
                params['message'] = self.message.to_alipay_dict()
            else:
                params['message'] = self.message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceApplyStatusNotifyModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'invoice_uks' in d:
            o.invoice_uks = d['invoice_uks']
        if 'message' in d:
            o.message = d['message']
        return o


