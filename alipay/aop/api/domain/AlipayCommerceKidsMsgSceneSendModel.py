#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceKidsMsgSceneSendModel(object):

    def __init__(self):
        self._biz_code = None
        self._biz_data = None
        self._biz_time = None
        self._out_biz_no = None
        self._template_code = None
        self._template_code_version = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_code_version(self):
        return self._template_code_version

    @template_code_version.setter
    def template_code_version(self, value):
        self._template_code_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_code_version:
            if hasattr(self.template_code_version, 'to_alipay_dict'):
                params['template_code_version'] = self.template_code_version.to_alipay_dict()
            else:
                params['template_code_version'] = self.template_code_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceKidsMsgSceneSendModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_code_version' in d:
            o.template_code_version = d['template_code_version']
        return o


