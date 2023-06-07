#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OutputInvoiceRedApplyVO import OutputInvoiceRedApplyVO


class AlipayBossFncOutputinvoiceRedinvoiceApplyModel(object):

    def __init__(self):
        self._output_invoice_red_apply = None

    @property
    def output_invoice_red_apply(self):
        return self._output_invoice_red_apply

    @output_invoice_red_apply.setter
    def output_invoice_red_apply(self, value):
        if isinstance(value, OutputInvoiceRedApplyVO):
            self._output_invoice_red_apply = value
        else:
            self._output_invoice_red_apply = OutputInvoiceRedApplyVO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.output_invoice_red_apply:
            if hasattr(self.output_invoice_red_apply, 'to_alipay_dict'):
                params['output_invoice_red_apply'] = self.output_invoice_red_apply.to_alipay_dict()
            else:
                params['output_invoice_red_apply'] = self.output_invoice_red_apply
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncOutputinvoiceRedinvoiceApplyModel()
        if 'output_invoice_red_apply' in d:
            o.output_invoice_red_apply = d['output_invoice_red_apply']
        return o


