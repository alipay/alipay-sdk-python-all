#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniVersionListQueryModel(object):

    def __init__(self):
        self._bundle_id = None
        self._version_status = None

    @property
    def bundle_id(self):
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, value):
        self._bundle_id = value
    @property
    def version_status(self):
        return self._version_status

    @version_status.setter
    def version_status(self, value):
        self._version_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.bundle_id:
            if hasattr(self.bundle_id, 'to_alipay_dict'):
                params['bundle_id'] = self.bundle_id.to_alipay_dict()
            else:
                params['bundle_id'] = self.bundle_id
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
        o = AlipayOpenMiniVersionListQueryModel()
        if 'bundle_id' in d:
            o.bundle_id = d['bundle_id']
        if 'version_status' in d:
            o.version_status = d['version_status']
        return o


