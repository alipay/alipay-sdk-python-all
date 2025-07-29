#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskPolicyCaptchaCheckModel(object):

    def __init__(self):
        self._captcha_bizno = None
        self._captcha_id = None
        self._captcha_scene = None
        self._captcha_token = None
        self._consult_data = None
        self._extra_data = None

    @property
    def captcha_bizno(self):
        return self._captcha_bizno

    @captcha_bizno.setter
    def captcha_bizno(self, value):
        self._captcha_bizno = value
    @property
    def captcha_id(self):
        return self._captcha_id

    @captcha_id.setter
    def captcha_id(self, value):
        self._captcha_id = value
    @property
    def captcha_scene(self):
        return self._captcha_scene

    @captcha_scene.setter
    def captcha_scene(self, value):
        self._captcha_scene = value
    @property
    def captcha_token(self):
        return self._captcha_token

    @captcha_token.setter
    def captcha_token(self, value):
        self._captcha_token = value
    @property
    def consult_data(self):
        return self._consult_data

    @consult_data.setter
    def consult_data(self, value):
        self._consult_data = value
    @property
    def extra_data(self):
        return self._extra_data

    @extra_data.setter
    def extra_data(self, value):
        self._extra_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.captcha_bizno:
            if hasattr(self.captcha_bizno, 'to_alipay_dict'):
                params['captcha_bizno'] = self.captcha_bizno.to_alipay_dict()
            else:
                params['captcha_bizno'] = self.captcha_bizno
        if self.captcha_id:
            if hasattr(self.captcha_id, 'to_alipay_dict'):
                params['captcha_id'] = self.captcha_id.to_alipay_dict()
            else:
                params['captcha_id'] = self.captcha_id
        if self.captcha_scene:
            if hasattr(self.captcha_scene, 'to_alipay_dict'):
                params['captcha_scene'] = self.captcha_scene.to_alipay_dict()
            else:
                params['captcha_scene'] = self.captcha_scene
        if self.captcha_token:
            if hasattr(self.captcha_token, 'to_alipay_dict'):
                params['captcha_token'] = self.captcha_token.to_alipay_dict()
            else:
                params['captcha_token'] = self.captcha_token
        if self.consult_data:
            if hasattr(self.consult_data, 'to_alipay_dict'):
                params['consult_data'] = self.consult_data.to_alipay_dict()
            else:
                params['consult_data'] = self.consult_data
        if self.extra_data:
            if hasattr(self.extra_data, 'to_alipay_dict'):
                params['extra_data'] = self.extra_data.to_alipay_dict()
            else:
                params['extra_data'] = self.extra_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskPolicyCaptchaCheckModel()
        if 'captcha_bizno' in d:
            o.captcha_bizno = d['captcha_bizno']
        if 'captcha_id' in d:
            o.captcha_id = d['captcha_id']
        if 'captcha_scene' in d:
            o.captcha_scene = d['captcha_scene']
        if 'captcha_token' in d:
            o.captcha_token = d['captcha_token']
        if 'consult_data' in d:
            o.consult_data = d['consult_data']
        if 'extra_data' in d:
            o.extra_data = d['extra_data']
        return o


