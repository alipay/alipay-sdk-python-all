#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCashitemvoucherTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCashitemvoucherTemplateCreateResponse, self).__init__()
        self._confirm_uri = None
        self._fund_order_no = None
        self._template_id = None
        self._voucher_discount_limit = None

    @property
    def confirm_uri(self):
        return self._confirm_uri

    @confirm_uri.setter
    def confirm_uri(self, value):
        self._confirm_uri = value
    @property
    def fund_order_no(self):
        return self._fund_order_no

    @fund_order_no.setter
    def fund_order_no(self, value):
        self._fund_order_no = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def voucher_discount_limit(self):
        return self._voucher_discount_limit

    @voucher_discount_limit.setter
    def voucher_discount_limit(self, value):
        self._voucher_discount_limit = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCashitemvoucherTemplateCreateResponse, self).parse_response_content(response_content)
        if 'confirm_uri' in response:
            self.confirm_uri = response['confirm_uri']
        if 'fund_order_no' in response:
            self.fund_order_no = response['fund_order_no']
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'voucher_discount_limit' in response:
            self.voucher_discount_limit = response['voucher_discount_limit']
