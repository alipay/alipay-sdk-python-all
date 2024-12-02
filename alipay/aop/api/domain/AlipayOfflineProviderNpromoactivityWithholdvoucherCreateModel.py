#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNpromoactivityWithholdvoucherCreateModel(object):

    def __init__(self):
        self._biz_time = None
        self._sub_activity_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def sub_activity_id(self):
        return self._sub_activity_id

    @sub_activity_id.setter
    def sub_activity_id(self, value):
        self._sub_activity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.sub_activity_id:
            if hasattr(self.sub_activity_id, 'to_alipay_dict'):
                params['sub_activity_id'] = self.sub_activity_id.to_alipay_dict()
            else:
                params['sub_activity_id'] = self.sub_activity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderNpromoactivityWithholdvoucherCreateModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'sub_activity_id' in d:
            o.sub_activity_id = d['sub_activity_id']
        return o


