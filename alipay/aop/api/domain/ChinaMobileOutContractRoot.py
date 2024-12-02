#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChinaMobileOutBody import ChinaMobileOutBody
from alipay.aop.api.domain.ChinaMobileHead import ChinaMobileHead


class ChinaMobileOutContractRoot(object):

    def __init__(self):
        self._body = None
        self._head = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        if isinstance(value, ChinaMobileOutBody):
            self._body = value
        else:
            self._body = ChinaMobileOutBody.from_alipay_dict(value)
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        if isinstance(value, ChinaMobileHead):
            self._head = value
        else:
            self._head = ChinaMobileHead.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.head:
            if hasattr(self.head, 'to_alipay_dict'):
                params['head'] = self.head.to_alipay_dict()
            else:
                params['head'] = self.head
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChinaMobileOutContractRoot()
        if 'body' in d:
            o.body = d['body']
        if 'head' in d:
            o.head = d['head']
        return o


