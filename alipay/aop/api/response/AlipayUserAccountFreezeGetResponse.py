#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccountFreeze import AccountFreeze


class AlipayUserAccountFreezeGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAccountFreezeGetResponse, self).__init__()
        self._freeze_items = None
        self._total_results = None

    @property
    def freeze_items(self):
        return self._freeze_items

    @freeze_items.setter
    def freeze_items(self, value):
        if isinstance(value, list):
            self._freeze_items = list()
            for i in value:
                if isinstance(i, AccountFreeze):
                    self._freeze_items.append(i)
                else:
                    self._freeze_items.append(AccountFreeze.from_alipay_dict(i))
    @property
    def total_results(self):
        return self._total_results

    @total_results.setter
    def total_results(self, value):
        self._total_results = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAccountFreezeGetResponse, self).parse_response_content(response_content)
        if 'freeze_items' in response:
            self.freeze_items = response['freeze_items']
        if 'total_results' in response:
            self.total_results = response['total_results']
