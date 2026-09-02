#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LifeServiceAccountInfo import LifeServiceAccountInfo


class AlipayCommerceLifeserviceAccountstatusBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLifeserviceAccountstatusBatchqueryResponse, self).__init__()
        self._life_service_account_list = None

    @property
    def life_service_account_list(self):
        return self._life_service_account_list

    @life_service_account_list.setter
    def life_service_account_list(self, value):
        if isinstance(value, list):
            self._life_service_account_list = list()
            for i in value:
                if isinstance(i, LifeServiceAccountInfo):
                    self._life_service_account_list.append(i)
                else:
                    self._life_service_account_list.append(LifeServiceAccountInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLifeserviceAccountstatusBatchqueryResponse, self).parse_response_content(response_content)
        if 'life_service_account_list' in response:
            self.life_service_account_list = response['life_service_account_list']
