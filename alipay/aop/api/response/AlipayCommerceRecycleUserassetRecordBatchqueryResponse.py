#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleUserAssetRecordDTO import RecycleUserAssetRecordDTO


class AlipayCommerceRecycleUserassetRecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleUserassetRecordBatchqueryResponse, self).__init__()
        self._page_no = None
        self._page_size = None
        self._total_count = None
        self._user_asset_amount = None
        self._user_asset_record_list = None
        self._user_withdraw_amount = None

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, value):
        self._page_no = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def user_asset_amount(self):
        return self._user_asset_amount

    @user_asset_amount.setter
    def user_asset_amount(self, value):
        self._user_asset_amount = value
    @property
    def user_asset_record_list(self):
        return self._user_asset_record_list

    @user_asset_record_list.setter
    def user_asset_record_list(self, value):
        if isinstance(value, list):
            self._user_asset_record_list = list()
            for i in value:
                if isinstance(i, RecycleUserAssetRecordDTO):
                    self._user_asset_record_list.append(i)
                else:
                    self._user_asset_record_list.append(RecycleUserAssetRecordDTO.from_alipay_dict(i))
    @property
    def user_withdraw_amount(self):
        return self._user_withdraw_amount

    @user_withdraw_amount.setter
    def user_withdraw_amount(self, value):
        self._user_withdraw_amount = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleUserassetRecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'total_count' in response:
            self.total_count = response['total_count']
        if 'user_asset_amount' in response:
            self.user_asset_amount = response['user_asset_amount']
        if 'user_asset_record_list' in response:
            self.user_asset_record_list = response['user_asset_record_list']
        if 'user_withdraw_amount' in response:
            self.user_withdraw_amount = response['user_withdraw_amount']
