#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntidVirtualCreateModel(object):

    def __init__(self):
        self._biz_scene = None
        self._ext_info = None
        self._identification_factor_content = None
        self._identification_factor_type = None
        self._register_from = None
        self._user_type = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
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
    @property
    def register_from(self):
        return self._register_from

    @register_from.setter
    def register_from(self, value):
        self._register_from = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.register_from:
            if hasattr(self.register_from, 'to_alipay_dict'):
                params['register_from'] = self.register_from.to_alipay_dict()
            else:
                params['register_from'] = self.register_from
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntidVirtualCreateModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'identification_factor_content' in d:
            o.identification_factor_content = d['identification_factor_content']
        if 'identification_factor_type' in d:
            o.identification_factor_type = d['identification_factor_type']
        if 'register_from' in d:
            o.register_from = d['register_from']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


