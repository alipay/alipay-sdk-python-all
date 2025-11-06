#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneClaimOverduePreconsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneClaimOverduePreconsultResponse, self).__init__()
        self._admit = None
        self._overdue_pre_consult_flow_id = None
        self._reject_reason = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def overdue_pre_consult_flow_id(self):
        return self._overdue_pre_consult_flow_id

    @overdue_pre_consult_flow_id.setter
    def overdue_pre_consult_flow_id(self, value):
        self._overdue_pre_consult_flow_id = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneClaimOverduePreconsultResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
        if 'overdue_pre_consult_flow_id' in response:
            self.overdue_pre_consult_flow_id = response['overdue_pre_consult_flow_id']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
