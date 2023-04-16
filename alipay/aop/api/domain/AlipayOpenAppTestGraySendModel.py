#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppTestGraySendModel(object):

    def __init__(self):
        self._oid = None
        self._pid = None
        self._tid = None

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, value):
        self._tid = value


    def to_alipay_dict(self):
        params = dict()
        if self.oid:
            if hasattr(self.oid, 'to_alipay_dict'):
                params['oid'] = self.oid.to_alipay_dict()
            else:
                params['oid'] = self.oid
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.tid:
            if hasattr(self.tid, 'to_alipay_dict'):
                params['tid'] = self.tid.to_alipay_dict()
            else:
                params['tid'] = self.tid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppTestGraySendModel()
        if 'oid' in d:
            o.oid = d['oid']
        if 'pid' in d:
            o.pid = d['pid']
        if 'tid' in d:
            o.tid = d['tid']
        return o


