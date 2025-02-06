#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNsalesActivityEffectModel(object):

    def __init__(self):
        self._activity_dvc_sn = None
        self._activity_id = None

    @property
    def activity_dvc_sn(self):
        return self._activity_dvc_sn

    @activity_dvc_sn.setter
    def activity_dvc_sn(self, value):
        self._activity_dvc_sn = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_dvc_sn:
            if hasattr(self.activity_dvc_sn, 'to_alipay_dict'):
                params['activity_dvc_sn'] = self.activity_dvc_sn.to_alipay_dict()
            else:
                params['activity_dvc_sn'] = self.activity_dvc_sn
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNsalesActivityEffectModel()
        if 'activity_dvc_sn' in d:
            o.activity_dvc_sn = d['activity_dvc_sn']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        return o


