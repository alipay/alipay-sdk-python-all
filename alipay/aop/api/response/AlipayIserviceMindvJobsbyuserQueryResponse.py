#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceMindvJobsbyuserQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceMindvJobsbyuserQueryResponse, self).__init__()
        self._job_ids = None

    @property
    def job_ids(self):
        return self._job_ids

    @job_ids.setter
    def job_ids(self, value):
        if isinstance(value, list):
            self._job_ids = list()
            for i in value:
                self._job_ids.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceMindvJobsbyuserQueryResponse, self).parse_response_content(response_content)
        if 'job_ids' in response:
            self.job_ids = response['job_ids']
