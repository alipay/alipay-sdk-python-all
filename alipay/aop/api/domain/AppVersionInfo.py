#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AppVersionInfo(object):

    def __init__(self):
        self._app_version = None
        self._base_audit = None
        self._bundle_id = None
        self._can_release = None
        self._create_time = None
        self._promote_audit = None
        self._version_description = None
        self._version_status = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def base_audit(self):
        return self._base_audit

    @base_audit.setter
    def base_audit(self, value):
        self._base_audit = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def can_release(self):
        return self._can_release

    @can_release.setter
    def can_release(self, value):
        self._can_release = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def promote_audit(self):
        return self._promote_audit

    @promote_audit.setter
    def promote_audit(self, value):
        self._promote_audit = value
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
        if self.base_audit:
            if hasattr(self.base_audit, 'to_alipay_dict'):
                params['base_audit'] = self.base_audit.to_alipay_dict()
            else:
                params['base_audit'] = self.base_audit
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.can_release:
            if hasattr(self.can_release, 'to_alipay_dict'):
                params['can_release'] = self.can_release.to_alipay_dict()
            else:
                params['can_release'] = self.can_release
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.promote_audit:
            if hasattr(self.promote_audit, 'to_alipay_dict'):
                params['promote_audit'] = self.promote_audit.to_alipay_dict()
            else:
                params['promote_audit'] = self.promote_audit
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
        if 'base_audit' in d:
            o.base_audit = d['base_audit']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'can_release' in d:
            o.can_release = d['can_release']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'promote_audit' in d:
            o.promote_audit = d['promote_audit']
        if 'version_description' in d:
            o.version_description = d['version_description']
        if 'version_status' in d:
            o.version_status = d['version_status']
        return o


