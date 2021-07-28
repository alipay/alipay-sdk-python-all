#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecruitEnrollRule import RecruitEnrollRule


class AlipayMarketingRecruitPlanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingRecruitPlanQueryResponse, self).__init__()
        self._description = None
        self._enroll_end_time = None
        self._enroll_rules = None
        self._enroll_start_time = None
        self._logo = None
        self._plan_id = None
        self._plan_name = None
        self._status = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def enroll_end_time(self):
        return self._enroll_end_time

    @enroll_end_time.setter
    def enroll_end_time(self, value):
        self._enroll_end_time = value
    @property
    def enroll_rules(self):
        return self._enroll_rules

    @enroll_rules.setter
    def enroll_rules(self, value):
        if isinstance(value, list):
            self._enroll_rules = list()
            for i in value:
                if isinstance(i, RecruitEnrollRule):
                    self._enroll_rules.append(i)
                else:
                    self._enroll_rules.append(RecruitEnrollRule.from_alipay_dict(i))
    @property
    def enroll_start_time(self):
        return self._enroll_start_time

    @enroll_start_time.setter
    def enroll_start_time(self, value):
        self._enroll_start_time = value
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def plan_name(self):
        return self._plan_name

    @plan_name.setter
    def plan_name(self, value):
        self._plan_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingRecruitPlanQueryResponse, self).parse_response_content(response_content)
        if 'description' in response:
            self.description = response['description']
        if 'enroll_end_time' in response:
            self.enroll_end_time = response['enroll_end_time']
        if 'enroll_rules' in response:
            self.enroll_rules = response['enroll_rules']
        if 'enroll_start_time' in response:
            self.enroll_start_time = response['enroll_start_time']
        if 'logo' in response:
            self.logo = response['logo']
        if 'plan_id' in response:
            self.plan_id = response['plan_id']
        if 'plan_name' in response:
            self.plan_name = response['plan_name']
        if 'status' in response:
            self.status = response['status']
