#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BusinessLicenseCertFileds(object):

    def __init__(self):
        self._creditcode = None
        self._entname = None

    @property
    def creditcode(self):
        return self._creditcode

    @creditcode.setter
    def creditcode(self, value):
        self._creditcode = value
    @property
    def entname(self):
        return self._entname

    @entname.setter
    def entname(self, value):
        self._entname = value


    def to_alipay_dict(self):
        params = dict()
        if self.creditcode:
            if hasattr(self.creditcode, 'to_alipay_dict'):
                params['creditcode'] = self.creditcode.to_alipay_dict()
            else:
                params['creditcode'] = self.creditcode
        if self.entname:
            if hasattr(self.entname, 'to_alipay_dict'):
                params['entname'] = self.entname.to_alipay_dict()
            else:
                params['entname'] = self.entname
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BusinessLicenseCertFileds()
        if 'creditcode' in d:
            o.creditcode = d['creditcode']
        if 'entname' in d:
            o.entname = d['entname']
        return o


