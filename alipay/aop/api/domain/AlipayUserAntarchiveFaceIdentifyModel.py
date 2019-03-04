#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntarchiveFaceIdentifyModel(object):

    def __init__(self):
        self._biz_scene = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._portrait = None
        self._portrait_auth_rect = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def portrait(self):
        return self._portrait

    @portrait.setter
    def portrait(self, value):
        self._portrait = value
    @property
    def portrait_auth_rect(self):
        return self._portrait_auth_rect

    @portrait_auth_rect.setter
    def portrait_auth_rect(self, value):
        self._portrait_auth_rect = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.portrait:
            if hasattr(self.portrait, 'to_alipay_dict'):
                params['portrait'] = self.portrait.to_alipay_dict()
            else:
                params['portrait'] = self.portrait
        if self.portrait_auth_rect:
            if hasattr(self.portrait_auth_rect, 'to_alipay_dict'):
                params['portrait_auth_rect'] = self.portrait_auth_rect.to_alipay_dict()
            else:
                params['portrait_auth_rect'] = self.portrait_auth_rect
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntarchiveFaceIdentifyModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'portrait' in d:
            o.portrait = d['portrait']
        if 'portrait_auth_rect' in d:
            o.portrait_auth_rect = d['portrait_auth_rect']
        return o


