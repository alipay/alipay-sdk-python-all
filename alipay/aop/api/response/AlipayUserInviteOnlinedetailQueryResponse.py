#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OnlineInviteNewerDetailInfo import OnlineInviteNewerDetailInfo


class AlipayUserInviteOnlinedetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserInviteOnlinedetailQueryResponse, self).__init__()
        self._online_detail_info_list = None
        self._total_count = None
        self._total_page = None

    @property
    def online_detail_info_list(self):
        return self._online_detail_info_list

    @online_detail_info_list.setter
    def online_detail_info_list(self, value):
        if isinstance(value, list):
            self._online_detail_info_list = list()
            for i in value:
                if isinstance(i, OnlineInviteNewerDetailInfo):
                    self._online_detail_info_list.append(i)
                else:
                    self._online_detail_info_list.append(OnlineInviteNewerDetailInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserInviteOnlinedetailQueryResponse, self).parse_response_content(response_content)
        if 'online_detail_info_list' in response:
            self.online_detail_info_list = response['online_detail_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page' in response:
            self.total_page = response['total_page']
