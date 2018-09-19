#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceMetainfoSyncModel(object):

    def __init__(self):
        self._meta_info = None

    @property
    def meta_info(self):
        return self._meta_info

    @meta_info.setter
    def meta_info(self, value):
        self._meta_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.meta_info:
            if hasattr(self.meta_info, 'to_alipay_dict'):
                params['meta_info'] = self.meta_info.to_alipay_dict()
            else:
                params['meta_info'] = self.meta_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceMetainfoSyncModel()
        if 'meta_info' in d:
            o.meta_info = d['meta_info']
        return o


