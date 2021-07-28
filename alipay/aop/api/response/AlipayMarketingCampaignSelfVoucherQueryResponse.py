#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherItem import VoucherItem


class AlipayMarketingCampaignSelfVoucherQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignSelfVoucherQueryResponse, self).__init__()
        self._voucher_item = None

    @property
    def voucher_item(self):
        return self._voucher_item

    @voucher_item.setter
    def voucher_item(self, value):
        if isinstance(value, VoucherItem):
            self._voucher_item = value
        else:
            self._voucher_item = VoucherItem.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignSelfVoucherQueryResponse, self).parse_response_content(response_content)
        if 'voucher_item' in response:
            self.voucher_item = response['voucher_item']
