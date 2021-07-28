#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossFncGfsettlePaycontractConfirmResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossFncGfsettlePaycontractConfirmResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayBossFncGfsettlePaycontractConfirmResponse, self).parse_response_content(response_content)
