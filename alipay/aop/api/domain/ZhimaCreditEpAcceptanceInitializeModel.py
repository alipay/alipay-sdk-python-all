#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAcceptanceInitializeModel(object):

    def __init__(self):
        self._device_type = None
        self._ep_cert_no = None
        self._ep_name = None
        self._merchant_return_url = None
        self._out_biz_no = None
        self._scene_code = None

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def merchant_return_url(self):
        return self._merchant_return_url

    @merchant_return_url.setter
    def merchant_return_url(self, value):
        self._merchant_return_url = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.merchant_return_url:
            if hasattr(self.merchant_return_url, 'to_alipay_dict'):
                params['merchant_return_url'] = self.merchant_return_url.to_alipay_dict()
            else:
                params['merchant_return_url'] = self.merchant_return_url
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAcceptanceInitializeModel()
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'merchant_return_url' in d:
            o.merchant_return_url = d['merchant_return_url']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


