#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BasicInfo import BasicInfo
from alipay.aop.api.domain.EliminationRuleDetailItem import EliminationRuleDetailItem
from alipay.aop.api.domain.InterviewDetail import InterviewDetail
from alipay.aop.api.domain.ReportUrlItem import ReportUrlItem
from alipay.aop.api.domain.SocialRiskInfo import SocialRiskInfo


class AlipayCommerceCareerJobinterviewQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceCareerJobinterviewQueryResponse, self).__init__()
        self._basic_info = None
        self._elimination_rule_detail = None
        self._initiate_start_time = None
        self._interview_detail = None
        self._interview_end_time = None
        self._interview_qualified = None
        self._interview_start_time = None
        self._interview_summary = None
        self._order_no = None
        self._out_biz_no = None
        self._report_expire_time = None
        self._report_generation_time = None
        self._report_url_list = None
        self._score = None
        self._social_risk_info = None
        self._status = None

    @property
    def basic_info(self):
        return self._basic_info

    @basic_info.setter
    def basic_info(self, value):
        if isinstance(value, BasicInfo):
            self._basic_info = value
        else:
            self._basic_info = BasicInfo.from_alipay_dict(value)
    @property
    def elimination_rule_detail(self):
        return self._elimination_rule_detail

    @elimination_rule_detail.setter
    def elimination_rule_detail(self, value):
        if isinstance(value, list):
            self._elimination_rule_detail = list()
            for i in value:
                if isinstance(i, EliminationRuleDetailItem):
                    self._elimination_rule_detail.append(i)
                else:
                    self._elimination_rule_detail.append(EliminationRuleDetailItem.from_alipay_dict(i))
    @property
    def initiate_start_time(self):
        return self._initiate_start_time

    @initiate_start_time.setter
    def initiate_start_time(self, value):
        self._initiate_start_time = value
    @property
    def interview_detail(self):
        return self._interview_detail

    @interview_detail.setter
    def interview_detail(self, value):
        if isinstance(value, InterviewDetail):
            self._interview_detail = value
        else:
            self._interview_detail = InterviewDetail.from_alipay_dict(value)
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
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def report_expire_time(self):
        return self._report_expire_time

    @report_expire_time.setter
    def report_expire_time(self, value):
        self._report_expire_time = value
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
        if isinstance(value, list):
            self._report_url_list = list()
            for i in value:
                if isinstance(i, ReportUrlItem):
                    self._report_url_list.append(i)
                else:
                    self._report_url_list.append(ReportUrlItem.from_alipay_dict(i))
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def social_risk_info(self):
        return self._social_risk_info

    @social_risk_info.setter
    def social_risk_info(self, value):
        if isinstance(value, SocialRiskInfo):
            self._social_risk_info = value
        else:
            self._social_risk_info = SocialRiskInfo.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceCareerJobinterviewQueryResponse, self).parse_response_content(response_content)
        if 'basic_info' in response:
            self.basic_info = response['basic_info']
        if 'elimination_rule_detail' in response:
            self.elimination_rule_detail = response['elimination_rule_detail']
        if 'initiate_start_time' in response:
            self.initiate_start_time = response['initiate_start_time']
        if 'interview_detail' in response:
            self.interview_detail = response['interview_detail']
        if 'interview_end_time' in response:
            self.interview_end_time = response['interview_end_time']
        if 'interview_qualified' in response:
            self.interview_qualified = response['interview_qualified']
        if 'interview_start_time' in response:
            self.interview_start_time = response['interview_start_time']
        if 'interview_summary' in response:
            self.interview_summary = response['interview_summary']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'report_expire_time' in response:
            self.report_expire_time = response['report_expire_time']
        if 'report_generation_time' in response:
            self.report_generation_time = response['report_generation_time']
        if 'report_url_list' in response:
            self.report_url_list = response['report_url_list']
        if 'score' in response:
            self.score = response['score']
        if 'social_risk_info' in response:
            self.social_risk_info = response['social_risk_info']
        if 'status' in response:
            self.status = response['status']
