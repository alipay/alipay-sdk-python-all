#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointVoucherprodBenefittemplateOfflineResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointVoucherprodBenefittemplateOfflineResponse, self).__init__()
        self._quick_recycle = None

    @property
    def quick_recycle(self):
        return self._quick_recycle

    @quick_recycle.setter
    def quick_recycle(self, value):
        self._quick_recycle = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointVoucherprodBenefittemplateOfflineResponse, self).parse_response_content(response_content)
        if 'quick_recycle' in response:
            self.quick_recycle = response['quick_recycle']
