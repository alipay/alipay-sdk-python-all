#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAgentVersionAuditModel(object):

    def __init__(self):
        self._app_version = None
        self._bundle_id = None
        self._bundle_ids = None

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
    def bundle_ids(self):
        return self._bundle_ids

    @bundle_ids.setter
    def bundle_ids(self, value):
        if isinstance(value, list):
            self._bundle_ids = list()
            for i in value:
                self._bundle_ids.append(i)


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
        if self.bundle_ids:
            if isinstance(self.bundle_ids, list):
                for i in range(0, len(self.bundle_ids)):
                    element = self.bundle_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bundle_ids[i] = element.to_alipay_dict()
            if hasattr(self.bundle_ids, 'to_alipay_dict'):
                params['bundle_ids'] = self.bundle_ids.to_alipay_dict()
            else:
                params['bundle_ids'] = self.bundle_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAgentVersionAuditModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'bundle_ids' in d:
            o.bundle_ids = d['bundle_ids']
        return o


