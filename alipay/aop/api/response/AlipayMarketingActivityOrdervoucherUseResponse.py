#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherUseDetailResultInfo import VoucherUseDetailResultInfo


class AlipayMarketingActivityOrdervoucherUseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingActivityOrdervoucherUseResponse, self).__init__()
        self._activity_id = None
        self._voucher_use_detail_result_info = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def voucher_use_detail_result_info(self):
        return self._voucher_use_detail_result_info

    @voucher_use_detail_result_info.setter
    def voucher_use_detail_result_info(self, value):
        if isinstance(value, VoucherUseDetailResultInfo):
            self._voucher_use_detail_result_info = value
        else:
            self._voucher_use_detail_result_info = VoucherUseDetailResultInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingActivityOrdervoucherUseResponse, self).parse_response_content(response_content)
        if 'activity_id' in response:
            self.activity_id = response['activity_id']
        if 'voucher_use_detail_result_info' in response:
            self.voucher_use_detail_result_info = response['voucher_use_detail_result_info']
