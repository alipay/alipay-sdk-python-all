#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAccountDeviceInfoQueryModel(object):

    def __init__(self):
        self._device_ids = None
        self._device_type = None
        self._encrypt_type = None
        self._extra_info = None
        self._request_from = None

    @property
    def device_ids(self):
        return self._device_ids

    @device_ids.setter
    def device_ids(self, value):
        if isinstance(value, list):
            self._device_ids = list()
            for i in value:
                self._device_ids.append(i)
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
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_ids:
            if isinstance(self.device_ids, list):
                for i in range(0, len(self.device_ids)):
                    element = self.device_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.device_ids[i] = element.to_alipay_dict()
            if hasattr(self.device_ids, 'to_alipay_dict'):
                params['device_ids'] = self.device_ids.to_alipay_dict()
            else:
                params['device_ids'] = self.device_ids
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
        o = AlipayUserAccountDeviceInfoQueryModel()
        if 'device_ids' in d:
            o.device_ids = d['device_ids']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'extra_info' in d:
            o.extra_info = d['extra_info']
        if 'request_from' in d:
            o.request_from = d['request_from']
        return o


