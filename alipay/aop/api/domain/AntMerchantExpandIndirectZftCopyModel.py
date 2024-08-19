#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandIndirectZftCopyModel(object):

    def __init__(self):
        self._pid_new = None
        self._smid_old = None

    @property
    def pid_new(self):
        return self._pid_new

    @pid_new.setter
    def pid_new(self, value):
        self._pid_new = value
    @property
    def smid_old(self):
        return self._smid_old

    @smid_old.setter
    def smid_old(self, value):
        self._smid_old = value


    def to_alipay_dict(self):
        params = dict()
        if self.pid_new:
            if hasattr(self.pid_new, 'to_alipay_dict'):
                params['pid_new'] = self.pid_new.to_alipay_dict()
            else:
                params['pid_new'] = self.pid_new
        if self.smid_old:
            if hasattr(self.smid_old, 'to_alipay_dict'):
                params['smid_old'] = self.smid_old.to_alipay_dict()
            else:
                params['smid_old'] = self.smid_old
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandIndirectZftCopyModel()
        if 'pid_new' in d:
            o.pid_new = d['pid_new']
        if 'smid_old' in d:
            o.smid_old = d['smid_old']
        return o


