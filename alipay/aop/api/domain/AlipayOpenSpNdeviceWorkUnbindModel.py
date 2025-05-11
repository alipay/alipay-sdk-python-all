#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpNdeviceWorkUnbindModel(object):

    def __init__(self):
        self._device_sn = None
        self._device_type = None
        self._open_id = None
        self._out_biz_id = None
        self._related_device_sn = None
        self._user_id = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def related_device_sn(self):
        return self._related_device_sn

    @related_device_sn.setter
    def related_device_sn(self, value):
        self._related_device_sn = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.related_device_sn:
            if hasattr(self.related_device_sn, 'to_alipay_dict'):
                params['related_device_sn'] = self.related_device_sn.to_alipay_dict()
            else:
                params['related_device_sn'] = self.related_device_sn
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNdeviceWorkUnbindModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'related_device_sn' in d:
            o.related_device_sn = d['related_device_sn']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


