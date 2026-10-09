#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CorporationInfo(object):

    def __init__(self):
        self._enterprise_registration_no = None

    @property
    def enterprise_registration_no(self):
        return self._enterprise_registration_no

    @enterprise_registration_no.setter
    def enterprise_registration_no(self, value):
        self._enterprise_registration_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.enterprise_registration_no:
            if hasattr(self.enterprise_registration_no, 'to_alipay_dict'):
                params['enterprise_registration_no'] = self.enterprise_registration_no.to_alipay_dict()
            else:
                params['enterprise_registration_no'] = self.enterprise_registration_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CorporationInfo()
        if 'enterprise_registration_no' in d:
            o.enterprise_registration_no = d['enterprise_registration_no']
        return o


