#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAmpeMobileappBindModel(object):

    def __init__(self):
        self._app_sign = None
        self._mobile_app_id = None
        self._product_id_list = None
        self._scene_code = None

    @property
    def app_sign(self):
        return self._app_sign

    @app_sign.setter
    def app_sign(self, value):
        self._app_sign = value
    @property
    def mobile_app_id(self):
        return self._mobile_app_id

    @mobile_app_id.setter
    def mobile_app_id(self, value):
        self._mobile_app_id = value
    @property
    def product_id_list(self):
        return self._product_id_list

    @product_id_list.setter
    def product_id_list(self, value):
        if isinstance(value, list):
            self._product_id_list = list()
            for i in value:
                self._product_id_list.append(i)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_sign:
            if hasattr(self.app_sign, 'to_alipay_dict'):
                params['app_sign'] = self.app_sign.to_alipay_dict()
            else:
                params['app_sign'] = self.app_sign
        if self.mobile_app_id:
            if hasattr(self.mobile_app_id, 'to_alipay_dict'):
                params['mobile_app_id'] = self.mobile_app_id.to_alipay_dict()
            else:
                params['mobile_app_id'] = self.mobile_app_id
        if self.product_id_list:
            if isinstance(self.product_id_list, list):
                for i in range(0, len(self.product_id_list)):
                    element = self.product_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_id_list[i] = element.to_alipay_dict()
            if hasattr(self.product_id_list, 'to_alipay_dict'):
                params['product_id_list'] = self.product_id_list.to_alipay_dict()
            else:
                params['product_id_list'] = self.product_id_list
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeMobileappBindModel()
        if 'app_sign' in d:
            o.app_sign = d['app_sign']
        if 'mobile_app_id' in d:
            o.mobile_app_id = d['mobile_app_id']
        if 'product_id_list' in d:
            o.product_id_list = d['product_id_list']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


