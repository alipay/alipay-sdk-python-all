#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalAfusigninQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalAfusigninQueryResponse, self).__init__()
        self._agent_avatar = None
        self._doctor_id = None
        self._status = None
        self._url = None

    @property
    def agent_avatar(self):
        return self._agent_avatar

    @agent_avatar.setter
    def agent_avatar(self, value):
        self._agent_avatar = value
    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        self._doctor_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalAfusigninQueryResponse, self).parse_response_content(response_content)
        if 'agent_avatar' in response:
            self.agent_avatar = response['agent_avatar']
        if 'doctor_id' in response:
            self.doctor_id = response['doctor_id']
        if 'status' in response:
            self.status = response['status']
        if 'url' in response:
            self.url = response['url']
