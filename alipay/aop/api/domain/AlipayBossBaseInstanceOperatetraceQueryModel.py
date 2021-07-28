#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossBaseInstanceOperatetraceQueryModel(object):

    def __init__(self):
        self._puid = None

    @property
    def puid(self):
        return self._puid

    @puid.setter
    def puid(self, value):
        self._puid = value


    def to_alipay_dict(self):
        params = dict()
        if self.puid:
            if hasattr(self.puid, 'to_alipay_dict'):
                params['puid'] = self.puid.to_alipay_dict()
            else:
                params['puid'] = self.puid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossBaseInstanceOperatetraceQueryModel()
        if 'puid' in d:
            o.puid = d['puid']
        return o


