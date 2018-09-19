#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MedicalSvTpCardActionInfo import MedicalSvTpCardActionInfo
from alipay.aop.api.domain.MedicalSvTpCardBodyInfo import MedicalSvTpCardBodyInfo
from alipay.aop.api.domain.MedicalSvTpCardHeadInfo import MedicalSvTpCardHeadInfo


class AlipayEcoMedicalcareCommonTpcardNotifyModel(object):

    def __init__(self):
        self._action_info = None
        self._body_info = None
        self._extend_params = None
        self._header_info = None
        self._notify_time = None
        self._operate = None
        self._template_code = None
        self._third_no = None
        self._user_id = None

    @property
    def action_info(self):
        return self._action_info

    @action_info.setter
    def action_info(self, value):
        if isinstance(value, list):
            self._action_info = list()
            for i in value:
                if isinstance(i, MedicalSvTpCardActionInfo):
                    self._action_info.append(i)
                else:
                    self._action_info.append(MedicalSvTpCardActionInfo.from_alipay_dict(i))
    @property
    def body_info(self):
        return self._body_info

    @body_info.setter
    def body_info(self, value):
        if isinstance(value, list):
            self._body_info = list()
            for i in value:
                if isinstance(i, MedicalSvTpCardBodyInfo):
                    self._body_info.append(i)
                else:
                    self._body_info.append(MedicalSvTpCardBodyInfo.from_alipay_dict(i))
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def header_info(self):
        return self._header_info

    @header_info.setter
    def header_info(self, value):
        if isinstance(value, MedicalSvTpCardHeadInfo):
            self._header_info = value
        else:
            self._header_info = MedicalSvTpCardHeadInfo.from_alipay_dict(value)
    @property
    def notify_time(self):
        return self._notify_time

    @notify_time.setter
    def notify_time(self, value):
        self._notify_time = value
    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        self._operate = value
    @property
    def template_code(self):
        return self._template_code

    @template_code.setter
    def template_code(self, value):
        self._template_code = value
    @property
    def third_no(self):
        return self._third_no

    @third_no.setter
    def third_no(self, value):
        self._third_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_info:
            if isinstance(self.action_info, list):
                for i in range(0, len(self.action_info)):
                    element = self.action_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.action_info[i] = element.to_alipay_dict()
            if hasattr(self.action_info, 'to_alipay_dict'):
                params['action_info'] = self.action_info.to_alipay_dict()
            else:
                params['action_info'] = self.action_info
        if self.body_info:
            if isinstance(self.body_info, list):
                for i in range(0, len(self.body_info)):
                    element = self.body_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.body_info[i] = element.to_alipay_dict()
            if hasattr(self.body_info, 'to_alipay_dict'):
                params['body_info'] = self.body_info.to_alipay_dict()
            else:
                params['body_info'] = self.body_info
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.header_info:
            if hasattr(self.header_info, 'to_alipay_dict'):
                params['header_info'] = self.header_info.to_alipay_dict()
            else:
                params['header_info'] = self.header_info
        if self.notify_time:
            if hasattr(self.notify_time, 'to_alipay_dict'):
                params['notify_time'] = self.notify_time.to_alipay_dict()
            else:
                params['notify_time'] = self.notify_time
        if self.operate:
            if hasattr(self.operate, 'to_alipay_dict'):
                params['operate'] = self.operate.to_alipay_dict()
            else:
                params['operate'] = self.operate
        if self.template_code:
            if hasattr(self.template_code, 'to_alipay_dict'):
                params['template_code'] = self.template_code.to_alipay_dict()
            else:
                params['template_code'] = self.template_code
        if self.third_no:
            if hasattr(self.third_no, 'to_alipay_dict'):
                params['third_no'] = self.third_no.to_alipay_dict()
            else:
                params['third_no'] = self.third_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMedicalcareCommonTpcardNotifyModel()
        if 'action_info' in d:
            o.action_info = d['action_info']
        if 'body_info' in d:
            o.body_info = d['body_info']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'header_info' in d:
            o.header_info = d['header_info']
        if 'notify_time' in d:
            o.notify_time = d['notify_time']
        if 'operate' in d:
            o.operate = d['operate']
        if 'template_code' in d:
            o.template_code = d['template_code']
        if 'third_no' in d:
            o.third_no = d['third_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


