#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotDeliveryContentInfo(object):

    def __init__(self):
        self._activity_ids = None
        self._display_app_id = None

    @property
    def activity_ids(self):
        return self._activity_ids

    @activity_ids.setter
    def activity_ids(self, value):
        self._activity_ids = value
    @property
    def display_app_id(self):
        return self._display_app_id

    @display_app_id.setter
    def display_app_id(self, value):
        self._display_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_ids:
            if hasattr(self.activity_ids, 'to_alipay_dict'):
                params['activity_ids'] = self.activity_ids.to_alipay_dict()
            else:
                params['activity_ids'] = self.activity_ids
        if self.display_app_id:
            if hasattr(self.display_app_id, 'to_alipay_dict'):
                params['display_app_id'] = self.display_app_id.to_alipay_dict()
            else:
                params['display_app_id'] = self.display_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotDeliveryContentInfo()
        if 'activity_ids' in d:
            o.activity_ids = d['activity_ids']
        if 'display_app_id' in d:
            o.display_app_id = d['display_app_id']
        return o


