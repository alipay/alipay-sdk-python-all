#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneInshealthserviceprodMallskustatusModifyModel(object):

    def __init__(self):
        self._merchant_sku_code = None
        self._ser_prod_no = None
        self._source_product_id = None
        self._status = None

    @property
    def merchant_sku_code(self):
        return self._merchant_sku_code

    @merchant_sku_code.setter
    def merchant_sku_code(self, value):
        self._merchant_sku_code = value
    @property
    def ser_prod_no(self):
        return self._ser_prod_no

    @ser_prod_no.setter
    def ser_prod_no(self, value):
        self._ser_prod_no = value
    @property
    def source_product_id(self):
        return self._source_product_id

    @source_product_id.setter
    def source_product_id(self, value):
        self._source_product_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_sku_code:
            if hasattr(self.merchant_sku_code, 'to_alipay_dict'):
                params['merchant_sku_code'] = self.merchant_sku_code.to_alipay_dict()
            else:
                params['merchant_sku_code'] = self.merchant_sku_code
        if self.ser_prod_no:
            if hasattr(self.ser_prod_no, 'to_alipay_dict'):
                params['ser_prod_no'] = self.ser_prod_no.to_alipay_dict()
            else:
                params['ser_prod_no'] = self.ser_prod_no
        if self.source_product_id:
            if hasattr(self.source_product_id, 'to_alipay_dict'):
                params['source_product_id'] = self.source_product_id.to_alipay_dict()
            else:
                params['source_product_id'] = self.source_product_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneInshealthserviceprodMallskustatusModifyModel()
        if 'merchant_sku_code' in d:
            o.merchant_sku_code = d['merchant_sku_code']
        if 'ser_prod_no' in d:
            o.ser_prod_no = d['ser_prod_no']
        if 'source_product_id' in d:
            o.source_product_id = d['source_product_id']
        if 'status' in d:
            o.status = d['status']
        return o


