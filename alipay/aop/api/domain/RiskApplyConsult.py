#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskApplyConsult(object):

    def __init__(self):
        self._consult_time = None
        self._risk_desc = None
        self._risk_level = None
        self._risk_scene = None

    @property
    def consult_time(self):
        return self._consult_time

    @consult_time.setter
    def consult_time(self, value):
        self._consult_time = value
    @property
    def risk_desc(self):
        return self._risk_desc

    @risk_desc.setter
    def risk_desc(self, value):
        self._risk_desc = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.consult_time:
            if hasattr(self.consult_time, 'to_alipay_dict'):
                params['consult_time'] = self.consult_time.to_alipay_dict()
            else:
                params['consult_time'] = self.consult_time
        if self.risk_desc:
            if hasattr(self.risk_desc, 'to_alipay_dict'):
                params['risk_desc'] = self.risk_desc.to_alipay_dict()
            else:
                params['risk_desc'] = self.risk_desc
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskApplyConsult()
        if 'consult_time' in d:
            o.consult_time = d['consult_time']
        if 'risk_desc' in d:
            o.risk_desc = d['risk_desc']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_scene' in d:
            o.risk_scene = d['risk_scene']
        return o


