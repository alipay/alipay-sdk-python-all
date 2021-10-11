#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAmpeUsersceneModifyModel(object):

    def __init__(self):
        self._device_id = None
        self._disable_scene_id_list = None
        self._enable_scene_id_list = None
        self._product_id = None
        self._user_key = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def disable_scene_id_list(self):
        return self._disable_scene_id_list

    @disable_scene_id_list.setter
    def disable_scene_id_list(self, value):
        if isinstance(value, list):
            self._disable_scene_id_list = list()
            for i in value:
                self._disable_scene_id_list.append(i)
    @property
    def enable_scene_id_list(self):
        return self._enable_scene_id_list

    @enable_scene_id_list.setter
    def enable_scene_id_list(self, value):
        if isinstance(value, list):
            self._enable_scene_id_list = list()
            for i in value:
                self._enable_scene_id_list.append(i)
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def user_key(self):
        return self._user_key

    @user_key.setter
    def user_key(self, value):
        self._user_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.disable_scene_id_list:
            if isinstance(self.disable_scene_id_list, list):
                for i in range(0, len(self.disable_scene_id_list)):
                    element = self.disable_scene_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.disable_scene_id_list[i] = element.to_alipay_dict()
            if hasattr(self.disable_scene_id_list, 'to_alipay_dict'):
                params['disable_scene_id_list'] = self.disable_scene_id_list.to_alipay_dict()
            else:
                params['disable_scene_id_list'] = self.disable_scene_id_list
        if self.enable_scene_id_list:
            if isinstance(self.enable_scene_id_list, list):
                for i in range(0, len(self.enable_scene_id_list)):
                    element = self.enable_scene_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.enable_scene_id_list[i] = element.to_alipay_dict()
            if hasattr(self.enable_scene_id_list, 'to_alipay_dict'):
                params['enable_scene_id_list'] = self.enable_scene_id_list.to_alipay_dict()
            else:
                params['enable_scene_id_list'] = self.enable_scene_id_list
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.user_key:
            if hasattr(self.user_key, 'to_alipay_dict'):
                params['user_key'] = self.user_key.to_alipay_dict()
            else:
                params['user_key'] = self.user_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAmpeUsersceneModifyModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'disable_scene_id_list' in d:
            o.disable_scene_id_list = d['disable_scene_id_list']
        if 'enable_scene_id_list' in d:
            o.enable_scene_id_list = d['enable_scene_id_list']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'user_key' in d:
            o.user_key = d['user_key']
        return o


