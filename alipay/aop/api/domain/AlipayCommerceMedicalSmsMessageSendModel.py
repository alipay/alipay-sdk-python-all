#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalSmsMessageSendModel(object):

    def __init__(self):
        self._agent_id = None
        self._channel = None
        self._out_order_no = None
        self._phone_number = None
        self._template = None
        self._template_param = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        if 'channel' in d:
            o.channel = d['channel']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'template' in d:
            o.template = d['template']
        if 'template_param' in d:
            o.template_param = d['template_param']
        return o


