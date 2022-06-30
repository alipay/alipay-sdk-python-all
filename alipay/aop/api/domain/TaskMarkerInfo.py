#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TaskMarkerInfo(object):

    def __init__(self):
        self._logo = None
        self._marker_desc = None
        self._marker_name = None
        self._marker_type = None
        self._personal_count = None
        self._total_count = None

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def marker_desc(self):
        return self._marker_desc

    @marker_desc.setter
    def marker_desc(self, value):
        self._marker_desc = value
    @property
    def marker_name(self):
        return self._marker_name

    @marker_name.setter
    def marker_name(self, value):
        self._marker_name = value
    @property
    def marker_type(self):
        return self._marker_type

    @marker_type.setter
    def marker_type(self, value):
        self._marker_type = value
    @property
    def personal_count(self):
        return self._personal_count

    @personal_count.setter
    def personal_count(self, value):
        self._personal_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.marker_desc:
            if hasattr(self.marker_desc, 'to_alipay_dict'):
                params['marker_desc'] = self.marker_desc.to_alipay_dict()
            else:
                params['marker_desc'] = self.marker_desc
        if self.marker_name:
            if hasattr(self.marker_name, 'to_alipay_dict'):
                params['marker_name'] = self.marker_name.to_alipay_dict()
            else:
                params['marker_name'] = self.marker_name
        if self.marker_type:
            if hasattr(self.marker_type, 'to_alipay_dict'):
                params['marker_type'] = self.marker_type.to_alipay_dict()
            else:
                params['marker_type'] = self.marker_type
        if self.personal_count:
            if hasattr(self.personal_count, 'to_alipay_dict'):
                params['personal_count'] = self.personal_count.to_alipay_dict()
            else:
                params['personal_count'] = self.personal_count
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TaskMarkerInfo()
        if 'logo' in d:
            o.logo = d['logo']
        if 'marker_desc' in d:
            o.marker_desc = d['marker_desc']
        if 'marker_name' in d:
            o.marker_name = d['marker_name']
        if 'marker_type' in d:
            o.marker_type = d['marker_type']
        if 'personal_count' in d:
            o.personal_count = d['personal_count']
        if 'total_count' in d:
            o.total_count = d['total_count']
        return o


