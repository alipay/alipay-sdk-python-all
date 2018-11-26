#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoanPayAssetResult import LoanPayAssetResult
from alipay.aop.api.domain.Refuse import Refuse


class MybankCreditLoantradeLoanpayAssetConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanpayAssetConsultResponse, self).__init__()
        self._asset_result = None
        self._refuse_msg = None
        self._success = None

    @property
    def asset_result(self):
        return self._asset_result

    @asset_result.setter
    def asset_result(self, value):
        if isinstance(value, LoanPayAssetResult):
            self._asset_result = value
        else:
            self._asset_result = LoanPayAssetResult.from_alipay_dict(value)
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        if isinstance(value, Refuse):
            self._refuse_msg = value
        else:
            self._refuse_msg = Refuse.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanpayAssetConsultResponse, self).parse_response_content(response_content)
        if 'asset_result' in response:
            self.asset_result = response['asset_result']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'success' in response:
            self.success = response['success']
