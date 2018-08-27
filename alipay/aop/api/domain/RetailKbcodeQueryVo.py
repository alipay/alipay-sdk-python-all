#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RetailKbcodeQueryVo(object):

    def __init__(self):
        self._batch_id = None
        self._code_template = None
        self._code_tip = None
        self._code_url = None
        self._create_time = None
        self._qr_code = None
        self._resource_url = None
        self._salesman = None

    @property
    def batch_id(self):
        return self._batch_id

    @batch_id.setter
    def batch_id(self, value):
        self._batch_id = value
    @property
    def code_template(self):
        return self._code_template

    @code_template.setter
    def code_template(self, value):
        self._code_template = value
    @property
    def code_tip(self):
        return self._code_tip

    @code_tip.setter
    def code_tip(self, value):
        self._code_tip = value
    @property
    def code_url(self):
        return self._code_url

    @code_url.setter
    def code_url(self, value):
        self._code_url = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
    @property
    def resource_url(self):
        return self._resource_url

    @resource_url.setter
    def resource_url(self, value):
        self._resource_url = value
    @property
    def salesman(self):
        return self._salesman

    @salesman.setter
    def salesman(self, value):
        self._salesman = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_id:
            if hasattr(self.batch_id, 'to_alipay_dict'):
                params['batch_id'] = self.batch_id.to_alipay_dict()
            else:
                params['batch_id'] = self.batch_id
        if self.code_template:
            if hasattr(self.code_template, 'to_alipay_dict'):
                params['code_template'] = self.code_template.to_alipay_dict()
            else:
                params['code_template'] = self.code_template
        if self.code_tip:
            if hasattr(self.code_tip, 'to_alipay_dict'):
                params['code_tip'] = self.code_tip.to_alipay_dict()
            else:
                params['code_tip'] = self.code_tip
        if self.code_url:
            if hasattr(self.code_url, 'to_alipay_dict'):
                params['code_url'] = self.code_url.to_alipay_dict()
            else:
                params['code_url'] = self.code_url
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.qr_code:
            if hasattr(self.qr_code, 'to_alipay_dict'):
                params['qr_code'] = self.qr_code.to_alipay_dict()
            else:
                params['qr_code'] = self.qr_code
        if self.resource_url:
            if hasattr(self.resource_url, 'to_alipay_dict'):
                params['resource_url'] = self.resource_url.to_alipay_dict()
            else:
                params['resource_url'] = self.resource_url
        if self.salesman:
            if hasattr(self.salesman, 'to_alipay_dict'):
                params['salesman'] = self.salesman.to_alipay_dict()
            else:
                params['salesman'] = self.salesman
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RetailKbcodeQueryVo()
        if 'batch_id' in d:
            o.batch_id = d['batch_id']
        if 'code_template' in d:
            o.code_template = d['code_template']
        if 'code_tip' in d:
            o.code_tip = d['code_tip']
        if 'code_url' in d:
            o.code_url = d['code_url']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'qr_code' in d:
            o.qr_code = d['qr_code']
        if 'resource_url' in d:
            o.resource_url = d['resource_url']
        if 'salesman' in d:
            o.salesman = d['salesman']
        return o


