#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenOperationPartnerIdentityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenOperationPartnerIdentityQueryResponse, self).__init__()
        self._certified = None
        self._master = None
        self._settled = None

    @property
    def certified(self):
        return self._certified

    @certified.setter
    def certified(self, value):
        self._certified = value
    @property
    def master(self):
        return self._master

    @master.setter
    def master(self, value):
        self._master = value
    @property
    def settled(self):
        return self._settled

    @settled.setter
    def settled(self, value):
        self._settled = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenOperationPartnerIdentityQueryResponse, self).parse_response_content(response_content)
        if 'certified' in response:
            self.certified = response['certified']
        if 'master' in response:
            self.master = response['master']
        if 'settled' in response:
            self.settled = response['settled']
