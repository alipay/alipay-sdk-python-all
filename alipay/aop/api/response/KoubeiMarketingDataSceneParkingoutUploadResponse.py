#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiMarketingDataSceneParkingoutUploadResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingDataSceneParkingoutUploadResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingDataSceneParkingoutUploadResponse, self).parse_response_content(response_content)
