#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCateringQueueShopinfoSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringQueueShopinfoSyncResponse, self).__init__()


    def parse_response_content(self, response_content):
        response = super(KoubeiCateringQueueShopinfoSyncResponse, self).parse_response_content(response_content)
