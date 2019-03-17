#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.UserDetailInfo import UserDetailInfo
from alipay.aop.api.domain.VoucherInfoDetail import VoucherInfoDetail


class AlipayBusinessOrderConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessOrderConsultResponse, self).__init__()
        self._buyer_info = None
        self._voucher_list = None

    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, UserDetailInfo):
            self._buyer_info = value
        else:
            self._buyer_info = UserDetailInfo.from_alipay_dict(value)
    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, list):
            self._voucher_list = list()
            for i in value:
                if isinstance(i, VoucherInfoDetail):
                    self._voucher_list.append(i)
                else:
                    self._voucher_list.append(VoucherInfoDetail.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessOrderConsultResponse, self).parse_response_content(response_content)
        if 'buyer_info' in response:
            self.buyer_info = response['buyer_info']
        if 'voucher_list' in response:
            self.voucher_list = response['voucher_list']
