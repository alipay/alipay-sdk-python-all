#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AgentScheduleLog import AgentScheduleLog


class AlipayIserviceCcmAgentSchedulelogQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCcmAgentSchedulelogQueryResponse, self).__init__()
        self._agent_schedule_logs = None
        self._page_num = None
        self._page_size = None
        self._total_count = None

    @property
    def agent_schedule_logs(self):
        return self._agent_schedule_logs

    @agent_schedule_logs.setter
    def agent_schedule_logs(self, value):
        if isinstance(value, AgentScheduleLog):
            self._agent_schedule_logs = value
        else:
            self._agent_schedule_logs = AgentScheduleLog.from_alipay_dict(value)
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCcmAgentSchedulelogQueryResponse, self).parse_response_content(response_content)
        if 'agent_schedule_logs' in response:
            self.agent_schedule_logs = response['agent_schedule_logs']
        if 'page_num' in response:
            self.page_num = response['page_num']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
