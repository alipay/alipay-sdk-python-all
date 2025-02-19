#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemCreateFailInfoDTO import ItemCreateFailInfoDTO
from alipay.aop.api.domain.ItemCreateSuccessInfoDTO import ItemCreateSuccessInfoDTO


class AlipayCommerceMedicalItemCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalItemCreateResponse, self).__init__()
        self._fail_list = None
        self._succ_list = None

    @property
    def fail_list(self):
        return self._fail_list

    @fail_list.setter
    def fail_list(self, value):
        if isinstance(value, list):
            self._fail_list = list()
            for i in value:
                if isinstance(i, ItemCreateFailInfoDTO):
                    self._fail_list.append(i)
                else:
                    self._fail_list.append(ItemCreateFailInfoDTO.from_alipay_dict(i))
    @property
    def succ_list(self):
        return self._succ_list

    @succ_list.setter
    def succ_list(self, value):
        if isinstance(value, list):
            self._succ_list = list()
            for i in value:
                if isinstance(i, ItemCreateSuccessInfoDTO):
                    self._succ_list.append(i)
                else:
                    self._succ_list.append(ItemCreateSuccessInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalItemCreateResponse, self).parse_response_content(response_content)
        if 'fail_list' in response:
            self.fail_list = response['fail_list']
        if 'succ_list' in response:
            self.succ_list = response['succ_list']
