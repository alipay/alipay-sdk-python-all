#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AppBaseInfo import AppBaseInfo


class AlipayOpenMiniOrderbillApplistBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderbillApplistBatchqueryResponse, self).__init__()
        self._app_list = None
        self._total = None

    @property
    def app_list(self):
        return self._app_list

    @app_list.setter
    def app_list(self, value):
        if isinstance(value, list):
            self._app_list = list()
            for i in value:
                if isinstance(i, AppBaseInfo):
                    self._app_list.append(i)
                else:
                    self._app_list.append(AppBaseInfo.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderbillApplistBatchqueryResponse, self).parse_response_content(response_content)
        if 'app_list' in response:
            self.app_list = response['app_list']
        if 'total' in response:
            self.total = response['total']
