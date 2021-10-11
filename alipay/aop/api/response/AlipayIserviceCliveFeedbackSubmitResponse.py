#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceCliveFeedbackSubmitResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceCliveFeedbackSubmitResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayIserviceCliveFeedbackSubmitResponse, self).parse_response_content(response_content)
