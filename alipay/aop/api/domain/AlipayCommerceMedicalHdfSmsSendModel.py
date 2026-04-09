#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfSmsSendModel(object):

    def __init__(self):
        self._sms_app_id = None
        self._template_args_str = None
        self._template_id = None
        self._third_msg_id = None
        self._to_account_no = None

    @property
    def sms_app_id(self):
        return self._sms_app_id

    @sms_app_id.setter
    def sms_app_id(self, value):
        self._sms_app_id = value
    @property
    def template_args_str(self):
        return self._template_args_str

    @template_args_str.setter
    def template_args_str(self, value):
        self._template_args_str = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def third_msg_id(self):
        return self._third_msg_id

    @third_msg_id.setter
    def third_msg_id(self, value):
        self._third_msg_id = value
    @property
    def to_account_no(self):
        return self._to_account_no

    @to_account_no.setter
    def to_account_no(self, value):
        self._to_account_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.sms_app_id:
            if hasattr(self.sms_app_id, 'to_alipay_dict'):
                params['sms_app_id'] = self.sms_app_id.to_alipay_dict()
            else:
                params['sms_app_id'] = self.sms_app_id
        if self.template_args_str:
            if hasattr(self.template_args_str, 'to_alipay_dict'):
                params['template_args_str'] = self.template_args_str.to_alipay_dict()
            else:
                params['template_args_str'] = self.template_args_str
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.third_msg_id:
            if hasattr(self.third_msg_id, 'to_alipay_dict'):
                params['third_msg_id'] = self.third_msg_id.to_alipay_dict()
            else:
                params['third_msg_id'] = self.third_msg_id
        if self.to_account_no:
            if hasattr(self.to_account_no, 'to_alipay_dict'):
                params['to_account_no'] = self.to_account_no.to_alipay_dict()
            else:
                params['to_account_no'] = self.to_account_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfSmsSendModel()
        if 'sms_app_id' in d:
            o.sms_app_id = d['sms_app_id']
        if 'template_args_str' in d:
            o.template_args_str = d['template_args_str']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'third_msg_id' in d:
            o.third_msg_id = d['third_msg_id']
        if 'to_account_no' in d:
            o.to_account_no = d['to_account_no']
        return o


