#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DiscountInfo import DiscountInfo
from alipay.aop.api.domain.KbAdvertIdentifyResponse import KbAdvertIdentifyResponse


class KoubeiAdvertDeliveryDiscountBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiAdvertDeliveryDiscountBatchqueryResponse, self).__init__()
        self._discounts = None
        self._purchase_datas = None
        self._recommend_id = None

    @property
    def discounts(self):
        return self._discounts

    @discounts.setter
    def discounts(self, value):
        if isinstance(value, list):
            self._discounts = list()
            for i in value:
                if isinstance(i, DiscountInfo):
                    self._discounts.append(i)
                else:
                    self._discounts.append(DiscountInfo.from_alipay_dict(i))
    @property
    def purchase_datas(self):
        return self._purchase_datas

    @purchase_datas.setter
    def purchase_datas(self, value):
        if isinstance(value, KbAdvertIdentifyResponse):
            self._purchase_datas = value
        else:
            self._purchase_datas = KbAdvertIdentifyResponse.from_alipay_dict(value)
    @property
    def recommend_id(self):
        return self._recommend_id

    @recommend_id.setter
    def recommend_id(self, value):
        self._recommend_id = value

    def parse_response_content(self, response_content):
        response = super(KoubeiAdvertDeliveryDiscountBatchqueryResponse, self).parse_response_content(response_content)
        if 'discounts' in response:
            self.discounts = response['discounts']
        if 'purchase_datas' in response:
            self.purchase_datas = response['purchase_datas']
        if 'recommend_id' in response:
            self.recommend_id = response['recommend_id']
