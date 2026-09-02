#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalSmsMessageSendModel(object):

    def __init__(self):
        self._agent_id = None
        self._cert_no = None
        self._cert_type = None
        self._channel = None
        self._iv = None
        self._out_order_no = None
        self._phone_number = None
        self._real_name = None
        self._template = None
        self._template_param = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def iv(self):
        return self._iv

    @iv.setter
    def iv(self, value):
        self._iv = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        self._template = value
    @property
    def template_param(self):
        return self._template_param

    @template_param.setter
    def template_param(self, value):
        self._template_param = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.iv:
            if hasattr(self.iv, 'to_alipay_dict'):
                params['iv'] = self.iv.to_alipay_dict()
            else:
                params['iv'] = self.iv
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        if self.template_param:
            if hasattr(self.template_param, 'to_alipay_dict'):
                params['template_param'] = self.template_param.to_alipay_dict()
            else:
                params['template_param'] = self.template_param
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalSmsMessageSendModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'iv' in d:
            o.iv = d['iv']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'template' in d:
            o.template = d['template']
        if 'template_param' in d:
            o.template_param = d['template_param']
        return o


