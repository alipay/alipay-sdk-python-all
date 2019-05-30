#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniInnerversionUploadstatusQueryModel(object):

    def __init__(self):
        self._build_package_id = None
        self._build_version = None
        self._bundle_id = None
        self._inst_code = None
        self._mini_app_id = None

    @property
    def build_package_id(self):
        return self._build_package_id

    @build_package_id.setter
    def build_package_id(self, value):
        self._build_package_id = value
    @property
    def build_version(self):
        return self._build_version

    @build_version.setter
    def build_version(self, value):
        self._build_version = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.build_package_id:
            if hasattr(self.build_package_id, 'to_alipay_dict'):
                params['build_package_id'] = self.build_package_id.to_alipay_dict()
            else:
                params['build_package_id'] = self.build_package_id
        if self.build_version:
            if hasattr(self.build_version, 'to_alipay_dict'):
                params['build_version'] = self.build_version.to_alipay_dict()
            else:
                params['build_version'] = self.build_version
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniInnerversionUploadstatusQueryModel()
        if 'build_package_id' in d:
            o.build_package_id = d['build_package_id']
        if 'build_version' in d:
            o.build_version = d['build_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        return o


