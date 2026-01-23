#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserServiceCardConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserServiceCardConsultResponse, self).__init__()
        self._agent_id = None
        self._expire_time = None
        self._service_list = None
        self._template_id = None
        self._url = None
        self._uuid = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def service_list(self):
        return self._service_list

    @service_list.setter
    def service_list(self, value):
        if isinstance(value, list):
            self._service_list = list()
            for i in value:
                self._service_list.append(i)
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
    @property
    def uuid(self):
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        self._uuid = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserServiceCardConsultResponse, self).parse_response_content(response_content)
        if 'agent_id' in response:
            self.agent_id = response['agent_id']
        if 'expire_time' in response:
            self.expire_time = response['expire_time']
        if 'service_list' in response:
            self.service_list = response['service_list']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'url' in response:
            self.url = response['url']
        if 'uuid' in response:
            self.uuid = response['uuid']
