#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZolozIdentificationCustomerSmilerepoSyncModel(object):

    def __init__(self):
        self._auth_img = None
        self._device_num = None
        self._scene_code = None
        self._zface_info = None

    @property
    def auth_img(self):
        return self._auth_img

    @auth_img.setter
    def auth_img(self, value):
        self._auth_img = value
    @property
    def device_num(self):
        return self._device_num

    @device_num.setter
    def device_num(self, value):
        self._device_num = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def zface_info(self):
        return self._zface_info

    @zface_info.setter
    def zface_info(self, value):
        self._zface_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_img:
            if hasattr(self.auth_img, 'to_alipay_dict'):
                params['auth_img'] = self.auth_img.to_alipay_dict()
            else:
                params['auth_img'] = self.auth_img
        if self.device_num:
            if hasattr(self.device_num, 'to_alipay_dict'):
                params['device_num'] = self.device_num.to_alipay_dict()
            else:
                params['device_num'] = self.device_num
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.zface_info:
            if hasattr(self.zface_info, 'to_alipay_dict'):
                params['zface_info'] = self.zface_info.to_alipay_dict()
            else:
                params['zface_info'] = self.zface_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZolozIdentificationCustomerSmilerepoSyncModel()
        if 'auth_img' in d:
            o.auth_img = d['auth_img']
        if 'device_num' in d:
            o.device_num = d['device_num']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'zface_info' in d:
            o.zface_info = d['zface_info']
        return o


