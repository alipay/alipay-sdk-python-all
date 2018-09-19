#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CaseInfoCode import CaseInfoCode


class AlipayInsDataAutoFraudQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsDataAutoFraudQueryResponse, self).__init__()
        self._fraud_tag = None
        self._fraud_tag_level = None
        self._info_code_list = None

    @property
    def fraud_tag(self):
        return self._fraud_tag

    @fraud_tag.setter
    def fraud_tag(self, value):
        self._fraud_tag = value
    @property
    def fraud_tag_level(self):
        return self._fraud_tag_level

    @fraud_tag_level.setter
    def fraud_tag_level(self, value):
        self._fraud_tag_level = value
    @property
    def info_code_list(self):
        return self._info_code_list

    @info_code_list.setter
    def info_code_list(self, value):
        if isinstance(value, list):
            self._info_code_list = list()
            for i in value:
                if isinstance(i, CaseInfoCode):
                    self._info_code_list.append(i)
                else:
                    self._info_code_list.append(CaseInfoCode.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayInsDataAutoFraudQueryResponse, self).parse_response_content(response_content)
        if 'fraud_tag' in response:
            self.fraud_tag = response['fraud_tag']
        if 'fraud_tag_level' in response:
            self.fraud_tag_level = response['fraud_tag_level']
        if 'info_code_list' in response:
            self.info_code_list = response['info_code_list']
