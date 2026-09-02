#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalMemberBenefitlinkQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalMemberBenefitlinkQueryResponse, self).__init__()
        self._link = None

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        self._link = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalMemberBenefitlinkQueryResponse, self).parse_response_content(response_content)
        if 'link' in response:
            self.link = response['link']
