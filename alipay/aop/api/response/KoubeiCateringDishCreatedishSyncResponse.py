#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.KbdishDetailInfo import KbdishDetailInfo


class KoubeiCateringDishCreatedishSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiCateringDishCreatedishSyncResponse, self).__init__()
        self._dish_id = None
        self._fail_group_detail_list = None
        self._retry = None
        self._sku_id_list = None

    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def fail_group_detail_list(self):
        return self._fail_group_detail_list

    @fail_group_detail_list.setter
    def fail_group_detail_list(self, value):
        if isinstance(value, list):
            self._fail_group_detail_list = list()
            for i in value:
                if isinstance(i, KbdishDetailInfo):
                    self._fail_group_detail_list.append(i)
                else:
                    self._fail_group_detail_list.append(KbdishDetailInfo.from_alipay_dict(i))
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def sku_id_list(self):
        return self._sku_id_list

    @sku_id_list.setter
    def sku_id_list(self, value):
        if isinstance(value, list):
            self._sku_id_list = list()
            for i in value:
                self._sku_id_list.append(i)

    def parse_response_content(self, response_content):
        response = super(KoubeiCateringDishCreatedishSyncResponse, self).parse_response_content(response_content)
        if 'dish_id' in response:
            self.dish_id = response['dish_id']
        if 'fail_group_detail_list' in response:
            self.fail_group_detail_list = response['fail_group_detail_list']
        if 'retry' in response:
            self.retry = response['retry']
        if 'sku_id_list' in response:
            self.sku_id_list = response['sku_id_list']
