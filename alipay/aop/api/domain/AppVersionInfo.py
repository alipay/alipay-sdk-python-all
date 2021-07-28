#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppVersionInfo(object):

    def __init__(self):
        self._app_version = None
        self._bundle_id = None
        self._create_time = None
        self._version_description = None
        self._version_status = None

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
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def version_description(self):
        return self._version_description

    @version_description.setter
    def version_description(self, value):
        self._version_description = value
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
        if self.version_description:
            if hasattr(self.version_description, 'to_alipay_dict'):
                params['version_description'] = self.version_description.to_alipay_dict()
            else:
                params['version_description'] = self.version_description
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
        o = AppVersionInfo()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'version_description' in d:
            o.version_description = d['version_description']
        if 'version_status' in d:
            o.version_status = d['version_status']
        return o


