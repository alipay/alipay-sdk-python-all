#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppPluginReference import MiniAppPluginReference
from alipay.aop.api.domain.SubPackageInfo import SubPackageInfo


class AlipayOpenMiniInnerversionNobuildUploadModel(object):

    def __init__(self):
        self._build_extra_info = None
        self._build_js_permission = None
        self._build_main_url = None
        self._build_qcloud_info = None
        self._build_version = None
        self._builded_package_size = None
        self._builded_package_url = None
        self._builded_plugin_size = None
        self._builded_plugin_url = None
        self._bundle_id = None
        self._components = None
        self._inst_code = None
        self._mini_app_id = None
        self._new_builded_package_size = None
        self._new_builded_package_url = None
        self._new_builded_plugin_size = None
        self._new_builded_plugin_url = None
        self._plugin_refs = None
        self._sub_packages = None

    @property
    def build_extra_info(self):
        return self._build_extra_info

    @build_extra_info.setter
    def build_extra_info(self, value):
        self._build_extra_info = value
    @property
    def build_js_permission(self):
        return self._build_js_permission

    @build_js_permission.setter
    def build_js_permission(self, value):
        self._build_js_permission = value
    @property
    def build_main_url(self):
        return self._build_main_url

    @build_main_url.setter
    def build_main_url(self, value):
        self._build_main_url = value
    @property
    def build_qcloud_info(self):
        return self._build_qcloud_info

    @build_qcloud_info.setter
    def build_qcloud_info(self, value):
        self._build_qcloud_info = value
    @property
    def build_version(self):
        return self._build_version

    @build_version.setter
    def build_version(self, value):
        self._build_version = value
    @property
    def builded_package_size(self):
        return self._builded_package_size

    @builded_package_size.setter
    def builded_package_size(self, value):
        self._builded_package_size = value
    @property
    def builded_package_url(self):
        return self._builded_package_url

    @builded_package_url.setter
    def builded_package_url(self, value):
        self._builded_package_url = value
    @property
    def builded_plugin_size(self):
        return self._builded_plugin_size

    @builded_plugin_size.setter
    def builded_plugin_size(self, value):
        self._builded_plugin_size = value
    @property
    def builded_plugin_url(self):
        return self._builded_plugin_url

    @builded_plugin_url.setter
    def builded_plugin_url(self, value):
        self._builded_plugin_url = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def components(self):
        return self._components

    @components.setter
    def components(self, value):
        self._components = value
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
    def new_builded_package_size(self):
        return self._new_builded_package_size

    @new_builded_package_size.setter
    def new_builded_package_size(self, value):
        self._new_builded_package_size = value
    @property
    def new_builded_package_url(self):
        return self._new_builded_package_url

    @new_builded_package_url.setter
    def new_builded_package_url(self, value):
        self._new_builded_package_url = value
    @property
    def new_builded_plugin_size(self):
        return self._new_builded_plugin_size

    @new_builded_plugin_size.setter
    def new_builded_plugin_size(self, value):
        self._new_builded_plugin_size = value
    @property
    def new_builded_plugin_url(self):
        return self._new_builded_plugin_url

    @new_builded_plugin_url.setter
    def new_builded_plugin_url(self, value):
        self._new_builded_plugin_url = value
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
    def sub_packages(self):
        return self._sub_packages

    @sub_packages.setter
    def sub_packages(self, value):
        if isinstance(value, list):
            self._sub_packages = list()
            for i in value:
                if isinstance(i, SubPackageInfo):
                    self._sub_packages.append(i)
                else:
                    self._sub_packages.append(SubPackageInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.build_extra_info:
            if hasattr(self.build_extra_info, 'to_alipay_dict'):
                params['build_extra_info'] = self.build_extra_info.to_alipay_dict()
            else:
                params['build_extra_info'] = self.build_extra_info
        if self.build_js_permission:
            if hasattr(self.build_js_permission, 'to_alipay_dict'):
                params['build_js_permission'] = self.build_js_permission.to_alipay_dict()
            else:
                params['build_js_permission'] = self.build_js_permission
        if self.build_main_url:
            if hasattr(self.build_main_url, 'to_alipay_dict'):
                params['build_main_url'] = self.build_main_url.to_alipay_dict()
            else:
                params['build_main_url'] = self.build_main_url
        if self.build_qcloud_info:
            if hasattr(self.build_qcloud_info, 'to_alipay_dict'):
                params['build_qcloud_info'] = self.build_qcloud_info.to_alipay_dict()
            else:
                params['build_qcloud_info'] = self.build_qcloud_info
        if self.build_version:
            if hasattr(self.build_version, 'to_alipay_dict'):
                params['build_version'] = self.build_version.to_alipay_dict()
            else:
                params['build_version'] = self.build_version
        if self.builded_package_size:
            if hasattr(self.builded_package_size, 'to_alipay_dict'):
                params['builded_package_size'] = self.builded_package_size.to_alipay_dict()
            else:
                params['builded_package_size'] = self.builded_package_size
        if self.builded_package_url:
            if hasattr(self.builded_package_url, 'to_alipay_dict'):
                params['builded_package_url'] = self.builded_package_url.to_alipay_dict()
            else:
                params['builded_package_url'] = self.builded_package_url
        if self.builded_plugin_size:
            if hasattr(self.builded_plugin_size, 'to_alipay_dict'):
                params['builded_plugin_size'] = self.builded_plugin_size.to_alipay_dict()
            else:
                params['builded_plugin_size'] = self.builded_plugin_size
        if self.builded_plugin_url:
            if hasattr(self.builded_plugin_url, 'to_alipay_dict'):
                params['builded_plugin_url'] = self.builded_plugin_url.to_alipay_dict()
            else:
                params['builded_plugin_url'] = self.builded_plugin_url
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.components:
            if hasattr(self.components, 'to_alipay_dict'):
                params['components'] = self.components.to_alipay_dict()
            else:
                params['components'] = self.components
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
        if self.new_builded_package_size:
            if hasattr(self.new_builded_package_size, 'to_alipay_dict'):
                params['new_builded_package_size'] = self.new_builded_package_size.to_alipay_dict()
            else:
                params['new_builded_package_size'] = self.new_builded_package_size
        if self.new_builded_package_url:
            if hasattr(self.new_builded_package_url, 'to_alipay_dict'):
                params['new_builded_package_url'] = self.new_builded_package_url.to_alipay_dict()
            else:
                params['new_builded_package_url'] = self.new_builded_package_url
        if self.new_builded_plugin_size:
            if hasattr(self.new_builded_plugin_size, 'to_alipay_dict'):
                params['new_builded_plugin_size'] = self.new_builded_plugin_size.to_alipay_dict()
            else:
                params['new_builded_plugin_size'] = self.new_builded_plugin_size
        if self.new_builded_plugin_url:
            if hasattr(self.new_builded_plugin_url, 'to_alipay_dict'):
                params['new_builded_plugin_url'] = self.new_builded_plugin_url.to_alipay_dict()
            else:
                params['new_builded_plugin_url'] = self.new_builded_plugin_url
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
        o = AlipayOpenMiniInnerversionNobuildUploadModel()
        if 'build_extra_info' in d:
            o.build_extra_info = d['build_extra_info']
        if 'build_js_permission' in d:
            o.build_js_permission = d['build_js_permission']
        if 'build_main_url' in d:
            o.build_main_url = d['build_main_url']
        if 'build_qcloud_info' in d:
            o.build_qcloud_info = d['build_qcloud_info']
        if 'build_version' in d:
            o.build_version = d['build_version']
        if 'builded_package_size' in d:
            o.builded_package_size = d['builded_package_size']
        if 'builded_package_url' in d:
            o.builded_package_url = d['builded_package_url']
        if 'builded_plugin_size' in d:
            o.builded_plugin_size = d['builded_plugin_size']
        if 'builded_plugin_url' in d:
            o.builded_plugin_url = d['builded_plugin_url']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'components' in d:
            o.components = d['components']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'new_builded_package_size' in d:
            o.new_builded_package_size = d['new_builded_package_size']
        if 'new_builded_package_url' in d:
            o.new_builded_package_url = d['new_builded_package_url']
        if 'new_builded_plugin_size' in d:
            o.new_builded_plugin_size = d['new_builded_plugin_size']
        if 'new_builded_plugin_url' in d:
            o.new_builded_plugin_url = d['new_builded_plugin_url']
        if 'plugin_refs' in d:
            o.plugin_refs = d['plugin_refs']
        if 'sub_packages' in d:
            o.sub_packages = d['sub_packages']
        return o


