#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChatMessage import ChatMessage


class AlipayIserviceCcmOlsChatrecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmOlsChatrecordQueryResponse, self).__init__()
        self._agent_id = None
        self._agent_name = None
        self._categories = None
        self._group_id = None
        self._group_name = None
        self._memo = None
        self._messages = None
        self._satisfaction = None
        self._status = None
        self._talk_duration = None
        self._visitor_province = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def agent_name(self):
        return self._agent_name

    @agent_name.setter
    def agent_name(self, value):
        self._agent_name = value
    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, value):
        if isinstance(value, list):
            self._messages = list()
            for i in value:
                if isinstance(i, ChatMessage):
                    self._messages.append(i)
                else:
                    self._messages.append(ChatMessage.from_alipay_dict(i))
    @property
    def satisfaction(self):
        return self._satisfaction

    @satisfaction.setter
    def satisfaction(self, value):
        self._satisfaction = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def talk_duration(self):
        return self._talk_duration

    @talk_duration.setter
    def talk_duration(self, value):
        self._talk_duration = value
    @property
    def visitor_province(self):
        return self._visitor_province

    @visitor_province.setter
    def visitor_province(self, value):
        self._visitor_province = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmOlsChatrecordQueryResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'agent_name' in response:
            self.agent_name = response['agent_name']
        if 'categories' in response:
            self.categories = response['categories']
        if 'group_id' in response:
            self.group_id = response['group_id']
        if 'group_name' in response:
            self.group_name = response['group_name']
        if 'memo' in response:
            self.memo = response['memo']
        if 'messages' in response:
            self.messages = response['messages']
        if 'satisfaction' in response:
            self.satisfaction = response['satisfaction']
        if 'status' in response:
            self.status = response['status']
        if 'talk_duration' in response:
            self.talk_duration = response['talk_duration']
        if 'visitor_province' in response:
            self.visitor_province = response['visitor_province']
