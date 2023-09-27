#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.FlowStatsEntry import FlowStatsEntry


class AlipayCloudCloudbaseAntifloodFlowbysourceipQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseAntifloodFlowbysourceipQueryResponse, self).__init__()
        self._flowstats = None

    @property
    def flowstats(self):
        return self._flowstats

    @flowstats.setter
    def flowstats(self, value):
        if isinstance(value, list):
            self._flowstats = list()
            for i in value:
                if isinstance(i, FlowStatsEntry):
                    self._flowstats.append(i)
                else:
                    self._flowstats.append(FlowStatsEntry.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseAntifloodFlowbysourceipQueryResponse, self).parse_response_content(response_content)
        if 'flowstats' in response:
            self.flowstats = response['flowstats']
