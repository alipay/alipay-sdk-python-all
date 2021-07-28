#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOverseasRemitFundInitializeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOverseasRemitFundInitializeResponse, self).__init__()
        self._compliance_check_result = None
        self._compliance_check_result_info = None
        self._compliance_result_signature = None
        self._extend_info = None
        self._external_biz_no = None
        self._receiver_mid = None
        self._sender_mid = None

    @property
    def compliance_check_result(self):
        return self._compliance_check_result

    @compliance_check_result.setter
    def compliance_check_result(self, value):
        self._compliance_check_result = value
    @property
    def compliance_check_result_info(self):
        return self._compliance_check_result_info

    @compliance_check_result_info.setter
    def compliance_check_result_info(self, value):
        self._compliance_check_result_info = value
    @property
    def compliance_result_signature(self):
        return self._compliance_result_signature

    @compliance_result_signature.setter
    def compliance_result_signature(self, value):
        self._compliance_result_signature = value
    @property
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
    @property
    def external_biz_no(self):
        return self._external_biz_no

    @external_biz_no.setter
    def external_biz_no(self, value):
        self._external_biz_no = value
    @property
    def receiver_mid(self):
        return self._receiver_mid

    @receiver_mid.setter
    def receiver_mid(self, value):
        self._receiver_mid = value
    @property
    def sender_mid(self):
        return self._sender_mid

    @sender_mid.setter
    def sender_mid(self, value):
        self._sender_mid = value

    def parse_response_content(self, response_content):
        response = super(AlipayOverseasRemitFundInitializeResponse, self).parse_response_content(response_content)
        if 'compliance_check_result' in response:
            self.compliance_check_result = response['compliance_check_result']
        if 'compliance_check_result_info' in response:
            self.compliance_check_result_info = response['compliance_check_result_info']
        if 'compliance_result_signature' in response:
            self.compliance_result_signature = response['compliance_result_signature']
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'external_biz_no' in response:
            self.external_biz_no = response['external_biz_no']
        if 'receiver_mid' in response:
            self.receiver_mid = response['receiver_mid']
        if 'sender_mid' in response:
            self.sender_mid = response['sender_mid']
