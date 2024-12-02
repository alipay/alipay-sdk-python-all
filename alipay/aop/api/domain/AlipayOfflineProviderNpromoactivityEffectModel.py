#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpromoactivityEffectModel(object):

    def __init__(self):
        self._activity_id = None
        self._biz_time = None
        self._dvc_sn = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def dvc_sn(self):
        return self._dvc_sn

    @dvc_sn.setter
    def dvc_sn(self, value):
        self._dvc_sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.dvc_sn:
            if hasattr(self.dvc_sn, 'to_alipay_dict'):
                params['dvc_sn'] = self.dvc_sn.to_alipay_dict()
            else:
                params['dvc_sn'] = self.dvc_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpromoactivityEffectModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'dvc_sn' in d:
            o.dvc_sn = d['dvc_sn']
        return o


