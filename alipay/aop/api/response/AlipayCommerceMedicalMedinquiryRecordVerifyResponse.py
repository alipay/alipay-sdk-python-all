#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.InquiryBizContent import InquiryBizContent


class AlipayCommerceMedicalMedinquiryRecordVerifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedinquiryRecordVerifyResponse, self).__init__()
        self._data = None
        self._orderStr = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, InquiryBizContent):
            self._data = value
        else:
            self._data = InquiryBizContent.from_alipay_dict(value)
    @property
    def orderStr(self):
        return self._orderStr

    @orderStr.setter
    def orderStr(self, value):
        self._orderStr = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedinquiryRecordVerifyResponse, self).parse_response_content(response_content)
        if 'data' in response:
            self.data = response['data']
        if 'orderStr' in response:
            self.orderStr = response['orderStr']
