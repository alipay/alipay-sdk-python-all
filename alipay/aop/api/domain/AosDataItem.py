#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AosDataItem(object):

    def __init__(self):
        self._id = None
        self._meta = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, value):
        self._meta = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.meta:
            if hasattr(self.meta, 'to_alipay_dict'):
                params['meta'] = self.meta.to_alipay_dict()
            else:
                params['meta'] = self.meta
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AosDataItem()
        if 'id' in d:
            o.id = d['id']
        if 'meta' in d:
            o.meta = d['meta']
        return o


