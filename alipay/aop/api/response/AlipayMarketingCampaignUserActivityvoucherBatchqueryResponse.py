#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityVoucherInfo import ActivityVoucherInfo


class AlipayMarketingCampaignUserActivityvoucherBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUserActivityvoucherBatchqueryResponse, self).__init__()
        self._activity_voucher_list = None

    @property
    def activity_voucher_list(self):
        return self._activity_voucher_list

    @activity_voucher_list.setter
    def activity_voucher_list(self, value):
        if isinstance(value, list):
            self._activity_voucher_list = list()
            for i in value:
                if isinstance(i, ActivityVoucherInfo):
                    self._activity_voucher_list.append(i)
                else:
                    self._activity_voucher_list.append(ActivityVoucherInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUserActivityvoucherBatchqueryResponse, self).parse_response_content(response_content)
        if 'activity_voucher_list' in response:
            self.activity_voucher_list = response['activity_voucher_list']
