#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseVerificationcodeVerifyModel(object):

    def __init__(self):
        self._code = None
        self._invalid = None
        self._passport_id = None
        self._scene = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def invalid(self):
        return self._invalid

    @invalid.setter
    def invalid(self, value):
        self._invalid = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.invalid:
            if hasattr(self.invalid, 'to_alipay_dict'):
                params['invalid'] = self.invalid.to_alipay_dict()
            else:
                params['invalid'] = self.invalid
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
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
        o = AnttechOceanbaseVerificationcodeVerifyModel()
        if 'code' in d:
            o.code = d['code']
        if 'invalid' in d:
            o.invalid = d['invalid']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'scene' in d:
            o.scene = d['scene']
        return o


