#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ResultInfoDTO import ResultInfoDTO
from alipay.aop.api.domain.VoyagerVoucherVO import VoyagerVoucherVO


class AlipayVoyagerMarketingCampaignapplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayVoyagerMarketingCampaignapplyResponse, self).__init__()
        self._apply_order_id = None
        self._result = None
        self._voucher_vos = None

    @property
    def apply_order_id(self):
        return self._apply_order_id

    @apply_order_id.setter
    def apply_order_id(self, value):
        self._apply_order_id = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        if isinstance(value, ResultInfoDTO):
            self._result = value
        else:
            self._result = ResultInfoDTO.from_alipay_dict(value)
    @property
    def voucher_vos(self):
        return self._voucher_vos

    @voucher_vos.setter
    def voucher_vos(self, value):
        if isinstance(value, list):
            self._voucher_vos = list()
            for i in value:
                if isinstance(i, VoyagerVoucherVO):
                    self._voucher_vos.append(i)
                else:
                    self._voucher_vos.append(VoyagerVoucherVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayVoyagerMarketingCampaignapplyResponse, self).parse_response_content(response_content)
        if 'apply_order_id' in response:
            self.apply_order_id = response['apply_order_id']
        if 'result' in response:
            self.result = response['result']
        if 'voucher_vos' in response:
            self.voucher_vos = response['voucher_vos']
