#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaCustomerGrowthTaskawardQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaCustomerGrowthTaskawardQueryResponse, self).__init__()
        self._award_type = None
        self._award_value = None

    @property
    def award_type(self):
        return self._award_type

    @award_type.setter
    def award_type(self, value):
        self._award_type = value
    @property
    def award_value(self):
        return self._award_value

    @award_value.setter
    def award_value(self, value):
        self._award_value = value

    def parse_response_content(self, response_content):
        response = super(ZhimaCustomerGrowthTaskawardQueryResponse, self).parse_response_content(response_content)
        if 'award_type' in response:
            self.award_type = response['award_type']
        if 'award_value' in response:
            self.award_value = response['award_value']
