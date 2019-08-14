#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCashlessitemvoucherTemplateCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCashlessitemvoucherTemplateCreateResponse, self).__init__()
        self._template_id = None
        self._voucher_discount_limit = None

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
        response = super(AlipayMarketingCashlessitemvoucherTemplateCreateResponse, self).parse_response_content(response_content)
        if 'template_id' in response:
            self.template_id = response['template_id']
        if 'voucher_discount_limit' in response:
            self.voucher_discount_limit = response['voucher_discount_limit']
