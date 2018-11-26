#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityParticipation import ActivityParticipation


class ZhimaMerchantActivityParticipatedQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantActivityParticipatedQueryResponse, self).__init__()
        self._activity_participation_list = None

    @property
    def activity_participation_list(self):
        return self._activity_participation_list

    @activity_participation_list.setter
    def activity_participation_list(self, value):
        if isinstance(value, list):
            self._activity_participation_list = list()
            for i in value:
                if isinstance(i, ActivityParticipation):
                    self._activity_participation_list.append(i)
                else:
                    self._activity_participation_list.append(ActivityParticipation.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantActivityParticipatedQueryResponse, self).parse_response_content(response_content)
        if 'activity_participation_list' in response:
            self.activity_participation_list = response['activity_participation_list']
