#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudNextbuilderAgentMetainfoGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudNextbuilderAgentMetainfoGetResponse, self).__init__()
        self._agent_id = None
        self._agent_name = None
        self._agent_type = None
        self._description = None
        self._icon = None
        self._mode = None
        self._platforms = None

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
    def agent_type(self):
        return self._agent_type

    @agent_type.setter
    def agent_type(self, value):
        self._agent_type = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def platforms(self):
        return self._platforms

    @platforms.setter
    def platforms(self, value):
        if isinstance(value, list):
            self._platforms = list()
            for i in value:
                self._platforms.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayCloudNextbuilderAgentMetainfoGetResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'agent_name' in response:
            self.agent_name = response['agent_name']
        if 'agent_type' in response:
            self.agent_type = response['agent_type']
        if 'description' in response:
            self.description = response['description']
        if 'icon' in response:
            self.icon = response['icon']
        if 'mode' in response:
            self.mode = response['mode']
        if 'platforms' in response:
            self.platforms = response['platforms']
