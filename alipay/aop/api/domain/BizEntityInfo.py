#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizEntityInfo(object):

    def __init__(self):
        self._store_door_img = None

    @property
    def store_door_img(self):
        return self._store_door_img

    @store_door_img.setter
    def store_door_img(self, value):
        self._store_door_img = value


    def to_alipay_dict(self):
        params = dict()
        if self.store_door_img:
            if hasattr(self.store_door_img, 'to_alipay_dict'):
                params['store_door_img'] = self.store_door_img.to_alipay_dict()
            else:
                params['store_door_img'] = self.store_door_img
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizEntityInfo()
        if 'store_door_img' in d:
            o.store_door_img = d['store_door_img']
        return o


