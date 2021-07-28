#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAssetPointVoucherprodBenefittemplateModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetPointVoucherprodBenefittemplateModifyResponse, self).__init__()
        self._publish_end_time = None

    @property
    def publish_end_time(self):
        return self._publish_end_time

    @publish_end_time.setter
    def publish_end_time(self, value):
        self._publish_end_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayAssetPointVoucherprodBenefittemplateModifyResponse, self).parse_response_content(response_content)
        if 'publish_end_time' in response:
            self.publish_end_time = response['publish_end_time']
