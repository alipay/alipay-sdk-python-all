#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LogisticsAccountStatusDTO import LogisticsAccountStatusDTO


class AlipayOpenInstantdeliveryAccountCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenInstantdeliveryAccountCreateResponse, self).__init__()
        self._logistics_account_status = None

    @property
    def logistics_account_status(self):
        return self._logistics_account_status

    @logistics_account_status.setter
    def logistics_account_status(self, value):
        if isinstance(value, list):
            self._logistics_account_status = list()
            for i in value:
                if isinstance(i, LogisticsAccountStatusDTO):
                    self._logistics_account_status.append(i)
                else:
                    self._logistics_account_status.append(LogisticsAccountStatusDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenInstantdeliveryAccountCreateResponse, self).parse_response_content(response_content)
        if 'logistics_account_status' in response:
            self.logistics_account_status = response['logistics_account_status']
