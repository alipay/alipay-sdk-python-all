#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountDeviceInfoUploadModel(object):

    def __init__(self):
        self._call_back = None
        self._device_id = None
        self._device_type = None
        self._encrypt_type = None
        self._extra_info = None
        self._params = None
        self._request_from = None

    @property
    def call_back(self):
        return self._call_back

    @call_back.setter
    def call_back(self, value):
        self._call_back = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def extra_info(self):
        return self._extra_info

    @extra_info.setter
    def extra_info(self, value):
        self._extra_info = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_back:
            if hasattr(self.call_back, 'to_alipay_dict'):
                params['call_back'] = self.call_back.to_alipay_dict()
            else:
                params['call_back'] = self.call_back
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.extra_info:
            if hasattr(self.extra_info, 'to_alipay_dict'):
                params['extra_info'] = self.extra_info.to_alipay_dict()
            else:
                params['extra_info'] = self.extra_info
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAccountDeviceInfoUploadModel()
        if 'call_back' in d:
            o.call_back = d['call_back']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'extra_info' in d:
            o.extra_info = d['extra_info']
        if 'params' in d:
            o.params = d['params']
        if 'request_from' in d:
            o.request_from = d['request_from']
        return o


