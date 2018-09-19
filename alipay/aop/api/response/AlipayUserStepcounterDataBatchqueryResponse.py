#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StepcounterDataInfo import StepcounterDataInfo


class AlipayUserStepcounterDataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserStepcounterDataBatchqueryResponse, self).__init__()
        self._step_info = None

    @property
    def step_info(self):
        return self._step_info

    @step_info.setter
    def step_info(self, value):
        if isinstance(value, list):
            self._step_info = list()
            for i in value:
                if isinstance(i, StepcounterDataInfo):
                    self._step_info.append(i)
                else:
                    self._step_info.append(StepcounterDataInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserStepcounterDataBatchqueryResponse, self).parse_response_content(response_content)
        if 'step_info' in response:
            self.step_info = response['step_info']
