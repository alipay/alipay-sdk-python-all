#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OfflineInviteNewerSummaryInfo import OfflineInviteNewerSummaryInfo


class AlipayUserInviteOfflinesummaryQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInviteOfflinesummaryQueryResponse, self).__init__()
        self._offline_summary_info_list = None

    @property
    def offline_summary_info_list(self):
        return self._offline_summary_info_list

    @offline_summary_info_list.setter
    def offline_summary_info_list(self, value):
        if isinstance(value, list):
            self._offline_summary_info_list = list()
            for i in value:
                if isinstance(i, OfflineInviteNewerSummaryInfo):
                    self._offline_summary_info_list.append(i)
                else:
                    self._offline_summary_info_list.append(OfflineInviteNewerSummaryInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayUserInviteOfflinesummaryQueryResponse, self).parse_response_content(response_content)
        if 'offline_summary_info_list' in response:
            self.offline_summary_info_list = response['offline_summary_info_list']
