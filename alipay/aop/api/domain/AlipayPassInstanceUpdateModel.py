#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPassInstanceUpdateModel(object):

    def __init__(self):
        self._channel_id = None
        self._serial_number = None
        self._status = None
        self._tpl_params = None
        self._user_id = None
        self._verify_code = None
        self._verify_type = None

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tpl_params(self):
        return self._tpl_params

    @tpl_params.setter
    def tpl_params(self, value):
        self._tpl_params = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, value):
        self._verify_code = value
    @property
    def verify_type(self):
        return self._verify_type

    @verify_type.setter
    def verify_type(self, value):
        self._verify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tpl_params:
            if hasattr(self.tpl_params, 'to_alipay_dict'):
                params['tpl_params'] = self.tpl_params.to_alipay_dict()
            else:
                params['tpl_params'] = self.tpl_params
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.verify_code:
            if hasattr(self.verify_code, 'to_alipay_dict'):
                params['verify_code'] = self.verify_code.to_alipay_dict()
            else:
                params['verify_code'] = self.verify_code
        if self.verify_type:
            if hasattr(self.verify_type, 'to_alipay_dict'):
                params['verify_type'] = self.verify_type.to_alipay_dict()
            else:
                params['verify_type'] = self.verify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPassInstanceUpdateModel()
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        if 'status' in d:
            o.status = d['status']
        if 'tpl_params' in d:
            o.tpl_params = d['tpl_params']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'verify_code' in d:
            o.verify_code = d['verify_code']
        if 'verify_type' in d:
            o.verify_type = d['verify_type']
        return o


