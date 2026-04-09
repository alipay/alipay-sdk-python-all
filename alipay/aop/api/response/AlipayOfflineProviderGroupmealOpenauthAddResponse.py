#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupmealOpenAuthAddResult import GroupmealOpenAuthAddResult


class AlipayOfflineProviderGroupmealOpenauthAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderGroupmealOpenauthAddResponse, self).__init__()
        self._groupmeal_openauth_add_result = None

    @property
    def groupmeal_openauth_add_result(self):
        return self._groupmeal_openauth_add_result

    @groupmeal_openauth_add_result.setter
    def groupmeal_openauth_add_result(self, value):
        if isinstance(value, GroupmealOpenAuthAddResult):
            self._groupmeal_openauth_add_result = value
        else:
            self._groupmeal_openauth_add_result = GroupmealOpenAuthAddResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderGroupmealOpenauthAddResponse, self).parse_response_content(response_content)
        if 'groupmeal_openauth_add_result' in response:
            self.groupmeal_openauth_add_result = response['groupmeal_openauth_add_result']
