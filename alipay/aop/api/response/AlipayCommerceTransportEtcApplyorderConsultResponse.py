#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcApplyorderConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcApplyorderConsultResponse, self).__init__()
        self._consult_desc = None
        self._consult_result = None
        self._consult_scene = None

    @property
    def consult_desc(self):
        return self._consult_desc

    @consult_desc.setter
    def consult_desc(self, value):
        self._consult_desc = value
    @property
    def consult_result(self):
        return self._consult_result

    @consult_result.setter
    def consult_result(self, value):
        self._consult_result = value
    @property
    def consult_scene(self):
        return self._consult_scene

    @consult_scene.setter
    def consult_scene(self, value):
        self._consult_scene = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcApplyorderConsultResponse, self).parse_response_content(response_content)
        if 'consult_desc' in response:
            self.consult_desc = response['consult_desc']
        if 'consult_result' in response:
            self.consult_result = response['consult_result']
        if 'consult_scene' in response:
            self.consult_scene = response['consult_scene']
