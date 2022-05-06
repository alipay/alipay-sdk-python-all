#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAuthResauthCheckModel(object):

    def __init__(self):
        self._auth_scene = None
        self._authorize_pid = None
        self._pid = None

    @property
    def auth_scene(self):
        return self._auth_scene

    @auth_scene.setter
    def auth_scene(self, value):
        self._auth_scene = value
    @property
    def authorize_pid(self):
        return self._authorize_pid

    @authorize_pid.setter
    def authorize_pid(self, value):
        self._authorize_pid = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_scene:
            if hasattr(self.auth_scene, 'to_alipay_dict'):
                params['auth_scene'] = self.auth_scene.to_alipay_dict()
            else:
                params['auth_scene'] = self.auth_scene
        if self.authorize_pid:
            if hasattr(self.authorize_pid, 'to_alipay_dict'):
                params['authorize_pid'] = self.authorize_pid.to_alipay_dict()
            else:
                params['authorize_pid'] = self.authorize_pid
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAuthResauthCheckModel()
        if 'auth_scene' in d:
            o.auth_scene = d['auth_scene']
        if 'authorize_pid' in d:
            o.authorize_pid = d['authorize_pid']
        if 'pid' in d:
            o.pid = d['pid']
        return o


