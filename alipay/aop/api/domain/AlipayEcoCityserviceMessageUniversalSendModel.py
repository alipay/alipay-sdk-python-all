#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UniversalKeyword import UniversalKeyword


class AlipayEcoCityserviceMessageUniversalSendModel(object):

    def __init__(self):
        self._keyword_list = None
        self._message_app_id = None
        self._template_id = None
        self._third_msg_id = None
        self._user_id = None

    @property
    def keyword_list(self):
        return self._keyword_list

    @keyword_list.setter
    def keyword_list(self, value):
        if isinstance(value, list):
            self._keyword_list = list()
            for i in value:
                if isinstance(i, UniversalKeyword):
                    self._keyword_list.append(i)
                else:
                    self._keyword_list.append(UniversalKeyword.from_alipay_dict(i))
    @property
    def message_app_id(self):
        return self._message_app_id

    @message_app_id.setter
    def message_app_id(self, value):
        self._message_app_id = value
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.keyword_list:
            if isinstance(self.keyword_list, list):
                for i in range(0, len(self.keyword_list)):
                    element = self.keyword_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.keyword_list[i] = element.to_alipay_dict()
            if hasattr(self.keyword_list, 'to_alipay_dict'):
                params['keyword_list'] = self.keyword_list.to_alipay_dict()
            else:
                params['keyword_list'] = self.keyword_list
        if self.message_app_id:
            if hasattr(self.message_app_id, 'to_alipay_dict'):
                params['message_app_id'] = self.message_app_id.to_alipay_dict()
            else:
                params['message_app_id'] = self.message_app_id
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
        o = AlipayEcoCityserviceMessageUniversalSendModel()
        if 'keyword_list' in d:
            o.keyword_list = d['keyword_list']
        if 'message_app_id' in d:
            o.message_app_id = d['message_app_id']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'third_msg_id' in d:
            o.third_msg_id = d['third_msg_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


