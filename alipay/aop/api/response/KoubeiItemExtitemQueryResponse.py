#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtItem import ExtItem


class KoubeiItemExtitemQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiItemExtitemQueryResponse, self).__init__()
        self._extitem = None

    @property
    def extitem(self):
        return self._extitem

    @extitem.setter
    def extitem(self, value):
        if isinstance(value, ExtItem):
            self._extitem = value
        else:
            self._extitem = ExtItem.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiItemExtitemQueryResponse, self).parse_response_content(response_content)
        if 'extitem' in response:
            self.extitem = response['extitem']
