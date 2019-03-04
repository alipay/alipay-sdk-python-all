#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MActivityDetailInfo import MActivityDetailInfo


class KoubeiMarketingCampaignMerchantActivityModifyResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignMerchantActivityModifyResponse, self).__init__()
        self._activity_detail_info = None

    @property
    def activity_detail_info(self):
        return self._activity_detail_info

    @activity_detail_info.setter
    def activity_detail_info(self, value):
        if isinstance(value, MActivityDetailInfo):
            self._activity_detail_info = value
        else:
            self._activity_detail_info = MActivityDetailInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignMerchantActivityModifyResponse, self).parse_response_content(response_content)
        if 'activity_detail_info' in response:
            self.activity_detail_info = response['activity_detail_info']
