#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AdMaterialInfo(object):

    def __init__(self):
        self._id = None
        self._material_url = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def material_url(self):
        return self._material_url

    @material_url.setter
    def material_url(self, value):
        self._material_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.material_url:
            if hasattr(self.material_url, 'to_alipay_dict'):
                params['material_url'] = self.material_url.to_alipay_dict()
            else:
                params['material_url'] = self.material_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AdMaterialInfo()
        if 'id' in d:
            o.id = d['id']
        if 'material_url' in d:
            o.material_url = d['material_url']
        return o


