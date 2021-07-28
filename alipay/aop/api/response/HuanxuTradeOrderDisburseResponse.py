#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtContext import ExtContext


class HuanxuTradeOrderDisburseResponse(AlipayResponse):

    def __init__(self):
        super(HuanxuTradeOrderDisburseResponse, self).__init__()
        self._channel = None
        self._disburse_amount = None
        self._disburse_id = None
        self._disburse_request_no = None
        self._disburse_status = None
        self._ext_context = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def disburse_amount(self):
        return self._disburse_amount

    @disburse_amount.setter
    def disburse_amount(self, value):
        self._disburse_amount = value
    @property
    def disburse_id(self):
        return self._disburse_id

    @disburse_id.setter
    def disburse_id(self, value):
        self._disburse_id = value
    @property
    def disburse_request_no(self):
        return self._disburse_request_no

    @disburse_request_no.setter
    def disburse_request_no(self, value):
        self._disburse_request_no = value
    @property
    def disburse_status(self):
        return self._disburse_status

    @disburse_status.setter
    def disburse_status(self, value):
        self._disburse_status = value
    @property
    def ext_context(self):
        return self._ext_context

    @ext_context.setter
    def ext_context(self, value):
        if isinstance(value, ExtContext):
            self._ext_context = value
        else:
            self._ext_context = ExtContext.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(HuanxuTradeOrderDisburseResponse, self).parse_response_content(response_content)
        if 'channel' in response:
            self.channel = response['channel']
        if 'disburse_amount' in response:
            self.disburse_amount = response['disburse_amount']
        if 'disburse_id' in response:
            self.disburse_id = response['disburse_id']
        if 'disburse_request_no' in response:
            self.disburse_request_no = response['disburse_request_no']
        if 'disburse_status' in response:
            self.disburse_status = response['disburse_status']
        if 'ext_context' in response:
            self.ext_context = response['ext_context']
