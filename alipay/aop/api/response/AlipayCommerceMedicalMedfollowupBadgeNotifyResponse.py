#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMedfollowupBadgeNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMedfollowupBadgeNotifyResponse, self).__init__()
        self._notify = None

    @property
    def notify(self):
        return self._notify

    @notify.setter
    def notify(self, value):
        self._notify = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMedfollowupBadgeNotifyResponse, self).parse_response_content(response_content)
        if 'notify' in response:
            self.notify = response['notify']
