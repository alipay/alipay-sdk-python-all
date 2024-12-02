#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DtbankActivitySendControlConfigInfo(object):

    def __init__(self):
        self._api_send_control_content_list = None
        self._api_send_control_type = None
        self._play_name_list = None
        self._public_domain = None
        self._send_type = None

    @property
    def api_send_control_content_list(self):
        return self._api_send_control_content_list

    @api_send_control_content_list.setter
    def api_send_control_content_list(self, value):
        if isinstance(value, list):
            self._api_send_control_content_list = list()
            for i in value:
                self._api_send_control_content_list.append(i)
    @property
    def api_send_control_type(self):
        return self._api_send_control_type

    @api_send_control_type.setter
    def api_send_control_type(self, value):
        self._api_send_control_type = value
    @property
    def play_name_list(self):
        return self._play_name_list

    @play_name_list.setter
    def play_name_list(self, value):
        if isinstance(value, list):
            self._play_name_list = list()
            for i in value:
                self._play_name_list.append(i)
    @property
    def public_domain(self):
        return self._public_domain

    @public_domain.setter
    def public_domain(self, value):
        self._public_domain = value
    @property
    def send_type(self):
        return self._send_type

    @send_type.setter
    def send_type(self, value):
        self._send_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_send_control_content_list:
            if isinstance(self.api_send_control_content_list, list):
                for i in range(0, len(self.api_send_control_content_list)):
                    element = self.api_send_control_content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.api_send_control_content_list[i] = element.to_alipay_dict()
            if hasattr(self.api_send_control_content_list, 'to_alipay_dict'):
                params['api_send_control_content_list'] = self.api_send_control_content_list.to_alipay_dict()
            else:
                params['api_send_control_content_list'] = self.api_send_control_content_list
        if self.api_send_control_type:
            if hasattr(self.api_send_control_type, 'to_alipay_dict'):
                params['api_send_control_type'] = self.api_send_control_type.to_alipay_dict()
            else:
                params['api_send_control_type'] = self.api_send_control_type
        if self.play_name_list:
            if isinstance(self.play_name_list, list):
                for i in range(0, len(self.play_name_list)):
                    element = self.play_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.play_name_list[i] = element.to_alipay_dict()
            if hasattr(self.play_name_list, 'to_alipay_dict'):
                params['play_name_list'] = self.play_name_list.to_alipay_dict()
            else:
                params['play_name_list'] = self.play_name_list
        if self.public_domain:
            if hasattr(self.public_domain, 'to_alipay_dict'):
                params['public_domain'] = self.public_domain.to_alipay_dict()
            else:
                params['public_domain'] = self.public_domain
        if self.send_type:
            if hasattr(self.send_type, 'to_alipay_dict'):
                params['send_type'] = self.send_type.to_alipay_dict()
            else:
                params['send_type'] = self.send_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DtbankActivitySendControlConfigInfo()
        if 'api_send_control_content_list' in d:
            o.api_send_control_content_list = d['api_send_control_content_list']
        if 'api_send_control_type' in d:
            o.api_send_control_type = d['api_send_control_type']
        if 'play_name_list' in d:
            o.play_name_list = d['play_name_list']
        if 'public_domain' in d:
            o.public_domain = d['public_domain']
        if 'send_type' in d:
            o.send_type = d['send_type']
        return o


