#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryAIChatSessionConfigRequest(object):

    def __init__(self):
        self._need_agent_content = None
        self._need_agent_info = None
        self._need_customer_like = None
        self._need_guess_question = None
        self._need_welcome_message = None

    @property
    def need_agent_content(self):
        return self._need_agent_content

    @need_agent_content.setter
    def need_agent_content(self, value):
        self._need_agent_content = value
    @property
    def need_agent_info(self):
        return self._need_agent_info

    @need_agent_info.setter
    def need_agent_info(self, value):
        self._need_agent_info = value
    @property
    def need_customer_like(self):
        return self._need_customer_like

    @need_customer_like.setter
    def need_customer_like(self, value):
        self._need_customer_like = value
    @property
    def need_guess_question(self):
        return self._need_guess_question

    @need_guess_question.setter
    def need_guess_question(self, value):
        self._need_guess_question = value
    @property
    def need_welcome_message(self):
        return self._need_welcome_message

    @need_welcome_message.setter
    def need_welcome_message(self, value):
        self._need_welcome_message = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_agent_content:
            if hasattr(self.need_agent_content, 'to_alipay_dict'):
                params['need_agent_content'] = self.need_agent_content.to_alipay_dict()
            else:
                params['need_agent_content'] = self.need_agent_content
        if self.need_agent_info:
            if hasattr(self.need_agent_info, 'to_alipay_dict'):
                params['need_agent_info'] = self.need_agent_info.to_alipay_dict()
            else:
                params['need_agent_info'] = self.need_agent_info
        if self.need_customer_like:
            if hasattr(self.need_customer_like, 'to_alipay_dict'):
                params['need_customer_like'] = self.need_customer_like.to_alipay_dict()
            else:
                params['need_customer_like'] = self.need_customer_like
        if self.need_guess_question:
            if hasattr(self.need_guess_question, 'to_alipay_dict'):
                params['need_guess_question'] = self.need_guess_question.to_alipay_dict()
            else:
                params['need_guess_question'] = self.need_guess_question
        if self.need_welcome_message:
            if hasattr(self.need_welcome_message, 'to_alipay_dict'):
                params['need_welcome_message'] = self.need_welcome_message.to_alipay_dict()
            else:
                params['need_welcome_message'] = self.need_welcome_message
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QueryAIChatSessionConfigRequest()
        if 'need_agent_content' in d:
            o.need_agent_content = d['need_agent_content']
        if 'need_agent_info' in d:
            o.need_agent_info = d['need_agent_info']
        if 'need_customer_like' in d:
            o.need_customer_like = d['need_customer_like']
        if 'need_guess_question' in d:
            o.need_guess_question = d['need_guess_question']
        if 'need_welcome_message' in d:
            o.need_welcome_message = d['need_welcome_message']
        return o


