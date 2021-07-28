#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignAppleActivityConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignAppleActivityConsultResponse, self).__init__()
        self._activity_status = None
        self._bind_status = None
        self._result_code = None
        self._result_desc = None
        self._success = None

    @property
    def activity_status(self):
        return self._activity_status

    @activity_status.setter
    def activity_status(self, value):
        self._activity_status = value
    @property
    def bind_status(self):
        return self._bind_status

    @bind_status.setter
    def bind_status(self, value):
        self._bind_status = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_desc(self):
        return self._result_desc

    @result_desc.setter
    def result_desc(self, value):
        self._result_desc = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignAppleActivityConsultResponse, self).parse_response_content(response_content)
        if 'activity_status' in response:
            self.activity_status = response['activity_status']
        if 'bind_status' in response:
            self.bind_status = response['bind_status']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_desc' in response:
            self.result_desc = response['result_desc']
        if 'success' in response:
            self.success = response['success']
