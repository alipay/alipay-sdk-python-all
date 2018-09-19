#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserSceneCooperationConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserSceneCooperationConsultResponse, self).__init__()
        self._consult_result = None
        self._invite_result = None

    @property
    def consult_result(self):
        return self._consult_result

    @consult_result.setter
    def consult_result(self, value):
        self._consult_result = value
    @property
    def invite_result(self):
        return self._invite_result

    @invite_result.setter
    def invite_result(self, value):
        self._invite_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserSceneCooperationConsultResponse, self).parse_response_content(response_content)
        if 'consult_result' in response:
            self.consult_result = response['consult_result']
        if 'invite_result' in response:
            self.invite_result = response['invite_result']
