#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExternalItemInfo import ExternalItemInfo


class AlipayInsSceneInshealthserviceprodMallitemModifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInshealthserviceprodMallitemModifyResponse, self).__init__()
        self._item = None

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if isinstance(value, ExternalItemInfo):
            self._item = value
        else:
            self._item = ExternalItemInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInshealthserviceprodMallitemModifyResponse, self).parse_response_content(response_content)
        if 'item' in response:
            self.item = response['item']
