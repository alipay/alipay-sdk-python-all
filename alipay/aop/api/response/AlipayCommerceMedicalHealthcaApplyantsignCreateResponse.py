#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntSignResult import AntSignResult


class AlipayCommerceMedicalHealthcaApplyantsignCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHealthcaApplyantsignCreateResponse, self).__init__()
        self._ant_sign_result_list = None
        self._biz_no = None
        self._sign_flow_id = None

    @property
    def ant_sign_result_list(self):
        return self._ant_sign_result_list

    @ant_sign_result_list.setter
    def ant_sign_result_list(self, value):
        if isinstance(value, list):
            self._ant_sign_result_list = list()
            for i in value:
                if isinstance(i, AntSignResult):
                    self._ant_sign_result_list.append(i)
                else:
                    self._ant_sign_result_list.append(AntSignResult.from_alipay_dict(i))
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHealthcaApplyantsignCreateResponse, self).parse_response_content(response_content)
        if 'ant_sign_result_list' in response:
            self.ant_sign_result_list = response['ant_sign_result_list']
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'sign_flow_id' in response:
            self.sign_flow_id = response['sign_flow_id']
