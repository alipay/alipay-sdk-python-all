#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NOrderTagBindResp import NOrderTagBindResp


class AlipayOpenSpNorderdevicePositionBindModel(object):

    def __init__(self):
        self._device_sn = None
        self._ext_param = None
        self._operate = None
        self._operator_id = None
        self._operator_name = None
        self._operator_phone = None
        self._operator_time = None
        self._position_id = None
        self._user_open_id = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        if isinstance(value, NOrderTagBindResp):
            self._ext_param = value
        else:
            self._ext_param = NOrderTagBindResp.from_alipay_dict(value)
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def operator_phone(self):
        return self._operator_phone

    @operator_phone.setter
    def operator_phone(self, value):
        self._operator_phone = value
    @property
    def operator_time(self):
        return self._operator_time

    @operator_time.setter
    def operator_time(self, value):
        self._operator_time = value
    @property
    def position_id(self):
        return self._position_id

    @position_id.setter
    def position_id(self, value):
        self._position_id = value
    @property
    def user_open_id(self):
        return self._user_open_id

    @user_open_id.setter
    def user_open_id(self, value):
        self._user_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.operator_phone:
            if hasattr(self.operator_phone, 'to_alipay_dict'):
                params['operator_phone'] = self.operator_phone.to_alipay_dict()
            else:
                params['operator_phone'] = self.operator_phone
        if self.operator_time:
            if hasattr(self.operator_time, 'to_alipay_dict'):
                params['operator_time'] = self.operator_time.to_alipay_dict()
            else:
                params['operator_time'] = self.operator_time
        if self.position_id:
            if hasattr(self.position_id, 'to_alipay_dict'):
                params['position_id'] = self.position_id.to_alipay_dict()
            else:
                params['position_id'] = self.position_id
        if self.user_open_id:
            if hasattr(self.user_open_id, 'to_alipay_dict'):
                params['user_open_id'] = self.user_open_id.to_alipay_dict()
            else:
                params['user_open_id'] = self.user_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpNorderdevicePositionBindModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'operate' in d:
            o.operate = d['operate']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'operator_phone' in d:
            o.operator_phone = d['operator_phone']
        if 'operator_time' in d:
            o.operator_time = d['operator_time']
        if 'position_id' in d:
            o.position_id = d['position_id']
        if 'user_open_id' in d:
            o.user_open_id = d['user_open_id']
        return o


