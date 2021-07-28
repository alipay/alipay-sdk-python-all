#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdAntlawOrderhitstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdAntlawOrderhitstatusQueryResponse, self).__init__()
        self._hit_result = None

    @property
    def hit_result(self):
        return self._hit_result

    @hit_result.setter
    def hit_result(self, value):
        self._hit_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdAntlawOrderhitstatusQueryResponse, self).parse_response_content(response_content)
        if 'hit_result' in response:
            self.hit_result = response['hit_result']
