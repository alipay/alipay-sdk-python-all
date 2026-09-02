#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ReferralJobInfo import ReferralJobInfo


class AlipayEbppIndustryReferralJobBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryReferralJobBatchqueryResponse, self).__init__()
        self._has_more = None
        self._job_list = None
        self._total_count = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def job_list(self):
        return self._job_list

    @job_list.setter
    def job_list(self, value):
        if isinstance(value, list):
            self._job_list = list()
            for i in value:
                if isinstance(i, ReferralJobInfo):
                    self._job_list.append(i)
                else:
                    self._job_list.append(ReferralJobInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryReferralJobBatchqueryResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'job_list' in response:
            self.job_list = response['job_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
