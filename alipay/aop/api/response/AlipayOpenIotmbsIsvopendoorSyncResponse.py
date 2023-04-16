#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenIotmbsIsvopendoorSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenIotmbsIsvopendoorSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(AlipayOpenIotmbsIsvopendoorSyncResponse, self).parse_response_content(response_content)
