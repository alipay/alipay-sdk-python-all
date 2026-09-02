#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ActivitySyncItem import ActivitySyncItem


class AlipayOfflineMarketActivityProductSyncModel(object):

    def __init__(self):
        self._activities = None

    @property
    def activities(self):
        return self._activities

    @activities.setter
    def activities(self, value):
        if isinstance(value, list):
            self._activities = list()
            for i in value:
                if isinstance(i, ActivitySyncItem):
                    self._activities.append(i)
                else:
                    self._activities.append(ActivitySyncItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.activities:
            if isinstance(self.activities, list):
                for i in range(0, len(self.activities)):
                    element = self.activities[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activities[i] = element.to_alipay_dict()
            if hasattr(self.activities, 'to_alipay_dict'):
                params['activities'] = self.activities.to_alipay_dict()
            else:
                params['activities'] = self.activities
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketActivityProductSyncModel()
        if 'activities' in d:
            o.activities = d['activities']
        return o


