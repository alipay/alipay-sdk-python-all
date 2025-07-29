#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GetAgentStatusVO import GetAgentStatusVO


class AlipayCommerceMedicalMedagentDoctoragentstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedagentDoctoragentstatusQueryResponse, self).__init__()
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, GetAgentStatusVO):
            self._data = value
        else:
            self._data = GetAgentStatusVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedagentDoctoragentstatusQueryResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
