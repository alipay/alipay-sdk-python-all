#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecruitFailureInfo import RecruitFailureInfo


class AlipayMarketingCampaignRecruitEnrollCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRecruitEnrollCreateResponse, self).__init__()
        self._accepted = None
        self._enroll_id = None
        self._failure_info = None
        self._out_biz_no = None

    @property
    def accepted(self):
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        self._accepted = value
    @property
    def enroll_id(self):
        return self._enroll_id

    @enroll_id.setter
    def enroll_id(self, value):
        self._enroll_id = value
    @property
    def failure_info(self):
        return self._failure_info

    @failure_info.setter
    def failure_info(self, value):
        if isinstance(value, RecruitFailureInfo):
            self._failure_info = value
        else:
            self._failure_info = RecruitFailureInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRecruitEnrollCreateResponse, self).parse_response_content(response_content)
        if 'accepted' in response:
            self.accepted = response['accepted']
        if 'enroll_id' in response:
            self.enroll_id = response['enroll_id']
        if 'failure_info' in response:
            self.failure_info = response['failure_info']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
