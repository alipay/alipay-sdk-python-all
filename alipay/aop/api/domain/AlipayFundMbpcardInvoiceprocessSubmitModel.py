#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceBaseInfo import InvoiceBaseInfo


class AlipayFundMbpcardInvoiceprocessSubmitModel(object):

    def __init__(self):
        self._biz_scene = None
        self._invoice_list = None
        self._merchant_id = None
        self._out_biz_no = None
        self._product_code = None
        self._task_id_list = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def invoice_list(self):
        return self._invoice_list

    @invoice_list.setter
    def invoice_list(self, value):
        if isinstance(value, list):
            self._invoice_list = list()
            for i in value:
                if isinstance(i, InvoiceBaseInfo):
                    self._invoice_list.append(i)
                else:
                    self._invoice_list.append(InvoiceBaseInfo.from_alipay_dict(i))
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def task_id_list(self):
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, value):
        if isinstance(value, list):
            self._task_id_list = list()
            for i in value:
                self._task_id_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.invoice_list:
            if isinstance(self.invoice_list, list):
                for i in range(0, len(self.invoice_list)):
                    element = self.invoice_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_list, 'to_alipay_dict'):
                params['invoice_list'] = self.invoice_list.to_alipay_dict()
            else:
                params['invoice_list'] = self.invoice_list
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.task_id_list:
            if isinstance(self.task_id_list, list):
                for i in range(0, len(self.task_id_list)):
                    element = self.task_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.task_id_list[i] = element.to_alipay_dict()
            if hasattr(self.task_id_list, 'to_alipay_dict'):
                params['task_id_list'] = self.task_id_list.to_alipay_dict()
            else:
                params['task_id_list'] = self.task_id_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFundMbpcardInvoiceprocessSubmitModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'invoice_list' in d:
            o.invoice_list = d['invoice_list']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'task_id_list' in d:
            o.task_id_list = d['task_id_list']
        return o


