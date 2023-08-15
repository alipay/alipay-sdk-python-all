#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneSubArea(object):

    def __init__(self):
        self._area_id = None
        self._name = None
        self._recommend_spot_id = None

    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def recommend_spot_id(self):
        return self._recommend_spot_id

    @recommend_spot_id.setter
    def recommend_spot_id(self, value):
        self._recommend_spot_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_id:
            if hasattr(self.area_id, 'to_alipay_dict'):
                params['area_id'] = self.area_id.to_alipay_dict()
            else:
                params['area_id'] = self.area_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.recommend_spot_id:
            if hasattr(self.recommend_spot_id, 'to_alipay_dict'):
                params['recommend_spot_id'] = self.recommend_spot_id.to_alipay_dict()
            else:
                params['recommend_spot_id'] = self.recommend_spot_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneSubArea()
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'name' in d:
            o.name = d['name']
        if 'recommend_spot_id' in d:
            o.recommend_spot_id = d['recommend_spot_id']
        return o


