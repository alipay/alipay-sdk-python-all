#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneConfigQueryDTO(object):

    def __init__(self):
        self._business_scene = None
        self._group_id = None
        self._isv_name = None
        self._pid = None
        self._school_id = None
        self._school_name = None
        self._school_std_code = None
        self._sign_app_id = None
        self._status = None

    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        if isinstance(value, list):
            self._business_scene = list()
            for i in value:
                self._business_scene.append(i)
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
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
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
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
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_scene:
            if isinstance(self.business_scene, list):
                for i in range(0, len(self.business_scene)):
                    element = self.business_scene[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.business_scene[i] = element.to_alipay_dict()
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
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
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
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
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneConfigQueryDTO()
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'school_id' in d:
            o.school_id = d['school_id']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        if 'sign_app_id' in d:
            o.sign_app_id = d['sign_app_id']
        if 'status' in d:
            o.status = d['status']
        return o


