#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ItemBatchDeleteByIdFailInfoDTO import ItemBatchDeleteByIdFailInfoDTO
from alipay.aop.api.domain.ItemBatchDeleteByIdSuccessInfoDTO import ItemBatchDeleteByIdSuccessInfoDTO


class AlipayCommerceMedicalItemByidDeleteResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalItemByidDeleteResponse, self).__init__()
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
                if isinstance(i, ItemBatchDeleteByIdFailInfoDTO):
                    self._fail_list.append(i)
                else:
                    self._fail_list.append(ItemBatchDeleteByIdFailInfoDTO.from_alipay_dict(i))
    @property
    def succ_list(self):
        return self._succ_list

    @succ_list.setter
    def succ_list(self, value):
        if isinstance(value, list):
            self._succ_list = list()
            for i in value:
                if isinstance(i, ItemBatchDeleteByIdSuccessInfoDTO):
                    self._succ_list.append(i)
                else:
                    self._succ_list.append(ItemBatchDeleteByIdSuccessInfoDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalItemByidDeleteResponse, self).parse_response_content(response_content)
        if 'fail_list' in response:
            self.fail_list = response['fail_list']
        if 'succ_list' in response:
            self.succ_list = response['succ_list']
