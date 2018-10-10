#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EntityPriorRiskVO(object):

    def __init__(self):
        self._dispose_department = None
        self._risk_detail = None
        self._risk_level = None
        self._risk_scene = None
        self._risk_type = None

    @property
    def dispose_department(self):
        return self._dispose_department

    @dispose_department.setter
    def dispose_department(self, value):
        self._dispose_department = value
    @property
    def risk_detail(self):
        return self._risk_detail

    @risk_detail.setter
    def risk_detail(self, value):
        self._risk_detail = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_scene(self):
        return self._risk_scene

    @risk_scene.setter
    def risk_scene(self, value):
        self._risk_scene = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.dispose_department:
            if hasattr(self.dispose_department, 'to_alipay_dict'):
                params['dispose_department'] = self.dispose_department.to_alipay_dict()
            else:
                params['dispose_department'] = self.dispose_department
        if self.risk_detail:
            if hasattr(self.risk_detail, 'to_alipay_dict'):
                params['risk_detail'] = self.risk_detail.to_alipay_dict()
            else:
                params['risk_detail'] = self.risk_detail
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_scene:
            if hasattr(self.risk_scene, 'to_alipay_dict'):
                params['risk_scene'] = self.risk_scene.to_alipay_dict()
            else:
                params['risk_scene'] = self.risk_scene
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EntityPriorRiskVO()
        if 'dispose_department' in d:
            o.dispose_department = d['dispose_department']
        if 'risk_detail' in d:
            o.risk_detail = d['risk_detail']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_scene' in d:
            o.risk_scene = d['risk_scene']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        return o


