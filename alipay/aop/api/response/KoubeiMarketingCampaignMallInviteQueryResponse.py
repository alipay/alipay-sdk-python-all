#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityPlanInfo import ActivityPlanInfo


class KoubeiMarketingCampaignMallInviteQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignMallInviteQueryResponse, self).__init__()
        self._activity_plan_info_list = None

    @property
    def activity_plan_info_list(self):
        return self._activity_plan_info_list

    @activity_plan_info_list.setter
    def activity_plan_info_list(self, value):
        if isinstance(value, list):
            self._activity_plan_info_list = list()
            for i in value:
                if isinstance(i, ActivityPlanInfo):
                    self._activity_plan_info_list.append(i)
                else:
                    self._activity_plan_info_list.append(ActivityPlanInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignMallInviteQueryResponse, self).parse_response_content(response_content)
        if 'activity_plan_info_list' in response:
            self.activity_plan_info_list = response['activity_plan_info_list']
