#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransThirdpartyRewardQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransThirdpartyRewardQueryResponse, self).__init__()
        self._amount = None
        self._error_msg = None
        self._last_modified = None
        self._receiver_user_id = None
        self._sender_user_id = None
        self._status = None
        self._transfer_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, value):
        self._last_modified = value
    @property
    def receiver_user_id(self):
        return self._receiver_user_id

    @receiver_user_id.setter
    def receiver_user_id(self, value):
        self._receiver_user_id = value
    @property
    def sender_user_id(self):
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, value):
        self._sender_user_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def transfer_no(self):
        return self._transfer_no

    @transfer_no.setter
    def transfer_no(self, value):
        self._transfer_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransThirdpartyRewardQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'last_modified' in response:
            self.last_modified = response['last_modified']
        if 'receiver_user_id' in response:
            self.receiver_user_id = response['receiver_user_id']
        if 'sender_user_id' in response:
            self.sender_user_id = response['sender_user_id']
        if 'status' in response:
            self.status = response['status']
        if 'transfer_no' in response:
            self.transfer_no = response['transfer_no']
