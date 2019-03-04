#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OnlineInviteNewerSummaryInfo import OnlineInviteNewerSummaryInfo


class AlipayUserInviteOnlinesummaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInviteOnlinesummaryQueryResponse, self).__init__()
        self._online_summary_info_list = None

    @property
    def online_summary_info_list(self):
        return self._online_summary_info_list

    @online_summary_info_list.setter
    def online_summary_info_list(self, value):
        if isinstance(value, list):
            self._online_summary_info_list = list()
            for i in value:
                if isinstance(i, OnlineInviteNewerSummaryInfo):
                    self._online_summary_info_list.append(i)
                else:
                    self._online_summary_info_list.append(OnlineInviteNewerSummaryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserInviteOnlinesummaryQueryResponse, self).parse_response_content(response_content)
        if 'online_summary_info_list' in response:
            self.online_summary_info_list = response['online_summary_info_list']
