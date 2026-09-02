#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayInsSceneInshealthserviceprodMallitemstatusModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInshealthserviceprodMallitemstatusModifyResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInshealthserviceprodMallitemstatusModifyResponse, self).parse_response_content(response_content)
