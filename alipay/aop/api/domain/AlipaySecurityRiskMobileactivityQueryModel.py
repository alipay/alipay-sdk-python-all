#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskMobileactivityQueryModel(object):

    def __init__(self):
        self._mobile = None
        self._scene_id = None
        self._user_id = None

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskMobileactivityQueryModel()
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


