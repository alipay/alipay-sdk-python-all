#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Advert import Advert


class AlipayOpenPublicAdvertBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenPublicAdvertBatchqueryResponse, self).__init__()
        self._advert_list = None

    @property
    def advert_list(self):
        return self._advert_list

    @advert_list.setter
    def advert_list(self, value):
        if isinstance(value, list):
            self._advert_list = list()
            for i in value:
                if isinstance(i, Advert):
                    self._advert_list.append(i)
                else:
                    self._advert_list.append(Advert.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayOpenPublicAdvertBatchqueryResponse, self).parse_response_content(response_content)
        if 'advert_list' in response:
            self.advert_list = response['advert_list']
