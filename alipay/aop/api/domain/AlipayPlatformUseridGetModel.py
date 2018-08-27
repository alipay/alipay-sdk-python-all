#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPlatformUseridGetModel(object):

    def __init__(self):
        self._open_ids = None

    @property
    def open_ids(self):
        return self._open_ids

    @open_ids.setter
    def open_ids(self, value):
        if isinstance(value, list):
            self._open_ids = list()
            for i in value:
                self._open_ids.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.open_ids:
            if isinstance(self.open_ids, list):
                for i in range(0, len(self.open_ids)):
                    element = self.open_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_ids[i] = element.to_alipay_dict()
            if hasattr(self.open_ids, 'to_alipay_dict'):
                params['open_ids'] = self.open_ids.to_alipay_dict()
            else:
                params['open_ids'] = self.open_ids
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPlatformUseridGetModel()
        if 'open_ids' in d:
            o.open_ids = d['open_ids']
        return o


