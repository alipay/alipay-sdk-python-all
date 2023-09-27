#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceSpecificsDTO import InvoiceSpecificsDTO


class AlipayBossFncGfsmartpayInvoiceserviceCreateModel(object):

    def __init__(self):
        self._entry_by = None
        self._invoice_specifics_dtos = None
        self._is_batch = None
        self._test_mode = None

    @property
    def entry_by(self):
        return self._entry_by

    @entry_by.setter
    def entry_by(self, value):
        self._entry_by = value
    @property
    def invoice_specifics_dtos(self):
        return self._invoice_specifics_dtos

    @invoice_specifics_dtos.setter
    def invoice_specifics_dtos(self, value):
        if isinstance(value, list):
            self._invoice_specifics_dtos = list()
            for i in value:
                if isinstance(i, InvoiceSpecificsDTO):
                    self._invoice_specifics_dtos.append(i)
                else:
                    self._invoice_specifics_dtos.append(InvoiceSpecificsDTO.from_alipay_dict(i))
    @property
    def is_batch(self):
        return self._is_batch

    @is_batch.setter
    def is_batch(self, value):
        self._is_batch = value
    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, value):
        self._test_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.entry_by:
            if hasattr(self.entry_by, 'to_alipay_dict'):
                params['entry_by'] = self.entry_by.to_alipay_dict()
            else:
                params['entry_by'] = self.entry_by
        if self.invoice_specifics_dtos:
            if isinstance(self.invoice_specifics_dtos, list):
                for i in range(0, len(self.invoice_specifics_dtos)):
                    element = self.invoice_specifics_dtos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_specifics_dtos[i] = element.to_alipay_dict()
            if hasattr(self.invoice_specifics_dtos, 'to_alipay_dict'):
                params['invoice_specifics_dtos'] = self.invoice_specifics_dtos.to_alipay_dict()
            else:
                params['invoice_specifics_dtos'] = self.invoice_specifics_dtos
        if self.is_batch:
            if hasattr(self.is_batch, 'to_alipay_dict'):
                params['is_batch'] = self.is_batch.to_alipay_dict()
            else:
                params['is_batch'] = self.is_batch
        if self.test_mode:
            if hasattr(self.test_mode, 'to_alipay_dict'):
                params['test_mode'] = self.test_mode.to_alipay_dict()
            else:
                params['test_mode'] = self.test_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsmartpayInvoiceserviceCreateModel()
        if 'entry_by' in d:
            o.entry_by = d['entry_by']
        if 'invoice_specifics_dtos' in d:
            o.invoice_specifics_dtos = d['invoice_specifics_dtos']
        if 'is_batch' in d:
            o.is_batch = d['is_batch']
        if 'test_mode' in d:
            o.test_mode = d['test_mode']
        return o


