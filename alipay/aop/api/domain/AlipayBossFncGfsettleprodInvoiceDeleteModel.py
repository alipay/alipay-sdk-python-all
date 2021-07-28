#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceOperateParam import InvoiceOperateParam


class AlipayBossFncGfsettleprodInvoiceDeleteModel(object):

    def __init__(self):
        self._invoice_operate_param = None

    @property
    def invoice_operate_param(self):
        return self._invoice_operate_param

    @invoice_operate_param.setter
    def invoice_operate_param(self, value):
        if isinstance(value, InvoiceOperateParam):
            self._invoice_operate_param = value
        else:
            self._invoice_operate_param = InvoiceOperateParam.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_operate_param:
            if hasattr(self.invoice_operate_param, 'to_alipay_dict'):
                params['invoice_operate_param'] = self.invoice_operate_param.to_alipay_dict()
            else:
                params['invoice_operate_param'] = self.invoice_operate_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodInvoiceDeleteModel()
        if 'invoice_operate_param' in d:
            o.invoice_operate_param = d['invoice_operate_param']
        return o


