#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class KoubeiCraftsmanDataProviderCreateResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCraftsmanDataProviderCreateResponse, self).__init__()
        self._craftsman_id = None

    @property
    def craftsman_id(self):
        return self._craftsman_id

    @craftsman_id.setter
    def craftsman_id(self, value):
        self._craftsman_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiCraftsmanDataProviderCreateResponse, self).parse_response_content(response_content)
        if 'craftsman_id' in response:
            self.craftsman_id = response['craftsman_id']
