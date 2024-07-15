#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryJobInvitationSendResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryJobInvitationSendResponse, self).__init__()
        self._invitation_id = None

    @property
    def invitation_id(self):
        return self._invitation_id

    @invitation_id.setter
    def invitation_id(self, value):
        self._invitation_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryJobInvitationSendResponse, self).parse_response_content(response_content)
        if 'invitation_id' in response:
            self.invitation_id = response['invitation_id']
