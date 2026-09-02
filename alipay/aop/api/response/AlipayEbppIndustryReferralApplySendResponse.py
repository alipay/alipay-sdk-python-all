#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryReferralApplySendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryReferralApplySendResponse, self).__init__()
        self._accepted = None
        self._reject_reason = None

    @property
    def accepted(self):
        return self._accepted

    @accepted.setter
    def accepted(self, value):
        self._accepted = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryReferralApplySendResponse, self).parse_response_content(response_content)
        if 'accepted' in response:
            self.accepted = response['accepted']
        if 'reject_reason' in response:
            self.reject_reason = response['reject_reason']
