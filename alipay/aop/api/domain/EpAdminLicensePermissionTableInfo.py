#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpAdminLicensePermissionTableInfo(object):

    def __init__(self):
        self._splb = None
        self._xkjdrq = None
        self._xkjzrq = None
        self._xzxujdwh = None

    @property
    def splb(self):
        return self._splb

    @splb.setter
    def splb(self, value):
        self._splb = value
    @property
    def xkjdrq(self):
        return self._xkjdrq

    @xkjdrq.setter
    def xkjdrq(self, value):
        self._xkjdrq = value
    @property
    def xkjzrq(self):
        return self._xkjzrq

    @xkjzrq.setter
    def xkjzrq(self, value):
        self._xkjzrq = value
    @property
    def xzxujdwh(self):
        return self._xzxujdwh

    @xzxujdwh.setter
    def xzxujdwh(self, value):
        self._xzxujdwh = value


    def to_alipay_dict(self):
        params = dict()
        if self.splb:
            if hasattr(self.splb, 'to_alipay_dict'):
                params['splb'] = self.splb.to_alipay_dict()
            else:
                params['splb'] = self.splb
        if self.xkjdrq:
            if hasattr(self.xkjdrq, 'to_alipay_dict'):
                params['xkjdrq'] = self.xkjdrq.to_alipay_dict()
            else:
                params['xkjdrq'] = self.xkjdrq
        if self.xkjzrq:
            if hasattr(self.xkjzrq, 'to_alipay_dict'):
                params['xkjzrq'] = self.xkjzrq.to_alipay_dict()
            else:
                params['xkjzrq'] = self.xkjzrq
        if self.xzxujdwh:
            if hasattr(self.xzxujdwh, 'to_alipay_dict'):
                params['xzxujdwh'] = self.xzxujdwh.to_alipay_dict()
            else:
                params['xzxujdwh'] = self.xzxujdwh
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpAdminLicensePermissionTableInfo()
        if 'splb' in d:
            o.splb = d['splb']
        if 'xkjdrq' in d:
            o.xkjdrq = d['xkjdrq']
        if 'xkjzrq' in d:
            o.xkjzrq = d['xkjzrq']
        if 'xzxujdwh' in d:
            o.xzxujdwh = d['xzxujdwh']
        return o


