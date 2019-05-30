#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionPreviewUploadModel(object):

    def __init__(self):
        self._build_js_permission = None
        self._build_pkg_url = None
        self._bundle_id = None
        self._extend_info = None
        self._inst_code = None
        self._main_url = None
        self._mini_app_id = None
        self._scene = None

    @property
    def build_js_permission(self):
        return self._build_js_permission

    @build_js_permission.setter
    def build_js_permission(self, value):
        self._build_js_permission = value
    @property
    def build_pkg_url(self):
        return self._build_pkg_url

    @build_pkg_url.setter
    def build_pkg_url(self, value):
        self._build_pkg_url = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def main_url(self):
        return self._main_url

    @main_url.setter
    def main_url(self, value):
        self._main_url = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.build_js_permission:
            if hasattr(self.build_js_permission, 'to_alipay_dict'):
                params['build_js_permission'] = self.build_js_permission.to_alipay_dict()
            else:
                params['build_js_permission'] = self.build_js_permission
        if self.build_pkg_url:
            if hasattr(self.build_pkg_url, 'to_alipay_dict'):
                params['build_pkg_url'] = self.build_pkg_url.to_alipay_dict()
            else:
                params['build_pkg_url'] = self.build_pkg_url
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.extend_info:
            if hasattr(self.extend_info, 'to_alipay_dict'):
                params['extend_info'] = self.extend_info.to_alipay_dict()
            else:
                params['extend_info'] = self.extend_info
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.main_url:
            if hasattr(self.main_url, 'to_alipay_dict'):
                params['main_url'] = self.main_url.to_alipay_dict()
            else:
                params['main_url'] = self.main_url
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionPreviewUploadModel()
        if 'build_js_permission' in d:
            o.build_js_permission = d['build_js_permission']
        if 'build_pkg_url' in d:
            o.build_pkg_url = d['build_pkg_url']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'extend_info' in d:
            o.extend_info = d['extend_info']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'main_url' in d:
            o.main_url = d['main_url']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'scene' in d:
            o.scene = d['scene']
        return o


