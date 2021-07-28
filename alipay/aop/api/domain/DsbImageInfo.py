#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DsbImageInfo(object):

    def __init__(self):
        self._afts_id = None
        self._image_name = None
        self._shoot_time = None

    @property
    def afts_id(self):
        return self._afts_id

    @afts_id.setter
    def afts_id(self, value):
        self._afts_id = value
    @property
    def image_name(self):
        return self._image_name

    @image_name.setter
    def image_name(self, value):
        self._image_name = value
    @property
    def shoot_time(self):
        return self._shoot_time

    @shoot_time.setter
    def shoot_time(self, value):
        self._shoot_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.afts_id:
            if hasattr(self.afts_id, 'to_alipay_dict'):
                params['afts_id'] = self.afts_id.to_alipay_dict()
            else:
                params['afts_id'] = self.afts_id
        if self.image_name:
            if hasattr(self.image_name, 'to_alipay_dict'):
                params['image_name'] = self.image_name.to_alipay_dict()
            else:
                params['image_name'] = self.image_name
        if self.shoot_time:
            if hasattr(self.shoot_time, 'to_alipay_dict'):
                params['shoot_time'] = self.shoot_time.to_alipay_dict()
            else:
                params['shoot_time'] = self.shoot_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DsbImageInfo()
        if 'afts_id' in d:
            o.afts_id = d['afts_id']
        if 'image_name' in d:
            o.image_name = d['image_name']
        if 'shoot_time' in d:
            o.shoot_time = d['shoot_time']
        return o


