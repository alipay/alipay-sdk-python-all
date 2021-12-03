#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserFamilyShareAuthCheckModel(object):

    def __init__(self):
        self._resource_id = None
        self._scene_id = None
        self._target_biz_user_id = None
        self._target_user_biz_source = None
        self._user_id = None

    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value
    @property
    def target_biz_user_id(self):
        return self._target_biz_user_id

    @target_biz_user_id.setter
    def target_biz_user_id(self, value):
        self._target_biz_user_id = value
    @property
    def target_user_biz_source(self):
        return self._target_user_biz_source

    @target_user_biz_source.setter
    def target_user_biz_source(self, value):
        self._target_user_biz_source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        if self.target_biz_user_id:
            if hasattr(self.target_biz_user_id, 'to_alipay_dict'):
                params['target_biz_user_id'] = self.target_biz_user_id.to_alipay_dict()
            else:
                params['target_biz_user_id'] = self.target_biz_user_id
        if self.target_user_biz_source:
            if hasattr(self.target_user_biz_source, 'to_alipay_dict'):
                params['target_user_biz_source'] = self.target_user_biz_source.to_alipay_dict()
            else:
                params['target_user_biz_source'] = self.target_user_biz_source
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
        o = AlipayUserFamilyShareAuthCheckModel()
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        if 'target_biz_user_id' in d:
            o.target_biz_user_id = d['target_biz_user_id']
        if 'target_user_biz_source' in d:
            o.target_user_biz_source = d['target_user_biz_source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


