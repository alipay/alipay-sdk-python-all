#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Reasons import Reasons


class ItemSceneRiskInfo(object):

    def __init__(self):
        self._risk_infos = None
        self._scene = None
        self._scene_code = None

    @property
    def risk_infos(self):
        return self._risk_infos

    @risk_infos.setter
    def risk_infos(self, value):
        if isinstance(value, list):
            self._risk_infos = list()
            for i in value:
                if isinstance(i, Reasons):
                    self._risk_infos.append(i)
                else:
                    self._risk_infos.append(Reasons.from_alipay_dict(i))
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_infos:
            if isinstance(self.risk_infos, list):
                for i in range(0, len(self.risk_infos)):
                    element = self.risk_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.risk_infos[i] = element.to_alipay_dict()
            if hasattr(self.risk_infos, 'to_alipay_dict'):
                params['risk_infos'] = self.risk_infos.to_alipay_dict()
            else:
                params['risk_infos'] = self.risk_infos
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemSceneRiskInfo()
        if 'risk_infos' in d:
            o.risk_infos = d['risk_infos']
        if 'scene' in d:
            o.scene = d['scene']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


