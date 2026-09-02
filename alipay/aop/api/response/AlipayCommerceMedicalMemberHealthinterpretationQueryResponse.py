#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMemberHealthinterpretationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberHealthinterpretationQueryResponse, self).__init__()
        self._interpretation_data = None
        self._status = None

    @property
    def interpretation_data(self):
        return self._interpretation_data

    @interpretation_data.setter
    def interpretation_data(self, value):
        self._interpretation_data = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberHealthinterpretationQueryResponse, self).parse_response_content(response_content)
        if 'interpretation_data' in response:
            self.interpretation_data = response['interpretation_data']
        if 'status' in response:
            self.status = response['status']
