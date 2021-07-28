#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppPluginReference import MiniAppPluginReference
from alipay.aop.api.domain.SubPackage import SubPackage


class AlipayOpenMiniInnerversionPreviewUploadModel(object):

    def __init__(self):
        self._build_js_permission = None
        self._build_pkg_url = None
        self._build_plugin_url = None
        self._bundle_id = None
        self._extend_info = None
        self._inst_code = None
        self._main_url = None
        self._mini_app_id = None
        self._new_build_pkg_url = None
        self._new_build_plugin_url = None
        self._plugin_refs = None
        self._scene = None
        self._sub_packages = None

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
    def build_plugin_url(self):
        return self._build_plugin_url

    @build_plugin_url.setter
    def build_plugin_url(self, value):
        self._build_plugin_url = value
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
    def new_build_pkg_url(self):
        return self._new_build_pkg_url

    @new_build_pkg_url.setter
    def new_build_pkg_url(self, value):
        self._new_build_pkg_url = value
    @property
    def new_build_plugin_url(self):
        return self._new_build_plugin_url

    @new_build_plugin_url.setter
    def new_build_plugin_url(self, value):
        self._new_build_plugin_url = value
    @property
    def plugin_refs(self):
        return self._plugin_refs

    @plugin_refs.setter
    def plugin_refs(self, value):
        if isinstance(value, list):
            self._plugin_refs = list()
            for i in value:
                if isinstance(i, MiniAppPluginReference):
                    self._plugin_refs.append(i)
                else:
                    self._plugin_refs.append(MiniAppPluginReference.from_alipay_dict(i))
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def sub_packages(self):
        return self._sub_packages

    @sub_packages.setter
    def sub_packages(self, value):
        if isinstance(value, list):
            self._sub_packages = list()
            for i in value:
                if isinstance(i, SubPackage):
                    self._sub_packages.append(i)
                else:
                    self._sub_packages.append(SubPackage.from_alipay_dict(i))


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
        if self.build_plugin_url:
            if hasattr(self.build_plugin_url, 'to_alipay_dict'):
                params['build_plugin_url'] = self.build_plugin_url.to_alipay_dict()
            else:
                params['build_plugin_url'] = self.build_plugin_url
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
        if self.new_build_pkg_url:
            if hasattr(self.new_build_pkg_url, 'to_alipay_dict'):
                params['new_build_pkg_url'] = self.new_build_pkg_url.to_alipay_dict()
            else:
                params['new_build_pkg_url'] = self.new_build_pkg_url
        if self.new_build_plugin_url:
            if hasattr(self.new_build_plugin_url, 'to_alipay_dict'):
                params['new_build_plugin_url'] = self.new_build_plugin_url.to_alipay_dict()
            else:
                params['new_build_plugin_url'] = self.new_build_plugin_url
        if self.plugin_refs:
            if isinstance(self.plugin_refs, list):
                for i in range(0, len(self.plugin_refs)):
                    element = self.plugin_refs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plugin_refs[i] = element.to_alipay_dict()
            if hasattr(self.plugin_refs, 'to_alipay_dict'):
                params['plugin_refs'] = self.plugin_refs.to_alipay_dict()
            else:
                params['plugin_refs'] = self.plugin_refs
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.sub_packages:
            if isinstance(self.sub_packages, list):
                for i in range(0, len(self.sub_packages)):
                    element = self.sub_packages[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_packages[i] = element.to_alipay_dict()
            if hasattr(self.sub_packages, 'to_alipay_dict'):
                params['sub_packages'] = self.sub_packages.to_alipay_dict()
            else:
                params['sub_packages'] = self.sub_packages
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
        if 'build_plugin_url' in d:
            o.build_plugin_url = d['build_plugin_url']
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
        if 'new_build_pkg_url' in d:
            o.new_build_pkg_url = d['new_build_pkg_url']
        if 'new_build_plugin_url' in d:
            o.new_build_plugin_url = d['new_build_plugin_url']
        if 'plugin_refs' in d:
            o.plugin_refs = d['plugin_refs']
        if 'scene' in d:
            o.scene = d['scene']
        if 'sub_packages' in d:
            o.sub_packages = d['sub_packages']
        return o


