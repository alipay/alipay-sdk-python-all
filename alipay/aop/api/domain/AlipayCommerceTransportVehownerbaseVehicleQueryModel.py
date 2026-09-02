#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportVehownerbaseVehicleQueryModel(object):

    def __init__(self):
        self._open_id = None
        self._scene = None
        self._user_id = None
        self._vi_id = None
        self._vi_number = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vi_id(self):
        return self._vi_id

    @vi_id.setter
    def vi_id(self, value):
        self._vi_id = value
    @property
    def vi_number(self):
        return self._vi_number

    @vi_number.setter
    def vi_number(self, value):
        self._vi_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vi_id:
            if hasattr(self.vi_id, 'to_alipay_dict'):
                params['vi_id'] = self.vi_id.to_alipay_dict()
            else:
                params['vi_id'] = self.vi_id
        if self.vi_number:
            if hasattr(self.vi_number, 'to_alipay_dict'):
                params['vi_number'] = self.vi_number.to_alipay_dict()
            else:
                params['vi_number'] = self.vi_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportVehownerbaseVehicleQueryModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vi_id' in d:
            o.vi_id = d['vi_id']
        if 'vi_number' in d:
            o.vi_number = d['vi_number']
        return o


