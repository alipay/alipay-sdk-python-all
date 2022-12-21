#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UnitedVoucherDetail import UnitedVoucherDetail


class AlipayMarketingCampaignUnitedopencouponRecordQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUnitedopencouponRecordQueryResponse, self).__init__()
        self._login_id = None
        self._voucher_details = None

    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value
    @property
    def voucher_details(self):
        return self._voucher_details

    @voucher_details.setter
    def voucher_details(self, value):
        if isinstance(value, list):
            self._voucher_details = list()
            for i in value:
                if isinstance(i, UnitedVoucherDetail):
                    self._voucher_details.append(i)
                else:
                    self._voucher_details.append(UnitedVoucherDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUnitedopencouponRecordQueryResponse, self).parse_response_content(response_content)
        if 'login_id' in response:
            self.login_id = response['login_id']
        if 'voucher_details' in response:
            self.voucher_details = response['voucher_details']
