#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobSyncResponse, self).__init__()
        self._job_id = None

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobSyncResponse, self).parse_response_content(response_content)
        if 'job_id' in response:
            self.job_id = response['job_id']
