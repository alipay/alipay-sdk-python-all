#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppVersionBaseInfo(object):

    def __init__(self):
        self._app_version = None
        self._build_source = None
        self._bundle_id = None
        self._create_time = None
        self._description = None
        self._ext_json = None
        self._gmt_modified = None
        self._gray_start_time = None
        self._inst_code = None
        self._mini_app_id = None
        self._offline_time = None
        self._package_url = None
        self._plugin_url = None
        self._rollback_time = None
        self._shelf_time = None
        self._status = None
        self._sub_status = None
        self._template_extra = None
        self._template_id = None
        self._template_version = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def build_source(self):
        return self._build_source

    @build_source.setter
    def build_source(self, value):
        self._build_source = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def ext_json(self):
        return self._ext_json

    @ext_json.setter
    def ext_json(self, value):
        self._ext_json = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def gray_start_time(self):
        return self._gray_start_time

    @gray_start_time.setter
    def gray_start_time(self, value):
        self._gray_start_time = value
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
    def offline_time(self):
        return self._offline_time

    @offline_time.setter
    def offline_time(self, value):
        self._offline_time = value
    @property
    def package_url(self):
        return self._package_url

    @package_url.setter
    def package_url(self, value):
        self._package_url = value
    @property
    def plugin_url(self):
        return self._plugin_url

    @plugin_url.setter
    def plugin_url(self, value):
        self._plugin_url = value
    @property
    def rollback_time(self):
        return self._rollback_time

    @rollback_time.setter
    def rollback_time(self, value):
        self._rollback_time = value
    @property
    def shelf_time(self):
        return self._shelf_time

    @shelf_time.setter
    def shelf_time(self, value):
        self._shelf_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_status(self):
        return self._sub_status

    @sub_status.setter
    def sub_status(self, value):
        self._sub_status = value
    @property
    def template_extra(self):
        return self._template_extra

    @template_extra.setter
    def template_extra(self, value):
        self._template_extra = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_version(self):
        return self._template_version

    @template_version.setter
    def template_version(self, value):
        self._template_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.build_source:
            if hasattr(self.build_source, 'to_alipay_dict'):
                params['build_source'] = self.build_source.to_alipay_dict()
            else:
                params['build_source'] = self.build_source
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.ext_json:
            if hasattr(self.ext_json, 'to_alipay_dict'):
                params['ext_json'] = self.ext_json.to_alipay_dict()
            else:
                params['ext_json'] = self.ext_json
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.gray_start_time:
            if hasattr(self.gray_start_time, 'to_alipay_dict'):
                params['gray_start_time'] = self.gray_start_time.to_alipay_dict()
            else:
                params['gray_start_time'] = self.gray_start_time
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
        if self.offline_time:
            if hasattr(self.offline_time, 'to_alipay_dict'):
                params['offline_time'] = self.offline_time.to_alipay_dict()
            else:
                params['offline_time'] = self.offline_time
        if self.package_url:
            if hasattr(self.package_url, 'to_alipay_dict'):
                params['package_url'] = self.package_url.to_alipay_dict()
            else:
                params['package_url'] = self.package_url
        if self.plugin_url:
            if hasattr(self.plugin_url, 'to_alipay_dict'):
                params['plugin_url'] = self.plugin_url.to_alipay_dict()
            else:
                params['plugin_url'] = self.plugin_url
        if self.rollback_time:
            if hasattr(self.rollback_time, 'to_alipay_dict'):
                params['rollback_time'] = self.rollback_time.to_alipay_dict()
            else:
                params['rollback_time'] = self.rollback_time
        if self.shelf_time:
            if hasattr(self.shelf_time, 'to_alipay_dict'):
                params['shelf_time'] = self.shelf_time.to_alipay_dict()
            else:
                params['shelf_time'] = self.shelf_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_status:
            if hasattr(self.sub_status, 'to_alipay_dict'):
                params['sub_status'] = self.sub_status.to_alipay_dict()
            else:
                params['sub_status'] = self.sub_status
        if self.template_extra:
            if hasattr(self.template_extra, 'to_alipay_dict'):
                params['template_extra'] = self.template_extra.to_alipay_dict()
            else:
                params['template_extra'] = self.template_extra
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_version:
            if hasattr(self.template_version, 'to_alipay_dict'):
                params['template_version'] = self.template_version.to_alipay_dict()
            else:
                params['template_version'] = self.template_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppVersionBaseInfo()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'build_source' in d:
            o.build_source = d['build_source']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'description' in d:
            o.description = d['description']
        if 'ext_json' in d:
            o.ext_json = d['ext_json']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'gray_start_time' in d:
            o.gray_start_time = d['gray_start_time']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'offline_time' in d:
            o.offline_time = d['offline_time']
        if 'package_url' in d:
            o.package_url = d['package_url']
        if 'plugin_url' in d:
            o.plugin_url = d['plugin_url']
        if 'rollback_time' in d:
            o.rollback_time = d['rollback_time']
        if 'shelf_time' in d:
            o.shelf_time = d['shelf_time']
        if 'status' in d:
            o.status = d['status']
        if 'sub_status' in d:
            o.sub_status = d['sub_status']
        if 'template_extra' in d:
            o.template_extra = d['template_extra']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_version' in d:
            o.template_version = d['template_version']
        return o


