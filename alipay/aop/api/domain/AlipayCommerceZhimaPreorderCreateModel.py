#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceZhimaPreorderCreateModel(object):

    def __init__(self):
        self._alipay_store_id = None
        self._alipay_user_id = None
        self._biz_time = None
        self._isv_pid = None
        self._openapi_app_id = None
        self._out_biz_no = None
        self._start_time = None
        self._store_id = None
        self._template_id = None
        self._template_type = None
        self._timeout_express = None

    @property
    def alipay_store_id(self):
        return self._alipay_store_id

    @alipay_store_id.setter
    def alipay_store_id(self, value):
        self._alipay_store_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def openapi_app_id(self):
        return self._openapi_app_id

    @openapi_app_id.setter
    def openapi_app_id(self, value):
        self._openapi_app_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value
    @property
    def timeout_express(self):
        return self._timeout_express

    @timeout_express.setter
    def timeout_express(self, value):
        self._timeout_express = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_store_id:
            if hasattr(self.alipay_store_id, 'to_alipay_dict'):
                params['alipay_store_id'] = self.alipay_store_id.to_alipay_dict()
            else:
                params['alipay_store_id'] = self.alipay_store_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.openapi_app_id:
            if hasattr(self.openapi_app_id, 'to_alipay_dict'):
                params['openapi_app_id'] = self.openapi_app_id.to_alipay_dict()
            else:
                params['openapi_app_id'] = self.openapi_app_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        if self.timeout_express:
            if hasattr(self.timeout_express, 'to_alipay_dict'):
                params['timeout_express'] = self.timeout_express.to_alipay_dict()
            else:
                params['timeout_express'] = self.timeout_express
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceZhimaPreorderCreateModel()
        if 'alipay_store_id' in d:
            o.alipay_store_id = d['alipay_store_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'openapi_app_id' in d:
            o.openapi_app_id = d['openapi_app_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'template_type' in d:
            o.template_type = d['template_type']
        if 'timeout_express' in d:
            o.timeout_express = d['timeout_express']
        return o


