#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniInnerversionGrayPublishResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniInnerversionGrayPublishResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniInnerversionGrayPublishResponse, self).parse_response_content(response_content)
