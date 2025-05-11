#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NorderTagPositionExtInfo(object):

    def __init__(self):
        self._brand = None
        self._place = None
        self._scene = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        self._place = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand:
            if hasattr(self.brand, 'to_alipay_dict'):
                params['brand'] = self.brand.to_alipay_dict()
            else:
                params['brand'] = self.brand
        if self.place:
            if hasattr(self.place, 'to_alipay_dict'):
                params['place'] = self.place.to_alipay_dict()
            else:
                params['place'] = self.place
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
        o = NorderTagPositionExtInfo()
        if 'brand' in d:
            o.brand = d['brand']
        if 'place' in d:
            o.place = d['place']
        if 'scene' in d:
            o.scene = d['scene']
        return o


