#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationDiscountPhoneRecommendModel(object):

    def __init__(self):
        self._faces = None
        self._mobile = None
        self._scene = None

    @property
    def faces(self):
        return self._faces

    @faces.setter
    def faces(self, value):
        self._faces = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.faces:
            if hasattr(self.faces, 'to_alipay_dict'):
                params['faces'] = self.faces.to_alipay_dict()
            else:
                params['faces'] = self.faces
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
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
        o = AlipayCommerceAcommunicationDiscountPhoneRecommendModel()
        if 'faces' in d:
            o.faces = d['faces']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'scene' in d:
            o.scene = d['scene']
        return o


