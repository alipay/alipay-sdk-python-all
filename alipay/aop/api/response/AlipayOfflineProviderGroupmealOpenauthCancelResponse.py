#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.GroupmealOpenAuthCancelResult import GroupmealOpenAuthCancelResult


class AlipayOfflineProviderGroupmealOpenauthCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderGroupmealOpenauthCancelResponse, self).__init__()
        self._groupmeal_openauth_cancel_result = None

    @property
    def groupmeal_openauth_cancel_result(self):
        return self._groupmeal_openauth_cancel_result

    @groupmeal_openauth_cancel_result.setter
    def groupmeal_openauth_cancel_result(self, value):
        if isinstance(value, GroupmealOpenAuthCancelResult):
            self._groupmeal_openauth_cancel_result = value
        else:
            self._groupmeal_openauth_cancel_result = GroupmealOpenAuthCancelResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderGroupmealOpenauthCancelResponse, self).parse_response_content(response_content)
        if 'groupmeal_openauth_cancel_result' in response:
            self.groupmeal_openauth_cancel_result = response['groupmeal_openauth_cancel_result']
