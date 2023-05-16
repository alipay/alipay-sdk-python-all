#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCreditlinkDataSubmitModel(object):

    def __init__(self):
        self._collect_id = None
        self._consumer_merchant_no = None
        self._data_content = None
        self._data_type = None
        self._merchant_request_id = None
        self._product_code = None
        self._serial_no = None

    @property
    def collect_id(self):
        return self._collect_id

    @collect_id.setter
    def collect_id(self, value):
        self._collect_id = value
    @property
    def consumer_merchant_no(self):
        return self._consumer_merchant_no

    @consumer_merchant_no.setter
    def consumer_merchant_no(self, value):
        self._consumer_merchant_no = value
    @property
    def data_content(self):
        return self._data_content

    @data_content.setter
    def data_content(self, value):
        self._data_content = value
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.collect_id:
            if hasattr(self.collect_id, 'to_alipay_dict'):
                params['collect_id'] = self.collect_id.to_alipay_dict()
            else:
                params['collect_id'] = self.collect_id
        if self.consumer_merchant_no:
            if hasattr(self.consumer_merchant_no, 'to_alipay_dict'):
                params['consumer_merchant_no'] = self.consumer_merchant_no.to_alipay_dict()
            else:
                params['consumer_merchant_no'] = self.consumer_merchant_no
        if self.data_content:
            if hasattr(self.data_content, 'to_alipay_dict'):
                params['data_content'] = self.data_content.to_alipay_dict()
            else:
                params['data_content'] = self.data_content
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.merchant_request_id:
            if hasattr(self.merchant_request_id, 'to_alipay_dict'):
                params['merchant_request_id'] = self.merchant_request_id.to_alipay_dict()
            else:
                params['merchant_request_id'] = self.merchant_request_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditlinkDataSubmitModel()
        if 'collect_id' in d:
            o.collect_id = d['collect_id']
        if 'consumer_merchant_no' in d:
            o.consumer_merchant_no = d['consumer_merchant_no']
        if 'data_content' in d:
            o.data_content = d['data_content']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'merchant_request_id' in d:
            o.merchant_request_id = d['merchant_request_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


