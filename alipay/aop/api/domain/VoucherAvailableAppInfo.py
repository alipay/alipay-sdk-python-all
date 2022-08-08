#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherAvailableAppInfo(object):

    def __init__(self):
        self._available_app_ids = None

    @property
    def available_app_ids(self):
        return self._available_app_ids

    @available_app_ids.setter
    def available_app_ids(self, value):
        if isinstance(value, list):
            self._available_app_ids = list()
            for i in value:
                self._available_app_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.available_app_ids:
            if isinstance(self.available_app_ids, list):
                for i in range(0, len(self.available_app_ids)):
                    element = self.available_app_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.available_app_ids[i] = element.to_alipay_dict()
            if hasattr(self.available_app_ids, 'to_alipay_dict'):
                params['available_app_ids'] = self.available_app_ids.to_alipay_dict()
            else:
                params['available_app_ids'] = self.available_app_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherAvailableAppInfo()
        if 'available_app_ids' in d:
            o.available_app_ids = d['available_app_ids']
        return o


