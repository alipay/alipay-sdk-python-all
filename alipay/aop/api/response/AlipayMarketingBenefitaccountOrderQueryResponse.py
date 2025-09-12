#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingBenefitaccountOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingBenefitaccountOrderQueryResponse, self).__init__()
        self._biz_no = None
        self._order_no = None
        self._status = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingBenefitaccountOrderQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'status' in response:
            self.status = response['status']
