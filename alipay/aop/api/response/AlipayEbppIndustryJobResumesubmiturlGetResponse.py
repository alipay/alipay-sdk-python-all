#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobResumesubmiturlGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobResumesubmiturlGetResponse, self).__init__()
        self._resume_submit_url = None

    @property
    def resume_submit_url(self):
        return self._resume_submit_url

    @resume_submit_url.setter
    def resume_submit_url(self, value):
        self._resume_submit_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobResumesubmiturlGetResponse, self).parse_response_content(response_content)
        if 'resume_submit_url' in response:
            self.resume_submit_url = response['resume_submit_url']
