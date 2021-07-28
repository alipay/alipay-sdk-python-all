#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotbpaasLavidabilldetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotbpaasLavidabilldetailQueryResponse, self).__init__()
        self._biz_no = None
        self._biz_order_amt = None
        self._mercht_disc_amt = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def biz_order_amt(self):
        return self._biz_order_amt

    @biz_order_amt.setter
    def biz_order_amt(self, value):
        self._biz_order_amt = value
    @property
    def mercht_disc_amt(self):
        return self._mercht_disc_amt

    @mercht_disc_amt.setter
    def mercht_disc_amt(self, value):
        self._mercht_disc_amt = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotbpaasLavidabilldetailQueryResponse, self).parse_response_content(response_content)
        if 'biz_no' in response:
            self.biz_no = response['biz_no']
        if 'biz_order_amt' in response:
            self.biz_order_amt = response['biz_order_amt']
        if 'mercht_disc_amt' in response:
            self.mercht_disc_amt = response['mercht_disc_amt']
