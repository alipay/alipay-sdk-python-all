#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAgreementAuthApplyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._auth_confirm_type = None
        self._auth_scene = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def auth_confirm_type(self):
        return self._auth_confirm_type

    @auth_confirm_type.setter
    def auth_confirm_type(self, value):
        self._auth_confirm_type = value
    @property
    def auth_scene(self):
        return self._auth_scene

    @auth_scene.setter
    def auth_scene(self, value):
        self._auth_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.auth_confirm_type:
            if hasattr(self.auth_confirm_type, 'to_alipay_dict'):
                params['auth_confirm_type'] = self.auth_confirm_type.to_alipay_dict()
            else:
                params['auth_confirm_type'] = self.auth_confirm_type
        if self.auth_scene:
            if hasattr(self.auth_scene, 'to_alipay_dict'):
                params['auth_scene'] = self.auth_scene.to_alipay_dict()
            else:
                params['auth_scene'] = self.auth_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAgreementAuthApplyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'auth_confirm_type' in d:
            o.auth_confirm_type = d['auth_confirm_type']
        if 'auth_scene' in d:
            o.auth_scene = d['auth_scene']
        return o


