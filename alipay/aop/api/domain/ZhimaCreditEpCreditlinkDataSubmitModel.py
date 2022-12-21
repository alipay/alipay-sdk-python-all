#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCreditlinkDataSubmitModel(object):

    def __init__(self):
        self._data_content = None
        self._data_type = None
        self._merchant_request_id = None
        self._serial_no = None

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
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value


    def to_alipay_dict(self):
        params = dict()
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
        if 'data_content' in d:
            o.data_content = d['data_content']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'merchant_request_id' in d:
            o.merchant_request_id = d['merchant_request_id']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        return o


