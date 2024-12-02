#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpromoactivityDeviceModifyModel(object):

    def __init__(self):
        self._activity_id = None
        self._biz_time = None
        self._source_dvc_sn = None
        self._target_dvc_sn = None

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
    def source_dvc_sn(self):
        return self._source_dvc_sn

    @source_dvc_sn.setter
    def source_dvc_sn(self, value):
        self._source_dvc_sn = value
    @property
    def target_dvc_sn(self):
        return self._target_dvc_sn

    @target_dvc_sn.setter
    def target_dvc_sn(self, value):
        self._target_dvc_sn = value


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
        if self.source_dvc_sn:
            if hasattr(self.source_dvc_sn, 'to_alipay_dict'):
                params['source_dvc_sn'] = self.source_dvc_sn.to_alipay_dict()
            else:
                params['source_dvc_sn'] = self.source_dvc_sn
        if self.target_dvc_sn:
            if hasattr(self.target_dvc_sn, 'to_alipay_dict'):
                params['target_dvc_sn'] = self.target_dvc_sn.to_alipay_dict()
            else:
                params['target_dvc_sn'] = self.target_dvc_sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpromoactivityDeviceModifyModel()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'source_dvc_sn' in d:
            o.source_dvc_sn = d['source_dvc_sn']
        if 'target_dvc_sn' in d:
            o.target_dvc_sn = d['target_dvc_sn']
        return o


