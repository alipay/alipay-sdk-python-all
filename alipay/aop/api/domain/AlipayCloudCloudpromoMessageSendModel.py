#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudpromoMessageSendModel(object):

    def __init__(self):
        self._out_biz_no = None
        self._phone_number = None
        self._sms_up_extend_code = None
        self._template_code = None
        self._template_param = None
        self._template_param_json = None

    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if isinstance(value, list):
            self._phone_number = list()
            for i in value:
                self._phone_number.append(i)
    @property
    def sms_up_extend_code(self):
        return self._sms_up_extend_code

    @sms_up_extend_code.setter
    def sms_up_extend_code(self, value):
        if isinstance(value, list):
            self._sms_up_extend_code = list()
            for i in value:
                self._sms_up_extend_code.append(i)
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def template_param(self):
        return self._template_param

    @template_param.setter
    def template_param(self, value):
        if isinstance(value, list):
            self._template_param = list()
            for i in value:
                self._template_param.append(i)
    @property
    def template_param_json(self):
        return self._template_param_json

    @template_param_json.setter
    def template_param_json(self, value):
        self._template_param_json = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone_number:
            if isinstance(self.phone_number, list):
                for i in range(0, len(self.phone_number)):
                    element = self.phone_number[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.phone_number[i] = element.to_alipay_dict()
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.sms_up_extend_code:
            if isinstance(self.sms_up_extend_code, list):
                for i in range(0, len(self.sms_up_extend_code)):
                    element = self.sms_up_extend_code[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sms_up_extend_code[i] = element.to_alipay_dict()
            if hasattr(self.sms_up_extend_code, 'to_alipay_dict'):
                params['sms_up_extend_code'] = self.sms_up_extend_code.to_alipay_dict()
            else:
                params['sms_up_extend_code'] = self.sms_up_extend_code
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.template_param:
            if isinstance(self.template_param, list):
                for i in range(0, len(self.template_param)):
                    element = self.template_param[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.template_param[i] = element.to_alipay_dict()
            if hasattr(self.template_param, 'to_alipay_dict'):
                params['template_param'] = self.template_param.to_alipay_dict()
            else:
                params['template_param'] = self.template_param
        if self.template_param_json:
            if hasattr(self.template_param_json, 'to_alipay_dict'):
                params['template_param_json'] = self.template_param_json.to_alipay_dict()
            else:
                params['template_param_json'] = self.template_param_json
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoMessageSendModel()
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'sms_up_extend_code' in d:
            o.sms_up_extend_code = d['sms_up_extend_code']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'template_param' in d:
            o.template_param = d['template_param']
        if 'template_param_json' in d:
            o.template_param_json = d['template_param_json']
        return o


