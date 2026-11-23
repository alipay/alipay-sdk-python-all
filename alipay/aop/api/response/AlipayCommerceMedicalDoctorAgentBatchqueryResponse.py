#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DoctorAgentInfo import DoctorAgentInfo


class AlipayCommerceMedicalDoctorAgentBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalDoctorAgentBatchqueryResponse, self).__init__()
        self._agent_info_list = None

    @property
    def agent_info_list(self):
        return self._agent_info_list

    @agent_info_list.setter
    def agent_info_list(self, value):
        if isinstance(value, list):
            self._agent_info_list = list()
            for i in value:
                if isinstance(i, DoctorAgentInfo):
                    self._agent_info_list.append(i)
                else:
                    self._agent_info_list.append(DoctorAgentInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalDoctorAgentBatchqueryResponse, self).parse_response_content(response_content)
        if 'agent_info_list' in response:
            self.agent_info_list = response['agent_info_list']
