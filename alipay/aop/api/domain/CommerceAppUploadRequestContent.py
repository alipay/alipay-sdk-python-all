#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CommerceAppUploadRequestContent(object):

    def __init__(self):
        self._activity_id = None
        self._body = None
        self._query = None
        self._tenant_app_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def tenant_app_id(self):
        return self._tenant_app_id

    @tenant_app_id.setter
    def tenant_app_id(self, value):
        self._tenant_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.body:
            if hasattr(self.body, 'to_alipay_dict'):
                params['body'] = self.body.to_alipay_dict()
            else:
                params['body'] = self.body
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.tenant_app_id:
            if hasattr(self.tenant_app_id, 'to_alipay_dict'):
                params['tenant_app_id'] = self.tenant_app_id.to_alipay_dict()
            else:
                params['tenant_app_id'] = self.tenant_app_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CommerceAppUploadRequestContent()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'body' in d:
            o.body = d['body']
        if 'query' in d:
            o.query = d['query']
        if 'tenant_app_id' in d:
            o.tenant_app_id = d['tenant_app_id']
        return o


