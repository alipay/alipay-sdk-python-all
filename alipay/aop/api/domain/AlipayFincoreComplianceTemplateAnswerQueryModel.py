#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceTemplateAnswerQueryModel(object):

    def __init__(self):
        self._biz_object_def_json = None
        self._template_code = None
        self._tenant = None

    @property
    def biz_object_def_json(self):
        return self._biz_object_def_json

    @biz_object_def_json.setter
    def biz_object_def_json(self, value):
        self._biz_object_def_json = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, value):
        self._tenant = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_object_def_json:
            if hasattr(self.biz_object_def_json, 'to_alipay_dict'):
                params['biz_object_def_json'] = self.biz_object_def_json.to_alipay_dict()
            else:
                params['biz_object_def_json'] = self.biz_object_def_json
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.tenant:
            if hasattr(self.tenant, 'to_alipay_dict'):
                params['tenant'] = self.tenant.to_alipay_dict()
            else:
                params['tenant'] = self.tenant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceTemplateAnswerQueryModel()
        if 'biz_object_def_json' in d:
            o.biz_object_def_json = d['biz_object_def_json']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'tenant' in d:
            o.tenant = d['tenant']
        return o


