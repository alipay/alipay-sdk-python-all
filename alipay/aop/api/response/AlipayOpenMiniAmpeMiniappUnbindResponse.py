#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniAmpeMiniappUnbindResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniAmpeMiniappUnbindResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniAmpeMiniappUnbindResponse, self).parse_response_content(response_content)
