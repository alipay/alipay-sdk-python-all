#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityConsultInfo import ActivityConsultInfo


class AlipayMarketingCampaignUserVoucherConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignUserVoucherConsultResponse, self).__init__()
        self._activity_consult_list = None

    @property
    def activity_consult_list(self):
        return self._activity_consult_list

    @activity_consult_list.setter
    def activity_consult_list(self, value):
        if isinstance(value, list):
            self._activity_consult_list = list()
            for i in value:
                if isinstance(i, ActivityConsultInfo):
                    self._activity_consult_list.append(i)
                else:
                    self._activity_consult_list.append(ActivityConsultInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignUserVoucherConsultResponse, self).parse_response_content(response_content)
        if 'activity_consult_list' in response:
            self.activity_consult_list = response['activity_consult_list']
