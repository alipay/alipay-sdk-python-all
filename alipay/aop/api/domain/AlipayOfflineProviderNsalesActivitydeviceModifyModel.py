#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNsalesActivitydeviceModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._source_sn = None
        self._target_sn = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def source_sn(self):
        return self._source_sn

    @source_sn.setter
    def source_sn(self, value):
        self._source_sn = value
    @property
    def target_sn(self):
        return self._target_sn

    @target_sn.setter
    def target_sn(self, value):
        self._target_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.source_sn:
            if hasattr(self.source_sn, 'to_alipay_dict'):
                params['source_sn'] = self.source_sn.to_alipay_dict()
            else:
                params['source_sn'] = self.source_sn
        if self.target_sn:
            if hasattr(self.target_sn, 'to_alipay_dict'):
                params['target_sn'] = self.target_sn.to_alipay_dict()
            else:
                params['target_sn'] = self.target_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNsalesActivitydeviceModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'source_sn' in d:
            o.source_sn = d['source_sn']
        if 'target_sn' in d:
            o.target_sn = d['target_sn']
        return o


