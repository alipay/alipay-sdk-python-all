#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AIChatAgentInfo import AIChatAgentInfo
from alipay.aop.api.domain.AIChatCustomerLike import AIChatCustomerLike
from alipay.aop.api.domain.AIChatWelcomeMessage import AIChatWelcomeMessage


class AlipayCloudCloudpromoAichatSessionCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudpromoAichatSessionCreateResponse, self).__init__()
        self._agent_content = None
        self._agent_info = None
        self._customer_like = None
        self._guess_question_list = None
        self._new_session_id = None
        self._session_id = None
        self._welcome_message = None

    @property
    def agent_content(self):
        return self._agent_content

    @agent_content.setter
    def agent_content(self, value):
        self._agent_content = value
    @property
    def agent_info(self):
        return self._agent_info

    @agent_info.setter
    def agent_info(self, value):
        if isinstance(value, AIChatAgentInfo):
            self._agent_info = value
        else:
            self._agent_info = AIChatAgentInfo.from_alipay_dict(value)
    @property
    def customer_like(self):
        return self._customer_like

    @customer_like.setter
    def customer_like(self, value):
        if isinstance(value, AIChatCustomerLike):
            self._customer_like = value
        else:
            self._customer_like = AIChatCustomerLike.from_alipay_dict(value)
    @property
    def guess_question_list(self):
        return self._guess_question_list

    @guess_question_list.setter
    def guess_question_list(self, value):
        if isinstance(value, list):
            self._guess_question_list = list()
            for i in value:
                self._guess_question_list.append(i)
    @property
    def new_session_id(self):
        return self._new_session_id

    @new_session_id.setter
    def new_session_id(self, value):
        self._new_session_id = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def welcome_message(self):
        return self._welcome_message

    @welcome_message.setter
    def welcome_message(self, value):
        if isinstance(value, AIChatWelcomeMessage):
            self._welcome_message = value
        else:
            self._welcome_message = AIChatWelcomeMessage.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudpromoAichatSessionCreateResponse, self).parse_response_content(response_content)
        if 'agent_content' in response:
            self.agent_content = response['agent_content']
        if 'agent_info' in response:
            self.agent_info = response['agent_info']
        if 'customer_like' in response:
            self.customer_like = response['customer_like']
        if 'guess_question_list' in response:
            self.guess_question_list = response['guess_question_list']
        if 'new_session_id' in response:
            self.new_session_id = response['new_session_id']
        if 'session_id' in response:
            self.session_id = response['session_id']
        if 'welcome_message' in response:
            self.welcome_message = response['welcome_message']
