#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.WhiteListFailDetail import WhiteListFailDetail


class AlipayOfflineProviderCollaborateDevicebindwhitelistBatchcreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderCollaborateDevicebindwhitelistBatchcreateResponse, self).__init__()
        self._fail_detail_list = None
        self._success_count = None

    @property
    def fail_detail_list(self):
        return self._fail_detail_list

    @fail_detail_list.setter
    def fail_detail_list(self, value):
        if isinstance(value, list):
            self._fail_detail_list = list()
            for i in value:
                if isinstance(i, WhiteListFailDetail):
                    self._fail_detail_list.append(i)
                else:
                    self._fail_detail_list.append(WhiteListFailDetail.from_alipay_dict(i))
    @property
    def success_count(self):
        return self._success_count

    @success_count.setter
    def success_count(self, value):
        self._success_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderCollaborateDevicebindwhitelistBatchcreateResponse, self).parse_response_content(response_content)
        if 'fail_detail_list' in response:
            self.fail_detail_list = response['fail_detail_list']
        if 'success_count' in response:
            self.success_count = response['success_count']
