#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenAppDeployPackageVO(object):

    def __init__(self):
        self._deploy_version = None
        self._mini_app_id = None
        self._package_url = None
        self._plugin_url = None

    @property
    def deploy_version(self):
        return self._deploy_version

    @deploy_version.setter
    def deploy_version(self, value):
        self._deploy_version = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.deploy_version:
            if hasattr(self.deploy_version, 'to_alipay_dict'):
                params['deploy_version'] = self.deploy_version.to_alipay_dict()
            else:
                params['deploy_version'] = self.deploy_version
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenAppDeployPackageVO()
        if 'deploy_version' in d:
            o.deploy_version = d['deploy_version']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'package_url' in d:
            o.package_url = d['package_url']
        if 'plugin_url' in d:
            o.plugin_url = d['plugin_url']
        return o


