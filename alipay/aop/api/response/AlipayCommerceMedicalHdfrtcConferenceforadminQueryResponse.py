#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EventLogInfo import EventLogInfo


class AlipayCommerceMedicalHdfrtcConferenceforadminQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfrtcConferenceforadminQueryResponse, self).__init__()
        self._event_log_info_list = None

    @property
    def event_log_info_list(self):
        return self._event_log_info_list

    @event_log_info_list.setter
    def event_log_info_list(self, value):
        if isinstance(value, list):
            self._event_log_info_list = list()
            for i in value:
                if isinstance(i, EventLogInfo):
                    self._event_log_info_list.append(i)
                else:
                    self._event_log_info_list.append(EventLogInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfrtcConferenceforadminQueryResponse, self).parse_response_content(response_content)
        if 'event_log_info_list' in response:
            self.event_log_info_list = response['event_log_info_list']
