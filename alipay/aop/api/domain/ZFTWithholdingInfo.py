#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZFTWithholdingInfo(object):

    def __init__(self):
        self._sign_scene = None
        self._withholding_service_feature_name = None

    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value
    @property
    def withholding_service_feature_name(self):
        return self._withholding_service_feature_name

    @withholding_service_feature_name.setter
    def withholding_service_feature_name(self, value):
        self._withholding_service_feature_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        if self.withholding_service_feature_name:
            if hasattr(self.withholding_service_feature_name, 'to_alipay_dict'):
                params['withholding_service_feature_name'] = self.withholding_service_feature_name.to_alipay_dict()
            else:
                params['withholding_service_feature_name'] = self.withholding_service_feature_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZFTWithholdingInfo()
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        if 'withholding_service_feature_name' in d:
            o.withholding_service_feature_name = d['withholding_service_feature_name']
        return o


