#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BooKAttributesDTO(object):

    def __init__(self):
        self._ch_info = None
        self._chat_id = None
        self._mgw_app_name = None

    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def chat_id(self):
        return self._chat_id

    @chat_id.setter
    def chat_id(self, value):
        self._chat_id = value
    @property
    def mgw_app_name(self):
        return self._mgw_app_name

    @mgw_app_name.setter
    def mgw_app_name(self, value):
        self._mgw_app_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.chat_id:
            if hasattr(self.chat_id, 'to_alipay_dict'):
                params['chat_id'] = self.chat_id.to_alipay_dict()
            else:
                params['chat_id'] = self.chat_id
        if self.mgw_app_name:
            if hasattr(self.mgw_app_name, 'to_alipay_dict'):
                params['mgw_app_name'] = self.mgw_app_name.to_alipay_dict()
            else:
                params['mgw_app_name'] = self.mgw_app_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BooKAttributesDTO()
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'chat_id' in d:
            o.chat_id = d['chat_id']
        if 'mgw_app_name' in d:
            o.mgw_app_name = d['mgw_app_name']
        return o


