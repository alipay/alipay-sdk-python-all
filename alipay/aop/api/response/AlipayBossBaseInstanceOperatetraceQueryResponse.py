#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BPOpenApiTicketOperateTraces import BPOpenApiTicketOperateTraces


class AlipayBossBaseInstanceOperatetraceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossBaseInstanceOperatetraceQueryResponse, self).__init__()
        self._operate_traces = None

    @property
    def operate_traces(self):
        return self._operate_traces

    @operate_traces.setter
    def operate_traces(self, value):
        if isinstance(value, BPOpenApiTicketOperateTraces):
            self._operate_traces = value
        else:
            self._operate_traces = BPOpenApiTicketOperateTraces.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayBossBaseInstanceOperatetraceQueryResponse, self).parse_response_content(response_content)
        if 'operate_traces' in response:
            self.operate_traces = response['operate_traces']
