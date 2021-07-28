#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeMobileappBindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeMobileappBindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeMobileappBindResponse, self).parse_response_content(response_content)
