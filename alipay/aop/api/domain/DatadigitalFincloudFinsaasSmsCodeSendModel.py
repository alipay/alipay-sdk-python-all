#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasSmsCodeSendModel(object):

    def __init__(self):
        self._phone_num_encrypt = None
        self._scene = None

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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasSmsCodeSendModel()
        if 'phone_num_encrypt' in d:
            o.phone_num_encrypt = d['phone_num_encrypt']
        if 'scene' in d:
            o.scene = d['scene']
        return o


