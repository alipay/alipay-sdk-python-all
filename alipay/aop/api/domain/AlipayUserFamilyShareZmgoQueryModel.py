#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserFamilyShareZmgoQueryModel(object):

    def __init__(self):
        self._enable_personal = None
        self._scene_id = None
        self._template_id = None
        self._user_id = None

    @property
    def enable_personal(self):
        return self._enable_personal

    @enable_personal.setter
    def enable_personal(self, value):
        self._enable_personal = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.enable_personal:
            if hasattr(self.enable_personal, 'to_alipay_dict'):
                params['enable_personal'] = self.enable_personal.to_alipay_dict()
            else:
                params['enable_personal'] = self.enable_personal
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
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
        o = AlipayUserFamilyShareZmgoQueryModel()
        if 'enable_personal' in d:
            o.enable_personal = d['enable_personal']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


