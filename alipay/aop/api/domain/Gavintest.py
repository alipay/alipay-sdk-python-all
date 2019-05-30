#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class Gavintest(object):

    def __init__(self):
        self._newid = None

    @property
    def newid(self):
        return self._newid

    @newid.setter
    def newid(self, value):
        self._newid = value


    def to_alipay_dict(self):
        params = dict()
        if self.newid:
            if hasattr(self.newid, 'to_alipay_dict'):
                params['newid'] = self.newid.to_alipay_dict()
            else:
                params['newid'] = self.newid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Gavintest()
        if 'newid' in d:
            o.newid = d['newid']
        return o


