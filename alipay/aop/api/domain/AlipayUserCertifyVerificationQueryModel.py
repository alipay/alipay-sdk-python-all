#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyVerificationQueryModel(object):

    def __init__(self):
        self._age = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._far = None
        self._gender_score = None
        self._portrait = None
        self._portrait_auth_rect = None
        self._scene_code = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
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
    def far(self):
        return self._far

    @far.setter
    def far(self, value):
        self._far = value
    @property
    def gender_score(self):
        return self._gender_score

    @gender_score.setter
    def gender_score(self, value):
        self._gender_score = value
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
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
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
        if self.far:
            if hasattr(self.far, 'to_alipay_dict'):
                params['far'] = self.far.to_alipay_dict()
            else:
                params['far'] = self.far
        if self.gender_score:
            if hasattr(self.gender_score, 'to_alipay_dict'):
                params['gender_score'] = self.gender_score.to_alipay_dict()
            else:
                params['gender_score'] = self.gender_score
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
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyVerificationQueryModel()
        if 'age' in d:
            o.age = d['age']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'far' in d:
            o.far = d['far']
        if 'gender_score' in d:
            o.gender_score = d['gender_score']
        if 'portrait' in d:
            o.portrait = d['portrait']
        if 'portrait_auth_rect' in d:
            o.portrait_auth_rect = d['portrait_auth_rect']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


