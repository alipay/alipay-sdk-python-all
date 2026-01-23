#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrganizationJobInfo import OrganizationJobInfo


class AlipayEbppIndustryJobOrganizationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobOrganizationQueryResponse, self).__init__()
        self._job_info_list = None
        self._total_count = None
        self._total_page = None

    @property
    def job_info_list(self):
        return self._job_info_list

    @job_info_list.setter
    def job_info_list(self, value):
        if isinstance(value, list):
            self._job_info_list = list()
            for i in value:
                if isinstance(i, OrganizationJobInfo):
                    self._job_info_list.append(i)
                else:
                    self._job_info_list.append(OrganizationJobInfo.from_alipay_dict(i))
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_page(self):
        return self._total_page

    @total_page.setter
    def total_page(self, value):
        self._total_page = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobOrganizationQueryResponse, self).parse_response_content(response_content)
        if 'job_info_list' in response:
            self.job_info_list = response['job_info_list']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'total_page' in response:
            self.total_page = response['total_page']
