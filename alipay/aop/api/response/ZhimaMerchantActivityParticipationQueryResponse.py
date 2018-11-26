#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityParticipation import ActivityParticipation


class ZhimaMerchantActivityParticipationQueryResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantActivityParticipationQueryResponse, self).__init__()
        self._activity_participation = None

    @property
    def activity_participation(self):
        return self._activity_participation

    @activity_participation.setter
    def activity_participation(self, value):
        if isinstance(value, ActivityParticipation):
            self._activity_participation = value
        else:
            self._activity_participation = ActivityParticipation.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantActivityParticipationQueryResponse, self).parse_response_content(response_content)
        if 'activity_participation' in response:
            self.activity_participation = response['activity_participation']
