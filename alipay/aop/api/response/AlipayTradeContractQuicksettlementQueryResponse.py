#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeContractQuicksettlementQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeContractQuicksettlementQueryResponse, self).__init__()
        self._credit_quota = None
        self._left_advance_quota = None
        self._left_credit_quota = None
        self._service_state = None
        self._signed = None

    @property
    def credit_quota(self):
        return self._credit_quota

    @credit_quota.setter
    def credit_quota(self, value):
        self._credit_quota = value
    @property
    def left_advance_quota(self):
        return self._left_advance_quota

    @left_advance_quota.setter
    def left_advance_quota(self, value):
        self._left_advance_quota = value
    @property
    def left_credit_quota(self):
        return self._left_credit_quota

    @left_credit_quota.setter
    def left_credit_quota(self, value):
        self._left_credit_quota = value
    @property
    def service_state(self):
        return self._service_state

    @service_state.setter
    def service_state(self, value):
        self._service_state = value
    @property
    def signed(self):
        return self._signed

    @signed.setter
    def signed(self, value):
        self._signed = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeContractQuicksettlementQueryResponse, self).parse_response_content(response_content)
        if 'credit_quota' in response:
            self.credit_quota = response['credit_quota']
        if 'left_advance_quota' in response:
            self.left_advance_quota = response['left_advance_quota']
        if 'left_credit_quota' in response:
            self.left_credit_quota = response['left_credit_quota']
        if 'service_state' in response:
            self.service_state = response['service_state']
        if 'signed' in response:
            self.signed = response['signed']
