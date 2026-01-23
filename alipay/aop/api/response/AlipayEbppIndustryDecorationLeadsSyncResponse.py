#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppIndustryDecorationLeadsSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryDecorationLeadsSyncResponse, self).__init__()
        self._leads_feedback = None

    @property
    def leads_feedback(self):
        return self._leads_feedback

    @leads_feedback.setter
    def leads_feedback(self, value):
        self._leads_feedback = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryDecorationLeadsSyncResponse, self).parse_response_content(response_content)
        if 'leads_feedback' in response:
            self.leads_feedback = response['leads_feedback']
