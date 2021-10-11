#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceContent(object):

    def __init__(self):
        self._content_list = None
        self._device_sn = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                self._content_list.append(i)
    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_list:
            if isinstance(self.content_list, list):
                for i in range(0, len(self.content_list)):
                    element = self.content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_list[i] = element.to_alipay_dict()
            if hasattr(self.content_list, 'to_alipay_dict'):
                params['content_list'] = self.content_list.to_alipay_dict()
            else:
                params['content_list'] = self.content_list
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceContent()
        if 'content_list' in d:
            o.content_list = d['content_list']
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        return o


