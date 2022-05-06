#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateSceneConfigCreateModel(object):

    def __init__(self):
        self._business_scene = None
        self._pid = None
        self._school_id = None
        self._school_std_code = None
        self._sign_app_id = None

    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def school_id(self):
        return self._school_id

    @school_id.setter
    def school_id(self, value):
        self._school_id = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value
    @property
    def sign_app_id(self):
        return self._sign_app_id

    @sign_app_id.setter
    def sign_app_id(self, value):
        self._sign_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.school_id:
            if hasattr(self.school_id, 'to_alipay_dict'):
                params['school_id'] = self.school_id.to_alipay_dict()
            else:
                params['school_id'] = self.school_id
        if self.school_std_code:
            if hasattr(self.school_std_code, 'to_alipay_dict'):
                params['school_std_code'] = self.school_std_code.to_alipay_dict()
            else:
                params['school_std_code'] = self.school_std_code
        if self.sign_app_id:
            if hasattr(self.sign_app_id, 'to_alipay_dict'):
                params['sign_app_id'] = self.sign_app_id.to_alipay_dict()
            else:
                params['sign_app_id'] = self.sign_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSceneConfigCreateModel()
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'pid' in d:
            o.pid = d['pid']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        if 'sign_app_id' in d:
            o.sign_app_id = d['sign_app_id']
        return o


