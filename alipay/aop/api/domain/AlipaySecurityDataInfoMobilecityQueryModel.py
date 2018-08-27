#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataInfoMobilecityQueryModel(object):

    def __init__(self):
        self._phone = None

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataInfoMobilecityQueryModel()
        if 'phone' in d:
            o.phone = d['phone']
        return o


