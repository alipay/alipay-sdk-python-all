#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppPocketmoneyPromoConsultModel(object):

    def __init__(self):
        self._biz_no = None
        self._device_id = None
        self._extra_device_id = None
        self._os_type = None
        self._red_packet_flag = None
        self._solution_vendor = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
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
    def red_packet_flag(self):
        return self._red_packet_flag

    @red_packet_flag.setter
    def red_packet_flag(self, value):
        self._red_packet_flag = value
    @property
    def solution_vendor(self):
        return self._solution_vendor

    @solution_vendor.setter
    def solution_vendor(self, value):
        self._solution_vendor = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
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
        if self.red_packet_flag:
            if hasattr(self.red_packet_flag, 'to_alipay_dict'):
                params['red_packet_flag'] = self.red_packet_flag.to_alipay_dict()
            else:
                params['red_packet_flag'] = self.red_packet_flag
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
        o = AlipayPayAppPocketmoneyPromoConsultModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'extra_device_id' in d:
            o.extra_device_id = d['extra_device_id']
        if 'os_type' in d:
            o.os_type = d['os_type']
        if 'red_packet_flag' in d:
            o.red_packet_flag = d['red_packet_flag']
        if 'solution_vendor' in d:
            o.solution_vendor = d['solution_vendor']
        return o


