#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConnectServerAdaptResult(object):

    def __init__(self):
        self._count = None
        self._is_service_time = None
        self._portal_msg = None
        self._visitor_id = None
        self._visitor_token = None
        self._visitor_type = None
        self._welcome = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def is_service_time(self):
        return self._is_service_time

    @is_service_time.setter
    def is_service_time(self, value):
        self._is_service_time = value
    @property
    def portal_msg(self):
        return self._portal_msg

    @portal_msg.setter
    def portal_msg(self, value):
        self._portal_msg = value
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
    @property
    def visitor_type(self):
        return self._visitor_type

    @visitor_type.setter
    def visitor_type(self, value):
        self._visitor_type = value
    @property
    def welcome(self):
        return self._welcome

    @welcome.setter
    def welcome(self, value):
        self._welcome = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.is_service_time:
            if hasattr(self.is_service_time, 'to_alipay_dict'):
                params['is_service_time'] = self.is_service_time.to_alipay_dict()
            else:
                params['is_service_time'] = self.is_service_time
        if self.portal_msg:
            if hasattr(self.portal_msg, 'to_alipay_dict'):
                params['portal_msg'] = self.portal_msg.to_alipay_dict()
            else:
                params['portal_msg'] = self.portal_msg
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
        if self.visitor_type:
            if hasattr(self.visitor_type, 'to_alipay_dict'):
                params['visitor_type'] = self.visitor_type.to_alipay_dict()
            else:
                params['visitor_type'] = self.visitor_type
        if self.welcome:
            if hasattr(self.welcome, 'to_alipay_dict'):
                params['welcome'] = self.welcome.to_alipay_dict()
            else:
                params['welcome'] = self.welcome
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConnectServerAdaptResult()
        if 'count' in d:
            o.count = d['count']
        if 'is_service_time' in d:
            o.is_service_time = d['is_service_time']
        if 'portal_msg' in d:
            o.portal_msg = d['portal_msg']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        if 'visitor_token' in d:
            o.visitor_token = d['visitor_token']
        if 'visitor_type' in d:
            o.visitor_type = d['visitor_type']
        if 'welcome' in d:
            o.welcome = d['welcome']
        return o


