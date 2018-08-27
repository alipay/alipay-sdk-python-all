#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataEnterpriseStaffinfoUploadResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataEnterpriseStaffinfoUploadResponse, self).__init__()
        self._crowd_id = None

    @property
    def crowd_id(self):
        return self._crowd_id

    @crowd_id.setter
    def crowd_id(self, value):
        self._crowd_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataEnterpriseStaffinfoUploadResponse, self).parse_response_content(response_content)
        if 'crowd_id' in response:
            self.crowd_id = response['crowd_id']
