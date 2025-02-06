#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryRecruitJobSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryRecruitJobSyncResponse, self).__init__()
        self._job_id = None
        self._recruit_job_id = None

    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def recruit_job_id(self):
        return self._recruit_job_id

    @recruit_job_id.setter
    def recruit_job_id(self, value):
        self._recruit_job_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryRecruitJobSyncResponse, self).parse_response_content(response_content)
        if 'job_id' in response:
            self.job_id = response['job_id']
        if 'recruit_job_id' in response:
            self.recruit_job_id = response['recruit_job_id']
