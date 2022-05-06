#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniPluginuseconfigUpgradeResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniPluginuseconfigUpgradeResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniPluginuseconfigUpgradeResponse, self).parse_response_content(response_content)
