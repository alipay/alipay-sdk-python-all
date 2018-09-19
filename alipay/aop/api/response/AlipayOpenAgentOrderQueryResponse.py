#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAgentOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAgentOrderQueryResponse, self).__init__()
        self._agent_app_id = None
        self._confirm_url = None
        self._merchant_pid = None
        self._order_status = None
        self._reject_reason = None

    @property
    def agent_app_id(self):
        return self._agent_app_id

    @agent_app_id.setter
    def agent_app_id(self, value):
        self._agent_app_id = value
    @property
    def confirm_url(self):
        return self._confirm_url

    @confirm_url.setter
    def confirm_url(self, value):
        self._confirm_url = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAgentOrderQueryResponse, self).parse_response_content(response_content)
        if 'agent_app_id' in response:
            self.agent_app_id = response['agent_app_id']
        if 'confirm_url' in response:
            self.confirm_url = response['confirm_url']
        if 'merchant_pid' in response:
            self.merchant_pid = response['merchant_pid']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
