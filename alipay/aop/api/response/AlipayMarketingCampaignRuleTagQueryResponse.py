#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMarketingCampaignRuleTagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMarketingCampaignRuleTagQueryResponse, self).__init__()
        self._customtagjson = None
        self._scenetagjson = None

    @property
    def customtagjson(self):
        return self._customtagjson

    @customtagjson.setter
    def customtagjson(self, value):
        self._customtagjson = value
    @property
    def scenetagjson(self):
        return self._scenetagjson

    @scenetagjson.setter
    def scenetagjson(self, value):
        self._scenetagjson = value

    def parse_response_content(self, response_content):
        response = super(AlipayMarketingCampaignRuleTagQueryResponse, self).parse_response_content(response_content)
        if 'customtagjson' in response:
            self.customtagjson = response['customtagjson']
        if 'scenetagjson' in response:
            self.scenetagjson = response['scenetagjson']
