#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialBaseSceneContentQueryModel(object):

    def __init__(self):
        self._city_id = None
        self._scene_id = None
        self._top_size = None
        self._user_id = None

    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def top_size(self):
        return self._top_size

    @top_size.setter
    def top_size(self, value):
        self._top_size = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_id:
            if hasattr(self.city_id, 'to_alipay_dict'):
                params['city_id'] = self.city_id.to_alipay_dict()
            else:
                params['city_id'] = self.city_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.top_size:
            if hasattr(self.top_size, 'to_alipay_dict'):
                params['top_size'] = self.top_size.to_alipay_dict()
            else:
                params['top_size'] = self.top_size
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
        o = AlipaySocialBaseSceneContentQueryModel()
        if 'city_id' in d:
            o.city_id = d['city_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'top_size' in d:
            o.top_size = d['top_size']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


