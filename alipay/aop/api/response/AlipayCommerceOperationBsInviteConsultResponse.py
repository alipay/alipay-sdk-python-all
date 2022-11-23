#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceOperationBsInviteConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationBsInviteConsultResponse, self).__init__()
        self._invitable = None

    @property
    def invitable(self):
        return self._invitable

    @invitable.setter
    def invitable(self, value):
        self._invitable = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationBsInviteConsultResponse, self).parse_response_content(response_content)
        if 'invitable' in response:
            self.invitable = response['invitable']
