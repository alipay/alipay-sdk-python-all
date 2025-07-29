#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Doctor(object):

    def __init__(self):
        self._describe = None
        self._head = None
        self._link = None

    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value
    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value


    def to_alipay_dict(self):
        params = dict()
        if self.describe:
            if hasattr(self.describe, 'to_alipay_dict'):
                params['describe'] = self.describe.to_alipay_dict()
            else:
                params['describe'] = self.describe
        if self.head:
            if hasattr(self.head, 'to_alipay_dict'):
                params['head'] = self.head.to_alipay_dict()
            else:
                params['head'] = self.head
        if self.link:
            if hasattr(self.link, 'to_alipay_dict'):
                params['link'] = self.link.to_alipay_dict()
            else:
                params['link'] = self.link
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Doctor()
        if 'describe' in d:
            o.describe = d['describe']
        if 'head' in d:
            o.head = d['head']
        if 'link' in d:
            o.link = d['link']
        return o


