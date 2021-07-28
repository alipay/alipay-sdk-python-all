#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AuthFieldApply(object):

    def __init__(self):
        self._api_name = None
        self._customer_answer = None
        self._field_name = None
        self._memo = None
        self._package_code = None
        self._qps_answer = None
        self._scene_code = None
        self._tiny_app_template_id = None

    @property
    def api_name(self):
        return self._api_name

    @api_name.setter
    def api_name(self, value):
        self._api_name = value
    @property
    def customer_answer(self):
        return self._customer_answer

    @customer_answer.setter
    def customer_answer(self, value):
        self._customer_answer = value
    @property
    def field_name(self):
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        self._field_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value
    @property
    def qps_answer(self):
        return self._qps_answer

    @qps_answer.setter
    def qps_answer(self, value):
        self._qps_answer = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def tiny_app_template_id(self):
        return self._tiny_app_template_id

    @tiny_app_template_id.setter
    def tiny_app_template_id(self, value):
        self._tiny_app_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_name:
            if hasattr(self.api_name, 'to_alipay_dict'):
                params['api_name'] = self.api_name.to_alipay_dict()
            else:
                params['api_name'] = self.api_name
        if self.customer_answer:
            if hasattr(self.customer_answer, 'to_alipay_dict'):
                params['customer_answer'] = self.customer_answer.to_alipay_dict()
            else:
                params['customer_answer'] = self.customer_answer
        if self.field_name:
            if hasattr(self.field_name, 'to_alipay_dict'):
                params['field_name'] = self.field_name.to_alipay_dict()
            else:
                params['field_name'] = self.field_name
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.package_code:
            if hasattr(self.package_code, 'to_alipay_dict'):
                params['package_code'] = self.package_code.to_alipay_dict()
            else:
                params['package_code'] = self.package_code
        if self.qps_answer:
            if hasattr(self.qps_answer, 'to_alipay_dict'):
                params['qps_answer'] = self.qps_answer.to_alipay_dict()
            else:
                params['qps_answer'] = self.qps_answer
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.tiny_app_template_id:
            if hasattr(self.tiny_app_template_id, 'to_alipay_dict'):
                params['tiny_app_template_id'] = self.tiny_app_template_id.to_alipay_dict()
            else:
                params['tiny_app_template_id'] = self.tiny_app_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AuthFieldApply()
        if 'api_name' in d:
            o.api_name = d['api_name']
        if 'customer_answer' in d:
            o.customer_answer = d['customer_answer']
        if 'field_name' in d:
            o.field_name = d['field_name']
        if 'memo' in d:
            o.memo = d['memo']
        if 'package_code' in d:
            o.package_code = d['package_code']
        if 'qps_answer' in d:
            o.qps_answer = d['qps_answer']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'tiny_app_template_id' in d:
            o.tiny_app_template_id = d['tiny_app_template_id']
        return o


