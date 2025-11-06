#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalHomedoctorAgenturlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHomedoctorAgenturlQueryResponse, self).__init__()
        self._agent_url = None

    @property
    def agent_url(self):
        return self._agent_url

    @agent_url.setter
    def agent_url(self, value):
        self._agent_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHomedoctorAgenturlQueryResponse, self).parse_response_content(response_content)
        if 'agent_url' in response:
            self.agent_url = response['agent_url']
