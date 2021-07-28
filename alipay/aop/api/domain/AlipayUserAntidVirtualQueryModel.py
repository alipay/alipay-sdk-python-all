#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntidVirtualQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._identification_factor_content = None
        self._identification_factor_type = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def identification_factor_content(self):
        return self._identification_factor_content

    @identification_factor_content.setter
    def identification_factor_content(self, value):
        self._identification_factor_content = value
    @property
    def identification_factor_type(self):
        return self._identification_factor_type

    @identification_factor_type.setter
    def identification_factor_type(self, value):
        self._identification_factor_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.identification_factor_content:
            if hasattr(self.identification_factor_content, 'to_alipay_dict'):
                params['identification_factor_content'] = self.identification_factor_content.to_alipay_dict()
            else:
                params['identification_factor_content'] = self.identification_factor_content
        if self.identification_factor_type:
            if hasattr(self.identification_factor_type, 'to_alipay_dict'):
                params['identification_factor_type'] = self.identification_factor_type.to_alipay_dict()
            else:
                params['identification_factor_type'] = self.identification_factor_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntidVirtualQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'identification_factor_content' in d:
            o.identification_factor_content = d['identification_factor_content']
        if 'identification_factor_type' in d:
            o.identification_factor_type = d['identification_factor_type']
        return o


