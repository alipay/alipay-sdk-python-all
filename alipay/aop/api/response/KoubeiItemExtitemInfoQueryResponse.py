#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbExtItemInfo import KbExtItemInfo


class KoubeiItemExtitemInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemExtitemInfoQueryResponse, self).__init__()
        self._kb_ext_item_info = None

    @property
    def kb_ext_item_info(self):
        return self._kb_ext_item_info

    @kb_ext_item_info.setter
    def kb_ext_item_info(self, value):
        if isinstance(value, KbExtItemInfo):
            self._kb_ext_item_info = value
        else:
            self._kb_ext_item_info = KbExtItemInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiItemExtitemInfoQueryResponse, self).parse_response_content(response_content)
        if 'kb_ext_item_info' in response:
            self.kb_ext_item_info = response['kb_ext_item_info']
