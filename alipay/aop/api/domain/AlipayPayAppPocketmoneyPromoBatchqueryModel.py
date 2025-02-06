#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppPocketmoneyPromoBatchqueryModel(object):

    def __init__(self):
        self._biz_no_list = None
        self._device_id = None
        self._extra_device_id = None
        self._os_type = None
        self._solution_vendor = None

    @property
    def biz_no_list(self):
        return self._biz_no_list

    @biz_no_list.setter
    def biz_no_list(self, value):
        if isinstance(value, list):
            self._biz_no_list = list()
            for i in value:
                self._biz_no_list.append(i)
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def extra_device_id(self):
        return self._extra_device_id

    @extra_device_id.setter
    def extra_device_id(self, value):
        self._extra_device_id = value
    @property
    def os_type(self):
        return self._os_type

    @os_type.setter
    def os_type(self, value):
        self._os_type = value
    @property
    def solution_vendor(self):
        return self._solution_vendor

    @solution_vendor.setter
    def solution_vendor(self, value):
        self._solution_vendor = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no_list:
            if isinstance(self.biz_no_list, list):
                for i in range(0, len(self.biz_no_list)):
                    element = self.biz_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_no_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_no_list, 'to_alipay_dict'):
                params['biz_no_list'] = self.biz_no_list.to_alipay_dict()
            else:
                params['biz_no_list'] = self.biz_no_list
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.extra_device_id:
            if hasattr(self.extra_device_id, 'to_alipay_dict'):
                params['extra_device_id'] = self.extra_device_id.to_alipay_dict()
            else:
                params['extra_device_id'] = self.extra_device_id
        if self.os_type:
            if hasattr(self.os_type, 'to_alipay_dict'):
                params['os_type'] = self.os_type.to_alipay_dict()
            else:
                params['os_type'] = self.os_type
        if self.solution_vendor:
            if hasattr(self.solution_vendor, 'to_alipay_dict'):
                params['solution_vendor'] = self.solution_vendor.to_alipay_dict()
            else:
                params['solution_vendor'] = self.solution_vendor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppPocketmoneyPromoBatchqueryModel()
        if 'biz_no_list' in d:
            o.biz_no_list = d['biz_no_list']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'extra_device_id' in d:
            o.extra_device_id = d['extra_device_id']
        if 'os_type' in d:
            o.os_type = d['os_type']
        if 'solution_vendor' in d:
            o.solution_vendor = d['solution_vendor']
        return o


