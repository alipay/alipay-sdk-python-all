#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhenChenDetail(object):

    def __init__(self):
        self._zhenchenstr = None
        self._zhenchentime = None

    @property
    def zhenchenstr(self):
        return self._zhenchenstr

    @zhenchenstr.setter
    def zhenchenstr(self, value):
        self._zhenchenstr = value
    @property
    def zhenchentime(self):
        return self._zhenchentime

    @zhenchentime.setter
    def zhenchentime(self, value):
        self._zhenchentime = value


    def to_alipay_dict(self):
        params = dict()
        if self.zhenchenstr:
            if hasattr(self.zhenchenstr, 'to_alipay_dict'):
                params['zhenchenstr'] = self.zhenchenstr.to_alipay_dict()
            else:
                params['zhenchenstr'] = self.zhenchenstr
        if self.zhenchentime:
            if hasattr(self.zhenchentime, 'to_alipay_dict'):
                params['zhenchentime'] = self.zhenchentime.to_alipay_dict()
            else:
                params['zhenchentime'] = self.zhenchentime
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhenChenDetail()
        if 'zhenchenstr' in d:
            o.zhenchenstr = d['zhenchenstr']
        if 'zhenchentime' in d:
            o.zhenchentime = d['zhenchentime']
        return o


