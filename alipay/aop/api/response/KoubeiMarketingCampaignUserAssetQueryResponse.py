#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherDetailInfo import VoucherDetailInfo


class KoubeiMarketingCampaignUserAssetQueryResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignUserAssetQueryResponse, self).__init__()
        self._voucher_asset_list = None
        self._voucher_asset_num = None

    @property
    def voucher_asset_list(self):
        return self._voucher_asset_list

    @voucher_asset_list.setter
    def voucher_asset_list(self, value):
        if isinstance(value, list):
            self._voucher_asset_list = list()
            for i in value:
                if isinstance(i, VoucherDetailInfo):
                    self._voucher_asset_list.append(i)
                else:
                    self._voucher_asset_list.append(VoucherDetailInfo.from_alipay_dict(i))
    @property
    def voucher_asset_num(self):
        return self._voucher_asset_num

    @voucher_asset_num.setter
    def voucher_asset_num(self, value):
        self._voucher_asset_num = value

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignUserAssetQueryResponse, self).parse_response_content(response_content)
        if 'voucher_asset_list' in response:
            self.voucher_asset_list = response['voucher_asset_list']
        if 'voucher_asset_num' in response:
            self.voucher_asset_num = response['voucher_asset_num']
