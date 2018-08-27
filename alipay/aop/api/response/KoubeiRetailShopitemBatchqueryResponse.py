#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ExtShopItem import ExtShopItem


class KoubeiRetailShopitemBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiRetailShopitemBatchqueryResponse, self).__init__()
        self._shopitemlist = None

    @property
    def shopitemlist(self):
        return self._shopitemlist

    @shopitemlist.setter
    def shopitemlist(self, value):
        if isinstance(value, list):
            self._shopitemlist = list()
            for i in value:
                if isinstance(i, ExtShopItem):
                    self._shopitemlist.append(i)
                else:
                    self._shopitemlist.append(ExtShopItem.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiRetailShopitemBatchqueryResponse, self).parse_response_content(response_content)
        if 'shopitemlist' in response:
            self.shopitemlist = response['shopitemlist']
