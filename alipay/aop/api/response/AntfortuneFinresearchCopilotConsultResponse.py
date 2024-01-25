#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AntfortuneFinresearchCopilotConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneFinresearchCopilotConsultResponse, self).__init__()
        self._consult_id = None

    @property
    def consult_id(self):
        return self._consult_id

    @consult_id.setter
    def consult_id(self, value):
        self._consult_id = value

    def parse_response_content(self, response_content):
        response = super(AntfortuneFinresearchCopilotConsultResponse, self).parse_response_content(response_content)
        if 'consult_id' in response:
            self.consult_id = response['consult_id']
