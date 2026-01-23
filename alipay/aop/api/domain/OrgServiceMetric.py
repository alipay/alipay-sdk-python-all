#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrgServiceMetric(object):

    def __init__(self):
        self._org_id = None
        self._org_name = None
        self._uv_dt_td = None

    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def uv_dt_td(self):
        return self._uv_dt_td

    @uv_dt_td.setter
    def uv_dt_td(self, value):
        self._uv_dt_td = value


    def to_alipay_dict(self):
        params = dict()
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.uv_dt_td:
            if hasattr(self.uv_dt_td, 'to_alipay_dict'):
                params['uv_dt_td'] = self.uv_dt_td.to_alipay_dict()
            else:
                params['uv_dt_td'] = self.uv_dt_td
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrgServiceMetric()
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'uv_dt_td' in d:
            o.uv_dt_td = d['uv_dt_td']
        return o


