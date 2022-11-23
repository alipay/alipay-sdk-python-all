#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerJobworthQuickhireSubmitResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerJobworthQuickhireSubmitResponse, self).__init__()
        self._deliver_result = None

    @property
    def deliver_result(self):
        return self._deliver_result

    @deliver_result.setter
    def deliver_result(self, value):
        self._deliver_result = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerJobworthQuickhireSubmitResponse, self).parse_response_content(response_content)
        if 'deliver_result' in response:
            self.deliver_result = response['deliver_result']
