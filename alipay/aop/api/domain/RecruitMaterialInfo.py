#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecruitMaterialInfo(object):

    def __init__(self):
        self._material_id = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecruitMaterialInfo()
        if 'material_id' in d:
            o.material_id = d['material_id']
        return o


