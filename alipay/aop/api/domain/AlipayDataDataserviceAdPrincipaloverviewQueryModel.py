#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAdPrincipaloverviewQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._charge_mode = None
        self._principal_tag = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def charge_mode(self):
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, value):
        self._charge_mode = value
    @property
    def principal_tag(self):
        return self._principal_tag

    @principal_tag.setter
    def principal_tag(self, value):
        self._principal_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.charge_mode:
            if hasattr(self.charge_mode, 'to_alipay_dict'):
                params['charge_mode'] = self.charge_mode.to_alipay_dict()
            else:
                params['charge_mode'] = self.charge_mode
        if self.principal_tag:
            if hasattr(self.principal_tag, 'to_alipay_dict'):
                params['principal_tag'] = self.principal_tag.to_alipay_dict()
            else:
                params['principal_tag'] = self.principal_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAdPrincipaloverviewQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'charge_mode' in d:
            o.charge_mode = d['charge_mode']
        if 'principal_tag' in d:
            o.principal_tag = d['principal_tag']
        return o


