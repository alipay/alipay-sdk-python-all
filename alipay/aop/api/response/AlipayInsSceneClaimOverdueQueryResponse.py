#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneClaimOverdueQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneClaimOverdueQueryResponse, self).__init__()
        self._amount = None
        self._claim_no = None
        self._out_order_id = None
        self._overdue_finished_time = None
        self._overdue_no = None
        self._partner_org_id = None
        self._pay_flow_id = None
        self._pay_flow_type = None
        self._policy_no = None
        self._report_no = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def overdue_finished_time(self):
        return self._overdue_finished_time

    @overdue_finished_time.setter
    def overdue_finished_time(self, value):
        self._overdue_finished_time = value
    @property
    def overdue_no(self):
        return self._overdue_no

    @overdue_no.setter
    def overdue_no(self, value):
        self._overdue_no = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value
    @property
    def pay_flow_id(self):
        return self._pay_flow_id

    @pay_flow_id.setter
    def pay_flow_id(self, value):
        self._pay_flow_id = value
    @property
    def pay_flow_type(self):
        return self._pay_flow_type

    @pay_flow_type.setter
    def pay_flow_type(self, value):
        self._pay_flow_type = value
    @property
    def policy_no(self):
        return self._policy_no

    @policy_no.setter
    def policy_no(self, value):
        self._policy_no = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneClaimOverdueQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'claim_no' in response:
            self.claim_no = response['claim_no']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'overdue_finished_time' in response:
            self.overdue_finished_time = response['overdue_finished_time']
        if 'overdue_no' in response:
            self.overdue_no = response['overdue_no']
        if 'partner_org_id' in response:
            self.partner_org_id = response['partner_org_id']
        if 'pay_flow_id' in response:
            self.pay_flow_id = response['pay_flow_id']
        if 'pay_flow_type' in response:
            self.pay_flow_type = response['pay_flow_type']
        if 'policy_no' in response:
            self.policy_no = response['policy_no']
        if 'report_no' in response:
            self.report_no = response['report_no']
        if 'status' in response:
            self.status = response['status']
