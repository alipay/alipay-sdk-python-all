#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiOutputInvoiceVO import OpenApiOutputInvoiceVO


class OpenApiInvoiceMixInfoVO(object):

    def __init__(self):
        self._output_invoices = None
        self._preview_order_id = None

    @property
    def output_invoices(self):
        return self._output_invoices

    @output_invoices.setter
    def output_invoices(self, value):
        if isinstance(value, list):
            self._output_invoices = list()
            for i in value:
                if isinstance(i, OpenApiOutputInvoiceVO):
                    self._output_invoices.append(i)
                else:
                    self._output_invoices.append(OpenApiOutputInvoiceVO.from_alipay_dict(i))
    @property
    def preview_order_id(self):
        return self._preview_order_id

    @preview_order_id.setter
    def preview_order_id(self, value):
        self._preview_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.output_invoices:
            if isinstance(self.output_invoices, list):
                for i in range(0, len(self.output_invoices)):
                    element = self.output_invoices[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.output_invoices[i] = element.to_alipay_dict()
            if hasattr(self.output_invoices, 'to_alipay_dict'):
                params['output_invoices'] = self.output_invoices.to_alipay_dict()
            else:
                params['output_invoices'] = self.output_invoices
        if self.preview_order_id:
            if hasattr(self.preview_order_id, 'to_alipay_dict'):
                params['preview_order_id'] = self.preview_order_id.to_alipay_dict()
            else:
                params['preview_order_id'] = self.preview_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiInvoiceMixInfoVO()
        if 'output_invoices' in d:
            o.output_invoices = d['output_invoices']
        if 'preview_order_id' in d:
            o.preview_order_id = d['preview_order_id']
        return o


