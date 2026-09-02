#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EliminationRuleDetailItem import EliminationRuleDetailItem
from alipay.aop.api.domain.ReportUrlItem import ReportUrlItem


class AlipayEbppJobinterviewInterviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppJobinterviewInterviewQueryResponse, self).__init__()
        self._candidate_id = None
        self._elimination_rule_detail = None
        self._external_candidate_id = None
        self._initiate_start_time = None
        self._interview_end_time = None
        self._interview_qualified = None
        self._interview_start_time = None
        self._interview_summary = None
        self._interview_url = None
        self._report_generation_time = None
        self._report_url_list = None
        self._room_expire_time = None
        self._score = None
        self._status = None

    @property
    def candidate_id(self):
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, value):
        self._candidate_id = value
    @property
    def elimination_rule_detail(self):
        return self._elimination_rule_detail

    @elimination_rule_detail.setter
    def elimination_rule_detail(self, value):
        if isinstance(value, EliminationRuleDetailItem):
            self._elimination_rule_detail = value
        else:
            self._elimination_rule_detail = EliminationRuleDetailItem.from_alipay_dict(value)
    @property
    def external_candidate_id(self):
        return self._external_candidate_id

    @external_candidate_id.setter
    def external_candidate_id(self, value):
        self._external_candidate_id = value
    @property
    def initiate_start_time(self):
        return self._initiate_start_time

    @initiate_start_time.setter
    def initiate_start_time(self, value):
        self._initiate_start_time = value
    @property
    def interview_end_time(self):
        return self._interview_end_time

    @interview_end_time.setter
    def interview_end_time(self, value):
        self._interview_end_time = value
    @property
    def interview_qualified(self):
        return self._interview_qualified

    @interview_qualified.setter
    def interview_qualified(self, value):
        self._interview_qualified = value
    @property
    def interview_start_time(self):
        return self._interview_start_time

    @interview_start_time.setter
    def interview_start_time(self, value):
        self._interview_start_time = value
    @property
    def interview_summary(self):
        return self._interview_summary

    @interview_summary.setter
    def interview_summary(self, value):
        self._interview_summary = value
    @property
    def interview_url(self):
        return self._interview_url

    @interview_url.setter
    def interview_url(self, value):
        self._interview_url = value
    @property
    def report_generation_time(self):
        return self._report_generation_time

    @report_generation_time.setter
    def report_generation_time(self, value):
        self._report_generation_time = value
    @property
    def report_url_list(self):
        return self._report_url_list

    @report_url_list.setter
    def report_url_list(self, value):
        if isinstance(value, ReportUrlItem):
            self._report_url_list = value
        else:
            self._report_url_list = ReportUrlItem.from_alipay_dict(value)
    @property
    def room_expire_time(self):
        return self._room_expire_time

    @room_expire_time.setter
    def room_expire_time(self, value):
        self._room_expire_time = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppJobinterviewInterviewQueryResponse, self).parse_response_content(response_content)
        if 'candidate_id' in response:
            self.candidate_id = response['candidate_id']
        if 'elimination_rule_detail' in response:
            self.elimination_rule_detail = response['elimination_rule_detail']
        if 'external_candidate_id' in response:
            self.external_candidate_id = response['external_candidate_id']
        if 'initiate_start_time' in response:
            self.initiate_start_time = response['initiate_start_time']
        if 'interview_end_time' in response:
            self.interview_end_time = response['interview_end_time']
        if 'interview_qualified' in response:
            self.interview_qualified = response['interview_qualified']
        if 'interview_start_time' in response:
            self.interview_start_time = response['interview_start_time']
        if 'interview_summary' in response:
            self.interview_summary = response['interview_summary']
        if 'interview_url' in response:
            self.interview_url = response['interview_url']
        if 'report_generation_time' in response:
            self.report_generation_time = response['report_generation_time']
        if 'report_url_list' in response:
            self.report_url_list = response['report_url_list']
        if 'room_expire_time' in response:
            self.room_expire_time = response['room_expire_time']
        if 'score' in response:
            self.score = response['score']
        if 'status' in response:
            self.status = response['status']
