#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecruitEnrollInfo import RecruitEnrollInfo


class AlipayMarketingRecruitEnrollQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingRecruitEnrollQueryResponse, self).__init__()
        self._enroll_id = None
        self._enroll_info = None
        self._enroll_time = None
        self._memo = None
        self._out_biz_no = None
        self._plan_id = None
        self._status = None

    @property
    def enroll_id(self):
        return self._enroll_id

    @enroll_id.setter
    def enroll_id(self, value):
        self._enroll_id = value
    @property
    def enroll_info(self):
        return self._enroll_info

    @enroll_info.setter
    def enroll_info(self, value):
        if isinstance(value, RecruitEnrollInfo):
            self._enroll_info = value
        else:
            self._enroll_info = RecruitEnrollInfo.from_alipay_dict(value)
    @property
    def enroll_time(self):
        return self._enroll_time

    @enroll_time.setter
    def enroll_time(self, value):
        self._enroll_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingRecruitEnrollQueryResponse, self).parse_response_content(response_content)
        if 'enroll_id' in response:
            self.enroll_id = response['enroll_id']
        if 'enroll_info' in response:
            self.enroll_info = response['enroll_info']
        if 'enroll_time' in response:
            self.enroll_time = response['enroll_time']
        if 'memo' in response:
            self.memo = response['memo']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'status' in response:
            self.status = response['status']
