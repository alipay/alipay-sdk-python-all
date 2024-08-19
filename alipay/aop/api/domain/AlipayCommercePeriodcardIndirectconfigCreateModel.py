#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePeriodcardIndirectconfigCreateModel(object):

    def __init__(self):
        self._group_code = None
        self._group_zm_service_id = None
        self._notify_app_id = None
        self._org_pid = None
        self._sign_scene = None

    @property
    def group_code(self):
        return self._group_code

    @group_code.setter
    def group_code(self, value):
        self._group_code = value
    @property
    def group_zm_service_id(self):
        return self._group_zm_service_id

    @group_zm_service_id.setter
    def group_zm_service_id(self, value):
        self._group_zm_service_id = value
    @property
    def notify_app_id(self):
        return self._notify_app_id

    @notify_app_id.setter
    def notify_app_id(self, value):
        self._notify_app_id = value
    @property
    def org_pid(self):
        return self._org_pid

    @org_pid.setter
    def org_pid(self, value):
        self._org_pid = value
    @property
    def sign_scene(self):
        return self._sign_scene

    @sign_scene.setter
    def sign_scene(self, value):
        self._sign_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.group_code:
            if hasattr(self.group_code, 'to_alipay_dict'):
                params['group_code'] = self.group_code.to_alipay_dict()
            else:
                params['group_code'] = self.group_code
        if self.group_zm_service_id:
            if hasattr(self.group_zm_service_id, 'to_alipay_dict'):
                params['group_zm_service_id'] = self.group_zm_service_id.to_alipay_dict()
            else:
                params['group_zm_service_id'] = self.group_zm_service_id
        if self.notify_app_id:
            if hasattr(self.notify_app_id, 'to_alipay_dict'):
                params['notify_app_id'] = self.notify_app_id.to_alipay_dict()
            else:
                params['notify_app_id'] = self.notify_app_id
        if self.org_pid:
            if hasattr(self.org_pid, 'to_alipay_dict'):
                params['org_pid'] = self.org_pid.to_alipay_dict()
            else:
                params['org_pid'] = self.org_pid
        if self.sign_scene:
            if hasattr(self.sign_scene, 'to_alipay_dict'):
                params['sign_scene'] = self.sign_scene.to_alipay_dict()
            else:
                params['sign_scene'] = self.sign_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePeriodcardIndirectconfigCreateModel()
        if 'group_code' in d:
            o.group_code = d['group_code']
        if 'group_zm_service_id' in d:
            o.group_zm_service_id = d['group_zm_service_id']
        if 'notify_app_id' in d:
            o.notify_app_id = d['notify_app_id']
        if 'org_pid' in d:
            o.org_pid = d['org_pid']
        if 'sign_scene' in d:
            o.sign_scene = d['sign_scene']
        return o


