#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherVO import VoucherVO
from alipay.aop.api.domain.VoucherVO import VoucherVO


class KoubeiMarketingCampaignBenefitSendResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiMarketingCampaignBenefitSendResponse, self).__init__()
        self._benefit_ids = None
        self._voucher_vo_list = None
        self._voucher_vos = None

    @property
    def benefit_ids(self):
        return self._benefit_ids

    @benefit_ids.setter
    def benefit_ids(self, value):
        if isinstance(value, list):
            self._benefit_ids = list()
            for i in value:
                self._benefit_ids.append(i)
    @property
    def voucher_vo_list(self):
        return self._voucher_vo_list

    @voucher_vo_list.setter
    def voucher_vo_list(self, value):
        if isinstance(value, list):
            self._voucher_vo_list = list()
            for i in value:
                if isinstance(i, VoucherVO):
                    self._voucher_vo_list.append(i)
                else:
                    self._voucher_vo_list.append(VoucherVO.from_alipay_dict(i))
    @property
    def voucher_vos(self):
        return self._voucher_vos

    @voucher_vos.setter
    def voucher_vos(self, value):
        if isinstance(value, VoucherVO):
            self._voucher_vos = value
        else:
            self._voucher_vos = VoucherVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(KoubeiMarketingCampaignBenefitSendResponse, self).parse_response_content(response_content)
        if 'benefit_ids' in response:
            self.benefit_ids = response['benefit_ids']
        if 'voucher_vo_list' in response:
            self.voucher_vo_list = response['voucher_vo_list']
        if 'voucher_vos' in response:
            self.voucher_vos = response['voucher_vos']
