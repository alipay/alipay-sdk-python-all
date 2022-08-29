#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniUserinfoQueryModel(object):

    def __init__(self):
        self._logonid = None

    @property
    def logonid(self):
        return self._logonid

    @logonid.setter
    def logonid(self, value):
        self._logonid = value


    def to_alipay_dict(self):
        params = dict()
        if self.logonid:
            if hasattr(self.logonid, 'to_alipay_dict'):
                params['logonid'] = self.logonid.to_alipay_dict()
            else:
                params['logonid'] = self.logonid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniUserinfoQueryModel()
        if 'logonid' in d:
            o.logonid = d['logonid']
        return o


