#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAliminiabilityprodJsapiModifyModel(object):

    def __init__(self):
        self._appx_min_version = None
        self._bundle_id = None
        self._bundle_min_version = None
        self._demo_url = None
        self._en_name = None
        self._instance_version = None
        self._owner = None
        self._status = None

    @property
    def appx_min_version(self):
        return self._appx_min_version

    @appx_min_version.setter
    def appx_min_version(self, value):
        self._appx_min_version = value
    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def bundle_min_version(self):
        return self._bundle_min_version

    @bundle_min_version.setter
    def bundle_min_version(self, value):
        self._bundle_min_version = value
    @property
    def demo_url(self):
        return self._demo_url

    @demo_url.setter
    def demo_url(self, value):
        self._demo_url = value
    @property
    def en_name(self):
        return self._en_name

    @en_name.setter
    def en_name(self, value):
        self._en_name = value
    @property
    def instance_version(self):
        return self._instance_version

    @instance_version.setter
    def instance_version(self, value):
        self._instance_version = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.appx_min_version:
            if hasattr(self.appx_min_version, 'to_alipay_dict'):
                params['appx_min_version'] = self.appx_min_version.to_alipay_dict()
            else:
                params['appx_min_version'] = self.appx_min_version
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
        if self.bundle_min_version:
            if hasattr(self.bundle_min_version, 'to_alipay_dict'):
                params['bundle_min_version'] = self.bundle_min_version.to_alipay_dict()
            else:
                params['bundle_min_version'] = self.bundle_min_version
        if self.demo_url:
            if hasattr(self.demo_url, 'to_alipay_dict'):
                params['demo_url'] = self.demo_url.to_alipay_dict()
            else:
                params['demo_url'] = self.demo_url
        if self.en_name:
            if hasattr(self.en_name, 'to_alipay_dict'):
                params['en_name'] = self.en_name.to_alipay_dict()
            else:
                params['en_name'] = self.en_name
        if self.instance_version:
            if hasattr(self.instance_version, 'to_alipay_dict'):
                params['instance_version'] = self.instance_version.to_alipay_dict()
            else:
                params['instance_version'] = self.instance_version
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
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
        o = AlipayOpenMiniAliminiabilityprodJsapiModifyModel()
        if 'appx_min_version' in d:
            o.appx_min_version = d['appx_min_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'bundle_min_version' in d:
            o.bundle_min_version = d['bundle_min_version']
        if 'demo_url' in d:
            o.demo_url = d['demo_url']
        if 'en_name' in d:
            o.en_name = d['en_name']
        if 'instance_version' in d:
            o.instance_version = d['instance_version']
        if 'owner' in d:
            o.owner = d['owner']
        if 'status' in d:
            o.status = d['status']
        return o


