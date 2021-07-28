#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniDeveloppackageQueryModel(object):

    def __init__(self):
        self._bundle_id = None
        self._deploy_version = None
        self._developer_version = None
        self._inst_code = None
        self._mini_app_id = None
        self._protocol = None
        self._scene = None
        self._user_id = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def deploy_version(self):
        return self._deploy_version

    @deploy_version.setter
    def deploy_version(self, value):
        self._deploy_version = value
    @property
    def developer_version(self):
        return self._developer_version

    @developer_version.setter
    def developer_version(self, value):
        self._developer_version = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.deploy_version:
            if hasattr(self.deploy_version, 'to_alipay_dict'):
                params['deploy_version'] = self.deploy_version.to_alipay_dict()
            else:
                params['deploy_version'] = self.deploy_version
        if self.developer_version:
            if hasattr(self.developer_version, 'to_alipay_dict'):
                params['developer_version'] = self.developer_version.to_alipay_dict()
            else:
                params['developer_version'] = self.developer_version
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.protocol:
            if hasattr(self.protocol, 'to_alipay_dict'):
                params['protocol'] = self.protocol.to_alipay_dict()
            else:
                params['protocol'] = self.protocol
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
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
        o = AlipayOpenMiniDeveloppackageQueryModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'deploy_version' in d:
            o.deploy_version = d['deploy_version']
        if 'developer_version' in d:
            o.developer_version = d['developer_version']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'protocol' in d:
            o.protocol = d['protocol']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


