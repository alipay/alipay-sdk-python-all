#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointVoucherprodBenefittemplateAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointVoucherprodBenefittemplateAddResponse, self).__init__()
        self._append_amount = None
        self._bill_no = None

    @property
    def append_amount(self):
        return self._append_amount

    @append_amount.setter
    def append_amount(self, value):
        self._append_amount = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointVoucherprodBenefittemplateAddResponse, self).parse_response_content(response_content)
        if 'append_amount' in response:
            self.append_amount = response['append_amount']
        if 'bill_no' in response:
            self.bill_no = response['bill_no']
