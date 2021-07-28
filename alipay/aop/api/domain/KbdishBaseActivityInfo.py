#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbdishBaseActivityInfo(object):

    def __init__(self):
        self._activity_clause_url = None
        self._activity_id = None
        self._activity_remark = None
        self._activity_type = None
        self._activity_value = None

    @property
    def activity_clause_url(self):
        return self._activity_clause_url

    @activity_clause_url.setter
    def activity_clause_url(self, value):
        self._activity_clause_url = value
    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_remark(self):
        return self._activity_remark

    @activity_remark.setter
    def activity_remark(self, value):
        self._activity_remark = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def activity_value(self):
        return self._activity_value

    @activity_value.setter
    def activity_value(self, value):
        self._activity_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_clause_url:
            if hasattr(self.activity_clause_url, 'to_alipay_dict'):
                params['activity_clause_url'] = self.activity_clause_url.to_alipay_dict()
            else:
                params['activity_clause_url'] = self.activity_clause_url
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_remark:
            if hasattr(self.activity_remark, 'to_alipay_dict'):
                params['activity_remark'] = self.activity_remark.to_alipay_dict()
            else:
                params['activity_remark'] = self.activity_remark
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.activity_value:
            if hasattr(self.activity_value, 'to_alipay_dict'):
                params['activity_value'] = self.activity_value.to_alipay_dict()
            else:
                params['activity_value'] = self.activity_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbdishBaseActivityInfo()
        if 'activity_clause_url' in d:
            o.activity_clause_url = d['activity_clause_url']
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_remark' in d:
            o.activity_remark = d['activity_remark']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'activity_value' in d:
            o.activity_value = d['activity_value']
        return o


