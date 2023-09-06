#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InputInvoiceQueryByIdsOpenApiDTO(object):

    def __init__(self):
        self._invoice_ids = None

    @property
    def invoice_ids(self):
        return self._invoice_ids

    @invoice_ids.setter
    def invoice_ids(self, value):
        if isinstance(value, list):
            self._invoice_ids = list()
            for i in value:
                self._invoice_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_ids:
            if isinstance(self.invoice_ids, list):
                for i in range(0, len(self.invoice_ids)):
                    element = self.invoice_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_ids[i] = element.to_alipay_dict()
            if hasattr(self.invoice_ids, 'to_alipay_dict'):
                params['invoice_ids'] = self.invoice_ids.to_alipay_dict()
            else:
                params['invoice_ids'] = self.invoice_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InputInvoiceQueryByIdsOpenApiDTO()
        if 'invoice_ids' in d:
            o.invoice_ids = d['invoice_ids']
        return o


