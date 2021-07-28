#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniAliminiabilityprodJsapiQueryModel(object):

    def __init__(self):
        self._bundle_id = None
        self._en_name = None
        self._instance_version = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniAliminiabilityprodJsapiQueryModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'en_name' in d:
            o.en_name = d['en_name']
        if 'instance_version' in d:
            o.instance_version = d['instance_version']
        return o


