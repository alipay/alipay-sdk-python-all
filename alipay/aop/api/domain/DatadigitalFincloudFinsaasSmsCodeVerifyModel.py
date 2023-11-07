#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasSmsCodeVerifyModel(object):

    def __init__(self):
        self._phone_num_encrypt = None
        self._scene = None
        self._sms_code = None

    @property
    def phone_num_encrypt(self):
        return self._phone_num_encrypt

    @phone_num_encrypt.setter
    def phone_num_encrypt(self, value):
        self._phone_num_encrypt = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone_num_encrypt:
            if hasattr(self.phone_num_encrypt, 'to_alipay_dict'):
                params['phone_num_encrypt'] = self.phone_num_encrypt.to_alipay_dict()
            else:
                params['phone_num_encrypt'] = self.phone_num_encrypt
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sms_code:
            if hasattr(self.sms_code, 'to_alipay_dict'):
                params['sms_code'] = self.sms_code.to_alipay_dict()
            else:
                params['sms_code'] = self.sms_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasSmsCodeVerifyModel()
        if 'phone_num_encrypt' in d:
            o.phone_num_encrypt = d['phone_num_encrypt']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sms_code' in d:
            o.sms_code = d['sms_code']
        return o


