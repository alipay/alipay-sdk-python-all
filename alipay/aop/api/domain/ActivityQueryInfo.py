#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityQueryInfo(object):

    def __init__(self):
        self._new_user_template = None
        self._old_user_template = None
        self._query_app_id = None

    @property
    def new_user_template(self):
        return self._new_user_template

    @new_user_template.setter
    def new_user_template(self, value):
        self._new_user_template = value
    @property
    def old_user_template(self):
        return self._old_user_template

    @old_user_template.setter
    def old_user_template(self, value):
        self._old_user_template = value
    @property
    def query_app_id(self):
        return self._query_app_id

    @query_app_id.setter
    def query_app_id(self, value):
        self._query_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_user_template:
            if hasattr(self.new_user_template, 'to_alipay_dict'):
                params['new_user_template'] = self.new_user_template.to_alipay_dict()
            else:
                params['new_user_template'] = self.new_user_template
        if self.old_user_template:
            if hasattr(self.old_user_template, 'to_alipay_dict'):
                params['old_user_template'] = self.old_user_template.to_alipay_dict()
            else:
                params['old_user_template'] = self.old_user_template
        if self.query_app_id:
            if hasattr(self.query_app_id, 'to_alipay_dict'):
                params['query_app_id'] = self.query_app_id.to_alipay_dict()
            else:
                params['query_app_id'] = self.query_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityQueryInfo()
        if 'new_user_template' in d:
            o.new_user_template = d['new_user_template']
        if 'old_user_template' in d:
            o.old_user_template = d['old_user_template']
        if 'query_app_id' in d:
            o.query_app_id = d['query_app_id']
        return o


