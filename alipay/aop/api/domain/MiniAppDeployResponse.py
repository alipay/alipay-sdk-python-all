#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MiniAppDeployResponse(object):

    def __init__(self):
        self._android_client_max = None
        self._android_client_min = None
        self._app_version = None
        self._bundle_id = None
        self._deploy_version = None
        self._gmt_create = None
        self._gmt_modified = None
        self._ios_client_max = None
        self._ios_client_min = None
        self._mini_app_id = None
        self._package_size = None
        self._status = None

    @property
    def android_client_max(self):
        return self._android_client_max

    @android_client_max.setter
    def android_client_max(self, value):
        self._android_client_max = value
    @property
    def android_client_min(self):
        return self._android_client_min

    @android_client_min.setter
    def android_client_min(self, value):
        self._android_client_min = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def deploy_version(self):
        return self._deploy_version

    @deploy_version.setter
    def deploy_version(self, value):
        self._deploy_version = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def ios_client_max(self):
        return self._ios_client_max

    @ios_client_max.setter
    def ios_client_max(self, value):
        self._ios_client_max = value
    @property
    def ios_client_min(self):
        return self._ios_client_min

    @ios_client_min.setter
    def ios_client_min(self, value):
        self._ios_client_min = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def package_size(self):
        return self._package_size

    @package_size.setter
    def package_size(self, value):
        self._package_size = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.android_client_max:
            if hasattr(self.android_client_max, 'to_alipay_dict'):
                params['android_client_max'] = self.android_client_max.to_alipay_dict()
            else:
                params['android_client_max'] = self.android_client_max
        if self.android_client_min:
            if hasattr(self.android_client_min, 'to_alipay_dict'):
                params['android_client_min'] = self.android_client_min.to_alipay_dict()
            else:
                params['android_client_min'] = self.android_client_min
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.deploy_version:
            if hasattr(self.deploy_version, 'to_alipay_dict'):
                params['deploy_version'] = self.deploy_version.to_alipay_dict()
            else:
                params['deploy_version'] = self.deploy_version
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.ios_client_max:
            if hasattr(self.ios_client_max, 'to_alipay_dict'):
                params['ios_client_max'] = self.ios_client_max.to_alipay_dict()
            else:
                params['ios_client_max'] = self.ios_client_max
        if self.ios_client_min:
            if hasattr(self.ios_client_min, 'to_alipay_dict'):
                params['ios_client_min'] = self.ios_client_min.to_alipay_dict()
            else:
                params['ios_client_min'] = self.ios_client_min
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.package_size:
            if hasattr(self.package_size, 'to_alipay_dict'):
                params['package_size'] = self.package_size.to_alipay_dict()
            else:
                params['package_size'] = self.package_size
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MiniAppDeployResponse()
        if 'android_client_max' in d:
            o.android_client_max = d['android_client_max']
        if 'android_client_min' in d:
            o.android_client_min = d['android_client_min']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'deploy_version' in d:
            o.deploy_version = d['deploy_version']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'ios_client_max' in d:
            o.ios_client_max = d['ios_client_max']
        if 'ios_client_min' in d:
            o.ios_client_min = d['ios_client_min']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'package_size' in d:
            o.package_size = d['package_size']
        if 'status' in d:
            o.status = d['status']
        return o


