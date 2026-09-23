#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KeyValueDTO import KeyValueDTO


class AlipayInsMarketingInscouponTriggerResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsMarketingInscouponTriggerResponse, self).__init__()
        self._trigger_result = None

    @property
    def trigger_result(self):
        return self._trigger_result

    @trigger_result.setter
    def trigger_result(self, value):
        if isinstance(value, list):
            self._trigger_result = list()
            for i in value:
                if isinstance(i, KeyValueDTO):
                    self._trigger_result.append(i)
                else:
                    self._trigger_result.append(KeyValueDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsMarketingInscouponTriggerResponse, self).parse_response_content(response_content)
        if 'trigger_result' in response:
            self.trigger_result = response['trigger_result']
