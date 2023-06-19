#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.QipanMerchantCrowd import QipanMerchantCrowd


class AlipayMerchantQipanCrowdBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantQipanCrowdBatchqueryResponse, self).__init__()
        self._crowd_list = None
        self._total_number = None

    @property
    def crowd_list(self):
        return self._crowd_list

    @crowd_list.setter
    def crowd_list(self, value):
        if isinstance(value, list):
            self._crowd_list = list()
            for i in value:
                if isinstance(i, QipanMerchantCrowd):
                    self._crowd_list.append(i)
                else:
                    self._crowd_list.append(QipanMerchantCrowd.from_alipay_dict(i))
    @property
    def total_number(self):
        return self._total_number

    @total_number.setter
    def total_number(self, value):
        self._total_number = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantQipanCrowdBatchqueryResponse, self).parse_response_content(response_content)
        if 'crowd_list' in response:
            self.crowd_list = response['crowd_list']
        if 'total_number' in response:
            self.total_number = response['total_number']
