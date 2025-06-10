#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeCrowdConsultModel(object):

    def __init__(self):
        self._open_id = None
        self._scene = None
        self._scene_list = None
        self._user_id = None

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
    def scene_list(self):
        return self._scene_list

    @scene_list.setter
    def scene_list(self, value):
        if isinstance(value, list):
            self._scene_list = list()
            for i in value:
                self._scene_list.append(i)
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


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
        if self.scene_list:
            if isinstance(self.scene_list, list):
                for i in range(0, len(self.scene_list)):
                    element = self.scene_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.scene_list[i] = element.to_alipay_dict()
            if hasattr(self.scene_list, 'to_alipay_dict'):
                params['scene_list'] = self.scene_list.to_alipay_dict()
            else:
                params['scene_list'] = self.scene_list
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeCrowdConsultModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'scene_list' in d:
            o.scene_list = d['scene_list']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


