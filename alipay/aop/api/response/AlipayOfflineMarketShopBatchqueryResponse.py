#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineMarketShopBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineMarketShopBatchqueryResponse, self).__init__()
        self._current_pageno = None
        self._shop_ids = None
        self._total_pageno = None

    @property
    def current_pageno(self):
        return self._current_pageno

    @current_pageno.setter
    def current_pageno(self, value):
        self._current_pageno = value
    @property
    def shop_ids(self):
        return self._shop_ids

    @shop_ids.setter
    def shop_ids(self, value):
        if isinstance(value, list):
            self._shop_ids = list()
            for i in value:
                self._shop_ids.append(i)
    @property
    def total_pageno(self):
        return self._total_pageno

    @total_pageno.setter
    def total_pageno(self, value):
        self._total_pageno = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineMarketShopBatchqueryResponse, self).parse_response_content(response_content)
        if 'current_pageno' in response:
            self.current_pageno = response['current_pageno']
        if 'shop_ids' in response:
            self.shop_ids = response['shop_ids']
        if 'total_pageno' in response:
            self.total_pageno = response['total_pageno']
