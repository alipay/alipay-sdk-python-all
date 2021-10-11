#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCliveVisitorOfflineModel(object):

    def __init__(self):
        self._visitor_id = None
        self._visitor_token = None

    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value
    @property
    def visitor_token(self):
        return self._visitor_token

    @visitor_token.setter
    def visitor_token(self, value):
        self._visitor_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        if self.visitor_token:
            if hasattr(self.visitor_token, 'to_alipay_dict'):
                params['visitor_token'] = self.visitor_token.to_alipay_dict()
            else:
                params['visitor_token'] = self.visitor_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCliveVisitorOfflineModel()
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_token' in d:
            o.visitor_token = d['visitor_token']
        return o


