#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Voucher import Voucher


class KoubeiMarketingCampaignVoucherDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignVoucherDetailQueryResponse, self).__init__()
        self._status = None
        self._voucher = None
        self._voucher_id = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, Voucher):
            self._voucher = value
        else:
            self._voucher = Voucher.from_alipay_dict(value)
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignVoucherDetailQueryResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
        if 'voucher' in response:
            self.voucher = response['voucher']
        if 'voucher_id' in response:
            self.voucher_id = response['voucher_id']
