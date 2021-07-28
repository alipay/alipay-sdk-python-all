#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiSceneprodBenefitAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiSceneprodBenefitAddResponse, self).__init__()
        self._append_id = None

    @property
    def append_id(self):
        return self._append_id

    @append_id.setter
    def append_id(self, value):
        self._append_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiSceneprodBenefitAddResponse, self).parse_response_content(response_content)
        if 'append_id' in response:
            self.append_id = response['append_id']
