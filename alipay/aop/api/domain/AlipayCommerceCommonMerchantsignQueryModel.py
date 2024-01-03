#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCommonMerchantsignQueryModel(object):

    def __init__(self):
        self._scene = None
        self._sign_pid = None

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sign_pid(self):
        return self._sign_pid

    @sign_pid.setter
    def sign_pid(self, value):
        self._sign_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sign_pid:
            if hasattr(self.sign_pid, 'to_alipay_dict'):
                params['sign_pid'] = self.sign_pid.to_alipay_dict()
            else:
                params['sign_pid'] = self.sign_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCommonMerchantsignQueryModel()
        if 'scene' in d:
            o.scene = d['scene']
        if 'sign_pid' in d:
            o.sign_pid = d['sign_pid']
        return o


