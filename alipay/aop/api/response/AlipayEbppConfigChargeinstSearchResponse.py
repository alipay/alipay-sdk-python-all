#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChargeInstMode import ChargeInstMode


class AlipayEbppConfigChargeinstSearchResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppConfigChargeinstSearchResponse, self).__init__()
        self._charge_inst_mode_result = None

    @property
    def charge_inst_mode_result(self):
        return self._charge_inst_mode_result

    @charge_inst_mode_result.setter
    def charge_inst_mode_result(self, value):
        if isinstance(value, list):
            self._charge_inst_mode_result = list()
            for i in value:
                if isinstance(i, ChargeInstMode):
                    self._charge_inst_mode_result.append(i)
                else:
                    self._charge_inst_mode_result.append(ChargeInstMode.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppConfigChargeinstSearchResponse, self).parse_response_content(response_content)
        if 'charge_inst_mode_result' in response:
            self.charge_inst_mode_result = response['charge_inst_mode_result']
