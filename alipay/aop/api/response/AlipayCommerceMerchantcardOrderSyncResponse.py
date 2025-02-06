#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DataSyncResponse import DataSyncResponse


class AlipayCommerceMerchantcardOrderSyncResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMerchantcardOrderSyncResponse, self).__init__()
        self._data_sync_rep = None

    @property
    def data_sync_rep(self):
        return self._data_sync_rep

    @data_sync_rep.setter
    def data_sync_rep(self, value):
        if isinstance(value, DataSyncResponse):
            self._data_sync_rep = value
        else:
            self._data_sync_rep = DataSyncResponse.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMerchantcardOrderSyncResponse, self).parse_response_content(response_content)
        if 'data_sync_rep' in response:
            self.data_sync_rep = response['data_sync_rep']
