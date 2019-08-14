#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NextUrl import NextUrl


class ChildCertInfo(object):

    def __init__(self):
        self._child_id = None
        self._url = None

    @property
    def child_id(self):
        return self._child_id

    @child_id.setter
    def child_id(self, value):
        self._child_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if isinstance(value, NextUrl):
            self._url = value
        else:
            self._url = NextUrl.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.child_id:
            if hasattr(self.child_id, 'to_alipay_dict'):
                params['child_id'] = self.child_id.to_alipay_dict()
            else:
                params['child_id'] = self.child_id
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChildCertInfo()
        if 'child_id' in d:
            o.child_id = d['child_id']
        if 'url' in d:
            o.url = d['url']
        return o


