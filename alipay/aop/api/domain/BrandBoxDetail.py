#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BoxDetail import BoxDetail


class BrandBoxDetail(object):

    def __init__(self):
        self._detail = None
        self._key = None

    @property
    def detail(self):
        return self._detail

    @detail.setter
    def detail(self, value):
        if isinstance(value, BoxDetail):
            self._detail = value
        else:
            self._detail = BoxDetail.from_alipay_dict(value)
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value


    def to_alipay_dict(self):
        params = dict()
        if self.detail:
            if hasattr(self.detail, 'to_alipay_dict'):
                params['detail'] = self.detail.to_alipay_dict()
            else:
                params['detail'] = self.detail
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BrandBoxDetail()
        if 'detail' in d:
            o.detail = d['detail']
        if 'key' in d:
            o.key = d['key']
        return o


