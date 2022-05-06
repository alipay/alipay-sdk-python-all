#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudGeneralsaasFaceFeeChargeModel(object):

    def __init__(self):
        self._certify_no = None
        self._merchant_id = None
        self._product_code = None
        self._scene_code = None
        self._service_time = None

    @property
    def certify_no(self):
        return self._certify_no

    @certify_no.setter
    def certify_no(self, value):
        self._certify_no = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_time(self):
        return self._service_time

    @service_time.setter
    def service_time(self, value):
        self._service_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.certify_no:
            if hasattr(self.certify_no, 'to_alipay_dict'):
                params['certify_no'] = self.certify_no.to_alipay_dict()
            else:
                params['certify_no'] = self.certify_no
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_time:
            if hasattr(self.service_time, 'to_alipay_dict'):
                params['service_time'] = self.service_time.to_alipay_dict()
            else:
                params['service_time'] = self.service_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudGeneralsaasFaceFeeChargeModel()
        if 'certify_no' in d:
            o.certify_no = d['certify_no']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_time' in d:
            o.service_time = d['service_time']
        return o


