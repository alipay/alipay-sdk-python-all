#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePetMerchantarchiveCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePetMerchantarchiveCreateResponse, self).__init__()
        self._archive_id = None

    @property
    def archive_id(self):
        return self._archive_id

    @archive_id.setter
    def archive_id(self, value):
        self._archive_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePetMerchantarchiveCreateResponse, self).parse_response_content(response_content)
        if 'archive_id' in response:
            self.archive_id = response['archive_id']
