#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndustryExtendField import IndustryExtendField


class AlipayEbppIndustryBillNettingRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryBillNettingRefundResponse, self).__init__()
        self._alipay_bill_no = None
        self._industry_extend_field_list = None

    @property
    def alipay_bill_no(self):
        return self._alipay_bill_no

    @alipay_bill_no.setter
    def alipay_bill_no(self, value):
        self._alipay_bill_no = value
    @property
    def industry_extend_field_list(self):
        return self._industry_extend_field_list

    @industry_extend_field_list.setter
    def industry_extend_field_list(self, value):
        if isinstance(value, list):
            self._industry_extend_field_list = list()
            for i in value:
                if isinstance(i, IndustryExtendField):
                    self._industry_extend_field_list.append(i)
                else:
                    self._industry_extend_field_list.append(IndustryExtendField.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryBillNettingRefundResponse, self).parse_response_content(response_content)
        if 'alipay_bill_no' in response:
            self.alipay_bill_no = response['alipay_bill_no']
        if 'industry_extend_field_list' in response:
            self.industry_extend_field_list = response['industry_extend_field_list']
