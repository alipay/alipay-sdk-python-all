#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenAssetPublishConsultResult(object):

    def __init__(self):
        self._asset_id = None
        self._asset_info = None
        self._entity_id = None
        self._passed = None
        self._status = None

    @property
    def asset_id(self):
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        self._asset_id = value
    @property
    def asset_info(self):
        return self._asset_info

    @asset_info.setter
    def asset_info(self, value):
        self._asset_info = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value
    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_id:
            if hasattr(self.asset_id, 'to_alipay_dict'):
                params['asset_id'] = self.asset_id.to_alipay_dict()
            else:
                params['asset_id'] = self.asset_id
        if self.asset_info:
            if hasattr(self.asset_info, 'to_alipay_dict'):
                params['asset_info'] = self.asset_info.to_alipay_dict()
            else:
                params['asset_info'] = self.asset_info
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        if self.passed:
            if hasattr(self.passed, 'to_alipay_dict'):
                params['passed'] = self.passed.to_alipay_dict()
            else:
                params['passed'] = self.passed
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
        o = OpenAssetPublishConsultResult()
        if 'asset_id' in d:
            o.asset_id = d['asset_id']
        if 'asset_info' in d:
            o.asset_info = d['asset_info']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        if 'passed' in d:
            o.passed = d['passed']
        if 'status' in d:
            o.status = d['status']
        return o


