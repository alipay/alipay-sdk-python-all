#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingCampaignActivityModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignActivityModifyResponse, self).__init__()
        self._audit_status = None
        self._camp_status = None

    @property
    def audit_status(self):
        return self._audit_status

    @audit_status.setter
    def audit_status(self, value):
        self._audit_status = value
    @property
    def camp_status(self):
        return self._camp_status

    @camp_status.setter
    def camp_status(self, value):
        self._camp_status = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignActivityModifyResponse, self).parse_response_content(response_content)
        if 'audit_status' in response:
            self.audit_status = response['audit_status']
        if 'camp_status' in response:
            self.camp_status = response['camp_status']
