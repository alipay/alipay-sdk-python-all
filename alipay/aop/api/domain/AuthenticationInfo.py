#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AuthenticationScene import AuthenticationScene
from alipay.aop.api.domain.PrincipalInfo import PrincipalInfo


class AuthenticationInfo(object):

    def __init__(self):
        self._authentication_scene = None
        self._biz_id = None
        self._extend_info = None
        self._principal_info = None

    @property
    def authentication_scene(self):
        return self._authentication_scene

    @authentication_scene.setter
    def authentication_scene(self, value):
        if isinstance(value, AuthenticationScene):
            self._authentication_scene = value
        else:
            self._authentication_scene = AuthenticationScene.from_alipay_dict(value)
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def principal_info(self):
        return self._principal_info

    @principal_info.setter
    def principal_info(self, value):
        if isinstance(value, PrincipalInfo):
            self._principal_info = value
        else:
            self._principal_info = PrincipalInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.authentication_scene:
            if hasattr(self.authentication_scene, 'to_alipay_dict'):
                params['authentication_scene'] = self.authentication_scene.to_alipay_dict()
            else:
                params['authentication_scene'] = self.authentication_scene
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.principal_info:
            if hasattr(self.principal_info, 'to_alipay_dict'):
                params['principal_info'] = self.principal_info.to_alipay_dict()
            else:
                params['principal_info'] = self.principal_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthenticationInfo()
        if 'authentication_scene' in d:
            o.authentication_scene = d['authentication_scene']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'principal_info' in d:
            o.principal_info = d['principal_info']
        return o


