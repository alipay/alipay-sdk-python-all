#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ShopDataDetail import ShopDataDetail


class AnttechMorseMarketingShopDataBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingShopDataBatchqueryResponse, self).__init__()
        self._data_list = None
        self._task_status = None
        self._total = None

    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, ShopDataDetail):
                    self._data_list.append(i)
                else:
                    self._data_list.append(ShopDataDetail.from_alipay_dict(i))
    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingShopDataBatchqueryResponse, self).parse_response_content(response_content)
        if 'data_list' in response:
            self.data_list = response['data_list']
        if 'task_status' in response:
            self.task_status = response['task_status']
        if 'total' in response:
            self.total = response['total']
