#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ActivityPeriodInfo import ActivityPeriodInfo
from alipay.aop.api.domain.ActivityPeriodInfo import ActivityPeriodInfo


class AlipayCommerceOperationPromoActivityperiodQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoActivityperiodQueryResponse, self).__init__()
        self._current_activity = None
        self._next_activity = None

    @property
    def current_activity(self):
        return self._current_activity

    @current_activity.setter
    def current_activity(self, value):
        if isinstance(value, ActivityPeriodInfo):
            self._current_activity = value
        else:
            self._current_activity = ActivityPeriodInfo.from_alipay_dict(value)
    @property
    def next_activity(self):
        return self._next_activity

    @next_activity.setter
    def next_activity(self, value):
        if isinstance(value, ActivityPeriodInfo):
            self._next_activity = value
        else:
            self._next_activity = ActivityPeriodInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoActivityperiodQueryResponse, self).parse_response_content(response_content)
        if 'current_activity' in response:
            self.current_activity = response['current_activity']
        if 'next_activity' in response:
            self.next_activity = response['next_activity']
