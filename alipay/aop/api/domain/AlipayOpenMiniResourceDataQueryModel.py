#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniResourceDataQueryModel(object):

    def __init__(self):
        self._plugin_id = None
        self._report_date = None
        self._resource_id = None

    @property
    def plugin_id(self):
        return self._plugin_id

    @plugin_id.setter
    def plugin_id(self, value):
        self._plugin_id = value
    @property
    def report_date(self):
        return self._report_date

    @report_date.setter
    def report_date(self, value):
        self._report_date = value
    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, value):
        self._resource_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.plugin_id:
            if hasattr(self.plugin_id, 'to_alipay_dict'):
                params['plugin_id'] = self.plugin_id.to_alipay_dict()
            else:
                params['plugin_id'] = self.plugin_id
        if self.report_date:
            if hasattr(self.report_date, 'to_alipay_dict'):
                params['report_date'] = self.report_date.to_alipay_dict()
            else:
                params['report_date'] = self.report_date
        if self.resource_id:
            if hasattr(self.resource_id, 'to_alipay_dict'):
                params['resource_id'] = self.resource_id.to_alipay_dict()
            else:
                params['resource_id'] = self.resource_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniResourceDataQueryModel()
        if 'plugin_id' in d:
            o.plugin_id = d['plugin_id']
        if 'report_date' in d:
            o.report_date = d['report_date']
        if 'resource_id' in d:
            o.resource_id = d['resource_id']
        return o


