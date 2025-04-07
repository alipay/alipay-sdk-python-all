#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.StoreInfoVO import StoreInfoVO


class AlipayCommerceMedicalStoreDetailGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalStoreDetailGetResponse, self).__init__()
        self._records = None

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        if isinstance(value, list):
            self._records = list()
            for i in value:
                if isinstance(i, StoreInfoVO):
                    self._records.append(i)
                else:
                    self._records.append(StoreInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalStoreDetailGetResponse, self).parse_response_content(response_content)
        if 'records' in response:
            self.records = response['records']
