#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignRecruitEnrollCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRecruitEnrollCloseResponse, self).__init__()
        self._enroll_id = None
        self._status = None

    @property
    def enroll_id(self):
        return self._enroll_id

    @enroll_id.setter
    def enroll_id(self, value):
        self._enroll_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRecruitEnrollCloseResponse, self).parse_response_content(response_content)
        if 'enroll_id' in response:
            self.enroll_id = response['enroll_id']
        if 'status' in response:
            self.status = response['status']
