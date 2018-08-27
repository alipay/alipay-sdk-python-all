#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingToolPointsUpdateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingToolPointsUpdateResponse, self).__init__()
        self._point_log_no = None

    @property
    def point_log_no(self):
        return self._point_log_no

    @point_log_no.setter
    def point_log_no(self, value):
        self._point_log_no = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingToolPointsUpdateResponse, self).parse_response_content(response_content)
        if 'point_log_no' in response:
            self.point_log_no = response['point_log_no']
