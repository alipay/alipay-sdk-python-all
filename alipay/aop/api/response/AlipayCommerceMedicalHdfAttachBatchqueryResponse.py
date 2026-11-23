#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UrlItem import UrlItem


class AlipayCommerceMedicalHdfAttachBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalHdfAttachBatchqueryResponse, self).__init__()
        self._items = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, UrlItem):
                    self._items.append(i)
                else:
                    self._items.append(UrlItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalHdfAttachBatchqueryResponse, self).parse_response_content(response_content)
        if 'items' in response:
            self.items = response['items']
