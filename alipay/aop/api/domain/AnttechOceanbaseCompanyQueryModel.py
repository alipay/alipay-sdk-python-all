#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseCompanyQueryModel(object):

    def __init__(self):
        self._org_name = None

    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseCompanyQueryModel()
        if 'org_name' in d:
            o.org_name = d['org_name']
        return o


