#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionTemplatebasedUploadModel(object):

    def __init__(self):
        self._app_version = None
        self._build_extra_info = None
        self._bundle_id = None
        self._inst_code = None
        self._mini_app_id = None
        self._template_bundle_id = None
        self._template_id = None
        self._template_version = None
        self._version_status = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def build_extra_info(self):
        return self._build_extra_info

    @build_extra_info.setter
    def build_extra_info(self, value):
        self._build_extra_info = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
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
    def template_bundle_id(self):
        return self._template_bundle_id

    @template_bundle_id.setter
    def template_bundle_id(self, value):
        self._template_bundle_id = value
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
    @property
    def version_status(self):
        return self._version_status

    @version_status.setter
    def version_status(self, value):
        self._version_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.build_extra_info:
            if hasattr(self.build_extra_info, 'to_alipay_dict'):
                params['build_extra_info'] = self.build_extra_info.to_alipay_dict()
            else:
                params['build_extra_info'] = self.build_extra_info
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
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
        if self.template_bundle_id:
            if hasattr(self.template_bundle_id, 'to_alipay_dict'):
                params['template_bundle_id'] = self.template_bundle_id.to_alipay_dict()
            else:
                params['template_bundle_id'] = self.template_bundle_id
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
        if self.version_status:
            if hasattr(self.version_status, 'to_alipay_dict'):
                params['version_status'] = self.version_status.to_alipay_dict()
            else:
                params['version_status'] = self.version_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionTemplatebasedUploadModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'build_extra_info' in d:
            o.build_extra_info = d['build_extra_info']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'template_bundle_id' in d:
            o.template_bundle_id = d['template_bundle_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_version' in d:
            o.template_version = d['template_version']
        if 'version_status' in d:
            o.version_status = d['version_status']
        return o


