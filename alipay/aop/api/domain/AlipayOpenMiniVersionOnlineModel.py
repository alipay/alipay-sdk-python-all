#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniVersionOnlineModel(object):

    def __init__(self):
        self._app_version = None
        self._bundle_id = None
        self._downgrade = None

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
    def downgrade(self):
        return self._downgrade

    @downgrade.setter
    def downgrade(self, value):
        self._downgrade = value


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
        if self.downgrade:
            if hasattr(self.downgrade, 'to_alipay_dict'):
                params['downgrade'] = self.downgrade.to_alipay_dict()
            else:
                params['downgrade'] = self.downgrade
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniVersionOnlineModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'downgrade' in d:
            o.downgrade = d['downgrade']
        return o


