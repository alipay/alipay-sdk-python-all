#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityQueryResult(object):

    def __init__(self):
        self._biz_code = None
        self._biz_msg = None
        self._query_app_id = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def query_app_id(self):
        return self._query_app_id

    @query_app_id.setter
    def query_app_id(self, value):
        self._query_app_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_msg:
            if hasattr(self.biz_msg, 'to_alipay_dict'):
                params['biz_msg'] = self.biz_msg.to_alipay_dict()
            else:
                params['biz_msg'] = self.biz_msg
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
        o = ActivityQueryResult()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_msg' in d:
            o.biz_msg = d['biz_msg']
        if 'query_app_id' in d:
            o.query_app_id = d['query_app_id']
        return o


