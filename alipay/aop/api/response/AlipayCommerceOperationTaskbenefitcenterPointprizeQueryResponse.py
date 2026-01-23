#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IsvVehownerBenefitVO import IsvVehownerBenefitVO
from alipay.aop.api.domain.IsvVoucherVO import IsvVoucherVO


class AlipayCommerceOperationTaskbenefitcenterPointprizeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationTaskbenefitcenterPointprizeQueryResponse, self).__init__()
        self._has_more = None
        self._vehowner_benefit_list = None
        self._voucher_list = None

    @property
    def has_more(self):
        return self._has_more

    @has_more.setter
    def has_more(self, value):
        self._has_more = value
    @property
    def vehowner_benefit_list(self):
        return self._vehowner_benefit_list

    @vehowner_benefit_list.setter
    def vehowner_benefit_list(self, value):
        if isinstance(value, IsvVehownerBenefitVO):
            self._vehowner_benefit_list = value
        else:
            self._vehowner_benefit_list = IsvVehownerBenefitVO.from_alipay_dict(value)
    @property
    def voucher_list(self):
        return self._voucher_list

    @voucher_list.setter
    def voucher_list(self, value):
        if isinstance(value, IsvVoucherVO):
            self._voucher_list = value
        else:
            self._voucher_list = IsvVoucherVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationTaskbenefitcenterPointprizeQueryResponse, self).parse_response_content(response_content)
        if 'has_more' in response:
            self.has_more = response['has_more']
        if 'vehowner_benefit_list' in response:
            self.vehowner_benefit_list = response['vehowner_benefit_list']
        if 'voucher_list' in response:
            self.voucher_list = response['voucher_list']
