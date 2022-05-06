#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnergyExtRequest import EnergyExtRequest


class AlipayEcoCityserviceIndustryEnergySendModel(object):

    def __init__(self):
        self._ext_info = None
        self._outer_no = None
        self._scene = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, EnergyExtRequest):
            self._ext_info = value
        else:
            self._ext_info = EnergyExtRequest.from_alipay_dict(value)
    @property
    def outer_no(self):
        return self._outer_no

    @outer_no.setter
    def outer_no(self, value):
        self._outer_no = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.outer_no:
            if hasattr(self.outer_no, 'to_alipay_dict'):
                params['outer_no'] = self.outer_no.to_alipay_dict()
            else:
                params['outer_no'] = self.outer_no
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
        o = AlipayEcoCityserviceIndustryEnergySendModel()
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'outer_no' in d:
            o.outer_no = d['outer_no']
        if 'scene' in d:
            o.scene = d['scene']
        return o


