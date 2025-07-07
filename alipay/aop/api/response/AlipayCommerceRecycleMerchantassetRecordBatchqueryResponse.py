#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleMerchantAssetRecordDTO import RecycleMerchantAssetRecordDTO


class AlipayCommerceRecycleMerchantassetRecordBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleMerchantassetRecordBatchqueryResponse, self).__init__()
        self._fund_account = None
        self._merchant_asset_amount = None
        self._merchant_asset_record_list = None
        self._page_no = None
        self._page_size = None
        self._seller_id_list = None
        self._subsidy_ratio = None
        self._total_count = None

    @property
    def fund_account(self):
        return self._fund_account

    @fund_account.setter
    def fund_account(self, value):
        self._fund_account = value
    @property
    def merchant_asset_amount(self):
        return self._merchant_asset_amount

    @merchant_asset_amount.setter
    def merchant_asset_amount(self, value):
        self._merchant_asset_amount = value
    @property
    def merchant_asset_record_list(self):
        return self._merchant_asset_record_list

    @merchant_asset_record_list.setter
    def merchant_asset_record_list(self, value):
        if isinstance(value, list):
            self._merchant_asset_record_list = list()
            for i in value:
                if isinstance(i, RecycleMerchantAssetRecordDTO):
                    self._merchant_asset_record_list.append(i)
                else:
                    self._merchant_asset_record_list.append(RecycleMerchantAssetRecordDTO.from_alipay_dict(i))
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
    def seller_id_list(self):
        return self._seller_id_list

    @seller_id_list.setter
    def seller_id_list(self, value):
        if isinstance(value, list):
            self._seller_id_list = list()
            for i in value:
                self._seller_id_list.append(i)
    @property
    def subsidy_ratio(self):
        return self._subsidy_ratio

    @subsidy_ratio.setter
    def subsidy_ratio(self, value):
        self._subsidy_ratio = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleMerchantassetRecordBatchqueryResponse, self).parse_response_content(response_content)
        if 'fund_account' in response:
            self.fund_account = response['fund_account']
        if 'merchant_asset_amount' in response:
            self.merchant_asset_amount = response['merchant_asset_amount']
        if 'merchant_asset_record_list' in response:
            self.merchant_asset_record_list = response['merchant_asset_record_list']
        if 'page_no' in response:
            self.page_no = response['page_no']
        if 'page_size' in response:
            self.page_size = response['page_size']
        if 'seller_id_list' in response:
            self.seller_id_list = response['seller_id_list']
        if 'subsidy_ratio' in response:
            self.subsidy_ratio = response['subsidy_ratio']
        if 'total_count' in response:
            self.total_count = response['total_count']
