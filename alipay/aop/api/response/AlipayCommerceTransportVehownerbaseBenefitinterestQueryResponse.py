#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BenefitInterestInfoResponse import BenefitInterestInfoResponse


class AlipayCommerceTransportVehownerbaseBenefitinterestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportVehownerbaseBenefitinterestQueryResponse, self).__init__()
        self._benefit_id = None
        self._benefit_interest_info = None
        self._benefit_status = None
        self._effective_end_time = None
        self._effective_start_time = None
        self._operator_user_id = None
        self._orderStr = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def benefit_interest_info(self):
        return self._benefit_interest_info

    @benefit_interest_info.setter
    def benefit_interest_info(self, value):
        if isinstance(value, BenefitInterestInfoResponse):
            self._benefit_interest_info = value
        else:
            self._benefit_interest_info = BenefitInterestInfoResponse.from_alipay_dict(value)
    @property
    def benefit_status(self):
        return self._benefit_status

    @benefit_status.setter
    def benefit_status(self, value):
        self._benefit_status = value
    @property
    def effective_end_time(self):
        return self._effective_end_time

    @effective_end_time.setter
    def effective_end_time(self, value):
        self._effective_end_time = value
    @property
    def effective_start_time(self):
        return self._effective_start_time

    @effective_start_time.setter
    def effective_start_time(self, value):
        self._effective_start_time = value
    @property
    def operator_user_id(self):
        return self._operator_user_id

    @operator_user_id.setter
    def operator_user_id(self, value):
        self._operator_user_id = value
    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportVehownerbaseBenefitinterestQueryResponse, self).parse_response_content(response_content)
        if 'benefit_id' in response:
            self.benefit_id = response['benefit_id']
        if 'benefit_interest_info' in response:
            self.benefit_interest_info = response['benefit_interest_info']
        if 'benefit_status' in response:
            self.benefit_status = response['benefit_status']
        if 'effective_end_time' in response:
            self.effective_end_time = response['effective_end_time']
        if 'effective_start_time' in response:
            self.effective_start_time = response['effective_start_time']
        if 'operator_user_id' in response:
            self.operator_user_id = response['operator_user_id']
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
