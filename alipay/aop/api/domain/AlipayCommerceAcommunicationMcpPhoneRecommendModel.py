#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationMcpPhoneRecommendModel(object):

    def __init__(self):
        self._faces = None
        self._mobile = None
        self._scene = None
        self._sub_source = None

    @property
    def faces(self):
        return self._faces

    @faces.setter
    def faces(self, value):
        if isinstance(value, list):
            self._faces = list()
            for i in value:
                self._faces.append(i)
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
    @property
    def sub_source(self):
        return self._sub_source

    @sub_source.setter
    def sub_source(self, value):
        self._sub_source = value


    def to_alipay_dict(self):
        params = dict()
        if self.faces:
            if isinstance(self.faces, list):
                for i in range(0, len(self.faces)):
                    element = self.faces[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.faces[i] = element.to_alipay_dict()
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
        if self.sub_source:
            if hasattr(self.sub_source, 'to_alipay_dict'):
                params['sub_source'] = self.sub_source.to_alipay_dict()
            else:
                params['sub_source'] = self.sub_source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationMcpPhoneRecommendModel()
        if 'faces' in d:
            o.faces = d['faces']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sub_source' in d:
            o.sub_source = d['sub_source']
        return o


