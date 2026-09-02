#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarLeadsBizstatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarLeadsBizstatusQueryResponse, self).__init__()
        self._leads_biz_status = None

    @property
    def leads_biz_status(self):
        return self._leads_biz_status

    @leads_biz_status.setter
    def leads_biz_status(self, value):
        self._leads_biz_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarLeadsBizstatusQueryResponse, self).parse_response_content(response_content)
        if 'leads_biz_status' in response:
            self.leads_biz_status = response['leads_biz_status']
