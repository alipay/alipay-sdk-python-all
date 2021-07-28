#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniModelQueryModel(object):

    def __init__(self):
        self._app_info_modified = None
        self._app_version_modified = None
        self._deploy_package_modified = None
        self._deploy_window_modified = None
        self._inst_code = None
        self._load_test = None
        self._mini_app_id = None
        self._mini_app_version_modified = None

    @property
    def app_info_modified(self):
        return self._app_info_modified

    @app_info_modified.setter
    def app_info_modified(self, value):
        self._app_info_modified = value
    @property
    def app_version_modified(self):
        return self._app_version_modified

    @app_version_modified.setter
    def app_version_modified(self, value):
        self._app_version_modified = value
    @property
    def deploy_package_modified(self):
        return self._deploy_package_modified

    @deploy_package_modified.setter
    def deploy_package_modified(self, value):
        self._deploy_package_modified = value
    @property
    def deploy_window_modified(self):
        return self._deploy_window_modified

    @deploy_window_modified.setter
    def deploy_window_modified(self, value):
        self._deploy_window_modified = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def load_test(self):
        return self._load_test

    @load_test.setter
    def load_test(self, value):
        self._load_test = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_version_modified(self):
        return self._mini_app_version_modified

    @mini_app_version_modified.setter
    def mini_app_version_modified(self, value):
        self._mini_app_version_modified = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_info_modified:
            if hasattr(self.app_info_modified, 'to_alipay_dict'):
                params['app_info_modified'] = self.app_info_modified.to_alipay_dict()
            else:
                params['app_info_modified'] = self.app_info_modified
        if self.app_version_modified:
            if hasattr(self.app_version_modified, 'to_alipay_dict'):
                params['app_version_modified'] = self.app_version_modified.to_alipay_dict()
            else:
                params['app_version_modified'] = self.app_version_modified
        if self.deploy_package_modified:
            if hasattr(self.deploy_package_modified, 'to_alipay_dict'):
                params['deploy_package_modified'] = self.deploy_package_modified.to_alipay_dict()
            else:
                params['deploy_package_modified'] = self.deploy_package_modified
        if self.deploy_window_modified:
            if hasattr(self.deploy_window_modified, 'to_alipay_dict'):
                params['deploy_window_modified'] = self.deploy_window_modified.to_alipay_dict()
            else:
                params['deploy_window_modified'] = self.deploy_window_modified
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.load_test:
            if hasattr(self.load_test, 'to_alipay_dict'):
                params['load_test'] = self.load_test.to_alipay_dict()
            else:
                params['load_test'] = self.load_test
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_version_modified:
            if hasattr(self.mini_app_version_modified, 'to_alipay_dict'):
                params['mini_app_version_modified'] = self.mini_app_version_modified.to_alipay_dict()
            else:
                params['mini_app_version_modified'] = self.mini_app_version_modified
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniModelQueryModel()
        if 'app_info_modified' in d:
            o.app_info_modified = d['app_info_modified']
        if 'app_version_modified' in d:
            o.app_version_modified = d['app_version_modified']
        if 'deploy_package_modified' in d:
            o.deploy_package_modified = d['deploy_package_modified']
        if 'deploy_window_modified' in d:
            o.deploy_window_modified = d['deploy_window_modified']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'load_test' in d:
            o.load_test = d['load_test']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_version_modified' in d:
            o.mini_app_version_modified = d['mini_app_version_modified']
        return o


