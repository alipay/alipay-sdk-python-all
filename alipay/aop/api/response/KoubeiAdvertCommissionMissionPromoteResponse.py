#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbAdvertAdvResponse import KbAdvertAdvResponse


class KoubeiAdvertCommissionMissionPromoteResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertCommissionMissionPromoteResponse, self).__init__()
        self._advert = None
        self._can_cascade_mission = None

    @property
    def advert(self):
        return self._advert

    @advert.setter
    def advert(self, value):
        if isinstance(value, KbAdvertAdvResponse):
            self._advert = value
        else:
            self._advert = KbAdvertAdvResponse.from_alipay_dict(value)
    @property
    def can_cascade_mission(self):
        return self._can_cascade_mission

    @can_cascade_mission.setter
    def can_cascade_mission(self, value):
        self._can_cascade_mission = value

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertCommissionMissionPromoteResponse, self).parse_response_content(response_content)
        if 'advert' in response:
            self.advert = response['advert']
        if 'can_cascade_mission' in response:
            self.can_cascade_mission = response['can_cascade_mission']
