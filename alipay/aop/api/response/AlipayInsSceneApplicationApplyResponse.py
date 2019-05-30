#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneApplicationApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneApplicationApplyResponse, self).__init__()
        self._application_no = None
        self._operation_id = None
        self._out_biz_no = None
        self._policy_detail_url_4_mobile = None
        self._policy_detail_url_4_pc = None
        self._policy_no = None
        self._trade_no = None
        self._trade_type = None
        self._underwrite_reject_reason = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def policy_detail_url_4_mobile(self):
        return self._policy_detail_url_4_mobile

    @policy_detail_url_4_mobile.setter
    def policy_detail_url_4_mobile(self, value):
        self._policy_detail_url_4_mobile = value
    @property
    def policy_detail_url_4_pc(self):
        return self._policy_detail_url_4_pc

    @policy_detail_url_4_pc.setter
    def policy_detail_url_4_pc(self, value):
        self._policy_detail_url_4_pc = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
    @property
    def underwrite_reject_reason(self):
        return self._underwrite_reject_reason

    @underwrite_reject_reason.setter
    def underwrite_reject_reason(self, value):
        self._underwrite_reject_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneApplicationApplyResponse, self).parse_response_content(response_content)
        if 'application_no' in response:
            self.application_no = response['application_no']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'policy_detail_url_4_mobile' in response:
            self.policy_detail_url_4_mobile = response['policy_detail_url_4_mobile']
        if 'policy_detail_url_4_pc' in response:
            self.policy_detail_url_4_pc = response['policy_detail_url_4_pc']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_type' in response:
            self.trade_type = response['trade_type']
        if 'underwrite_reject_reason' in response:
            self.underwrite_reject_reason = response['underwrite_reject_reason']
