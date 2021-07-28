#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MiniAppPluginReference import MiniAppPluginReference


class AlipayOpenMiniInnerversionUploadModel(object):

    def __init__(self):
        self._app_origin = None
        self._build_app_type = None
        self._build_extra_info = None
        self._build_extra_mini_project_config = None
        self._build_js_permission = None
        self._build_main_url = None
        self._build_max_android_client_version = None
        self._build_max_ios_client_version = None
        self._build_min_android_client_version = None
        self._build_min_ios_client_version = None
        self._build_package_md_5 = None
        self._build_package_name = None
        self._build_package_stream = None
        self._build_qcloud_info = None
        self._build_signed_pkg_url = None
        self._build_source_pkg_size = None
        self._build_source_pkg_url = None
        self._build_sub_url = None
        self._build_version = None
        self._builded_package_size = None
        self._builded_package_url = None
        self._bundle_id = None
        self._client_type = None
        self._inst_code = None
        self._mini_app_id = None
        self._plugin_refs = None

    @property
    def app_origin(self):
        return self._app_origin

    @app_origin.setter
    def app_origin(self, value):
        self._app_origin = value
    @property
    def build_app_type(self):
        return self._build_app_type

    @build_app_type.setter
    def build_app_type(self, value):
        self._build_app_type = value
    @property
    def build_extra_info(self):
        return self._build_extra_info

    @build_extra_info.setter
    def build_extra_info(self, value):
        self._build_extra_info = value
    @property
    def build_extra_mini_project_config(self):
        return self._build_extra_mini_project_config

    @build_extra_mini_project_config.setter
    def build_extra_mini_project_config(self, value):
        self._build_extra_mini_project_config = value
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
    def build_max_android_client_version(self):
        return self._build_max_android_client_version

    @build_max_android_client_version.setter
    def build_max_android_client_version(self, value):
        self._build_max_android_client_version = value
    @property
    def build_max_ios_client_version(self):
        return self._build_max_ios_client_version

    @build_max_ios_client_version.setter
    def build_max_ios_client_version(self, value):
        self._build_max_ios_client_version = value
    @property
    def build_min_android_client_version(self):
        return self._build_min_android_client_version

    @build_min_android_client_version.setter
    def build_min_android_client_version(self, value):
        self._build_min_android_client_version = value
    @property
    def build_min_ios_client_version(self):
        return self._build_min_ios_client_version

    @build_min_ios_client_version.setter
    def build_min_ios_client_version(self, value):
        self._build_min_ios_client_version = value
    @property
    def build_package_md_5(self):
        return self._build_package_md_5

    @build_package_md_5.setter
    def build_package_md_5(self, value):
        self._build_package_md_5 = value
    @property
    def build_package_name(self):
        return self._build_package_name

    @build_package_name.setter
    def build_package_name(self, value):
        self._build_package_name = value
    @property
    def build_package_stream(self):
        return self._build_package_stream

    @build_package_stream.setter
    def build_package_stream(self, value):
        self._build_package_stream = value
    @property
    def build_qcloud_info(self):
        return self._build_qcloud_info

    @build_qcloud_info.setter
    def build_qcloud_info(self, value):
        self._build_qcloud_info = value
    @property
    def build_signed_pkg_url(self):
        return self._build_signed_pkg_url

    @build_signed_pkg_url.setter
    def build_signed_pkg_url(self, value):
        self._build_signed_pkg_url = value
    @property
    def build_source_pkg_size(self):
        return self._build_source_pkg_size

    @build_source_pkg_size.setter
    def build_source_pkg_size(self, value):
        self._build_source_pkg_size = value
    @property
    def build_source_pkg_url(self):
        return self._build_source_pkg_url

    @build_source_pkg_url.setter
    def build_source_pkg_url(self, value):
        self._build_source_pkg_url = value
    @property
    def build_sub_url(self):
        return self._build_sub_url

    @build_sub_url.setter
    def build_sub_url(self, value):
        self._build_sub_url = value
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
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def client_type(self):
        return self._client_type

    @client_type.setter
    def client_type(self, value):
        self._client_type = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.app_origin:
            if hasattr(self.app_origin, 'to_alipay_dict'):
                params['app_origin'] = self.app_origin.to_alipay_dict()
            else:
                params['app_origin'] = self.app_origin
        if self.build_app_type:
            if hasattr(self.build_app_type, 'to_alipay_dict'):
                params['build_app_type'] = self.build_app_type.to_alipay_dict()
            else:
                params['build_app_type'] = self.build_app_type
        if self.build_extra_info:
            if hasattr(self.build_extra_info, 'to_alipay_dict'):
                params['build_extra_info'] = self.build_extra_info.to_alipay_dict()
            else:
                params['build_extra_info'] = self.build_extra_info
        if self.build_extra_mini_project_config:
            if hasattr(self.build_extra_mini_project_config, 'to_alipay_dict'):
                params['build_extra_mini_project_config'] = self.build_extra_mini_project_config.to_alipay_dict()
            else:
                params['build_extra_mini_project_config'] = self.build_extra_mini_project_config
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
        if self.build_max_android_client_version:
            if hasattr(self.build_max_android_client_version, 'to_alipay_dict'):
                params['build_max_android_client_version'] = self.build_max_android_client_version.to_alipay_dict()
            else:
                params['build_max_android_client_version'] = self.build_max_android_client_version
        if self.build_max_ios_client_version:
            if hasattr(self.build_max_ios_client_version, 'to_alipay_dict'):
                params['build_max_ios_client_version'] = self.build_max_ios_client_version.to_alipay_dict()
            else:
                params['build_max_ios_client_version'] = self.build_max_ios_client_version
        if self.build_min_android_client_version:
            if hasattr(self.build_min_android_client_version, 'to_alipay_dict'):
                params['build_min_android_client_version'] = self.build_min_android_client_version.to_alipay_dict()
            else:
                params['build_min_android_client_version'] = self.build_min_android_client_version
        if self.build_min_ios_client_version:
            if hasattr(self.build_min_ios_client_version, 'to_alipay_dict'):
                params['build_min_ios_client_version'] = self.build_min_ios_client_version.to_alipay_dict()
            else:
                params['build_min_ios_client_version'] = self.build_min_ios_client_version
        if self.build_package_md_5:
            if hasattr(self.build_package_md_5, 'to_alipay_dict'):
                params['build_package_md_5'] = self.build_package_md_5.to_alipay_dict()
            else:
                params['build_package_md_5'] = self.build_package_md_5
        if self.build_package_name:
            if hasattr(self.build_package_name, 'to_alipay_dict'):
                params['build_package_name'] = self.build_package_name.to_alipay_dict()
            else:
                params['build_package_name'] = self.build_package_name
        if self.build_package_stream:
            if hasattr(self.build_package_stream, 'to_alipay_dict'):
                params['build_package_stream'] = self.build_package_stream.to_alipay_dict()
            else:
                params['build_package_stream'] = self.build_package_stream
        if self.build_qcloud_info:
            if hasattr(self.build_qcloud_info, 'to_alipay_dict'):
                params['build_qcloud_info'] = self.build_qcloud_info.to_alipay_dict()
            else:
                params['build_qcloud_info'] = self.build_qcloud_info
        if self.build_signed_pkg_url:
            if hasattr(self.build_signed_pkg_url, 'to_alipay_dict'):
                params['build_signed_pkg_url'] = self.build_signed_pkg_url.to_alipay_dict()
            else:
                params['build_signed_pkg_url'] = self.build_signed_pkg_url
        if self.build_source_pkg_size:
            if hasattr(self.build_source_pkg_size, 'to_alipay_dict'):
                params['build_source_pkg_size'] = self.build_source_pkg_size.to_alipay_dict()
            else:
                params['build_source_pkg_size'] = self.build_source_pkg_size
        if self.build_source_pkg_url:
            if hasattr(self.build_source_pkg_url, 'to_alipay_dict'):
                params['build_source_pkg_url'] = self.build_source_pkg_url.to_alipay_dict()
            else:
                params['build_source_pkg_url'] = self.build_source_pkg_url
        if self.build_sub_url:
            if hasattr(self.build_sub_url, 'to_alipay_dict'):
                params['build_sub_url'] = self.build_sub_url.to_alipay_dict()
            else:
                params['build_sub_url'] = self.build_sub_url
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
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.client_type:
            if hasattr(self.client_type, 'to_alipay_dict'):
                params['client_type'] = self.client_type.to_alipay_dict()
            else:
                params['client_type'] = self.client_type
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionUploadModel()
        if 'app_origin' in d:
            o.app_origin = d['app_origin']
        if 'build_app_type' in d:
            o.build_app_type = d['build_app_type']
        if 'build_extra_info' in d:
            o.build_extra_info = d['build_extra_info']
        if 'build_extra_mini_project_config' in d:
            o.build_extra_mini_project_config = d['build_extra_mini_project_config']
        if 'build_js_permission' in d:
            o.build_js_permission = d['build_js_permission']
        if 'build_main_url' in d:
            o.build_main_url = d['build_main_url']
        if 'build_max_android_client_version' in d:
            o.build_max_android_client_version = d['build_max_android_client_version']
        if 'build_max_ios_client_version' in d:
            o.build_max_ios_client_version = d['build_max_ios_client_version']
        if 'build_min_android_client_version' in d:
            o.build_min_android_client_version = d['build_min_android_client_version']
        if 'build_min_ios_client_version' in d:
            o.build_min_ios_client_version = d['build_min_ios_client_version']
        if 'build_package_md_5' in d:
            o.build_package_md_5 = d['build_package_md_5']
        if 'build_package_name' in d:
            o.build_package_name = d['build_package_name']
        if 'build_package_stream' in d:
            o.build_package_stream = d['build_package_stream']
        if 'build_qcloud_info' in d:
            o.build_qcloud_info = d['build_qcloud_info']
        if 'build_signed_pkg_url' in d:
            o.build_signed_pkg_url = d['build_signed_pkg_url']
        if 'build_source_pkg_size' in d:
            o.build_source_pkg_size = d['build_source_pkg_size']
        if 'build_source_pkg_url' in d:
            o.build_source_pkg_url = d['build_source_pkg_url']
        if 'build_sub_url' in d:
            o.build_sub_url = d['build_sub_url']
        if 'build_version' in d:
            o.build_version = d['build_version']
        if 'builded_package_size' in d:
            o.builded_package_size = d['builded_package_size']
        if 'builded_package_url' in d:
            o.builded_package_url = d['builded_package_url']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'client_type' in d:
            o.client_type = d['client_type']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'plugin_refs' in d:
            o.plugin_refs = d['plugin_refs']
        return o


