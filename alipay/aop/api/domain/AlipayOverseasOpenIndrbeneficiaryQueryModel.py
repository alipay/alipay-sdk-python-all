#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasOpenIndrbeneficiaryQueryModel(object):

    def __init__(self):
        self._beneficiary_name = None
        self._scene_type = None

    @property
    def beneficiary_name(self):
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, value):
        self._beneficiary_name = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary_name:
            if hasattr(self.beneficiary_name, 'to_alipay_dict'):
                params['beneficiary_name'] = self.beneficiary_name.to_alipay_dict()
            else:
                params['beneficiary_name'] = self.beneficiary_name
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasOpenIndrbeneficiaryQueryModel()
        if 'beneficiary_name' in d:
            o.beneficiary_name = d['beneficiary_name']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        return o


