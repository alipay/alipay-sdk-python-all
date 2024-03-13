#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMessageTemplateModifyModel(object):

    def __init__(self):
        self._remark = None
        self._sign_name = None
        self._template_code = None
        self._template_content = None
        self._template_name = None
        self._template_type = None

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def sign_name(self):
        return self._sign_name

    @sign_name.setter
    def sign_name(self, value):
        self._sign_name = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_content(self):
        return self._template_content

    @template_content.setter
    def template_content(self, value):
        self._template_content = value
    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, value):
        self._template_name = value
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.sign_name:
            if hasattr(self.sign_name, 'to_alipay_dict'):
                params['sign_name'] = self.sign_name.to_alipay_dict()
            else:
                params['sign_name'] = self.sign_name
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_content:
            if hasattr(self.template_content, 'to_alipay_dict'):
                params['template_content'] = self.template_content.to_alipay_dict()
            else:
                params['template_content'] = self.template_content
        if self.template_name:
            if hasattr(self.template_name, 'to_alipay_dict'):
                params['template_name'] = self.template_name.to_alipay_dict()
            else:
                params['template_name'] = self.template_name
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMessageTemplateModifyModel()
        if 'remark' in d:
            o.remark = d['remark']
        if 'sign_name' in d:
            o.sign_name = d['sign_name']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_content' in d:
            o.template_content = d['template_content']
        if 'template_name' in d:
            o.template_name = d['template_name']
        if 'template_type' in d:
            o.template_type = d['template_type']
        return o


