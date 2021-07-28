#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniResourceUserdataQueryModel(object):

    def __init__(self):
        self._plugin_id = None
        self._profile_type = None
        self._report_date = None

    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def profile_type(self):
        return self._profile_type

    @profile_type.setter
    def profile_type(self, value):
        self._profile_type = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.profile_type:
            if hasattr(self.profile_type, 'to_alipay_dict'):
                params['profile_type'] = self.profile_type.to_alipay_dict()
            else:
                params['profile_type'] = self.profile_type
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniResourceUserdataQueryModel()
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'profile_type' in d:
            o.profile_type = d['profile_type']
        if 'report_date' in d:
            o.report_date = d['report_date']
        return o


