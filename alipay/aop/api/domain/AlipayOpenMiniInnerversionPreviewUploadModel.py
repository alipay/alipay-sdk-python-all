#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionPreviewUploadModel(object):

    def __init__(self):
        self._build_js_permission = None
        self._build_pkg_url = None
        self._mini_app_id = None

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
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value


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
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
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
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o


