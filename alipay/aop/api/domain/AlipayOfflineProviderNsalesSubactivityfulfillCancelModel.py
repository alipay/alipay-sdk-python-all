#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderNsalesSubactivityfulfillCancelModel(object):

    def __init__(self):
        self._sub_activity_id = None

    @property
    def sub_activity_id(self):
        return self._sub_activity_id

    @sub_activity_id.setter
    def sub_activity_id(self, value):
        self._sub_activity_id = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOfflineProviderNsalesSubactivityfulfillCancelModel()
        if 'sub_activity_id' in d:
            o.sub_activity_id = d['sub_activity_id']
        return o


