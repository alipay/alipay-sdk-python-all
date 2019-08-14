#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.CreditPayBillAssetVO import CreditPayBillAssetVO
from alipay.aop.api.domain.CreditPayInstallmentAssetVO import CreditPayInstallmentAssetVO
from alipay.aop.api.domain.CreditPayRefuseVO import CreditPayRefuseVO


class MybankCreditLoantradePayAssetConsultResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradePayAssetConsultResponse, self).__init__()
        self._bill_assets = None
        self._installment_assets = None
        self._refuse_info = None
        self._success = None

    @property
    def bill_assets(self):
        return self._bill_assets

    @bill_assets.setter
    def bill_assets(self, value):
        if isinstance(value, list):
            self._bill_assets = list()
            for i in value:
                if isinstance(i, CreditPayBillAssetVO):
                    self._bill_assets.append(i)
                else:
                    self._bill_assets.append(CreditPayBillAssetVO.from_alipay_dict(i))
    @property
    def installment_assets(self):
        return self._installment_assets

    @installment_assets.setter
    def installment_assets(self, value):
        if isinstance(value, list):
            self._installment_assets = list()
            for i in value:
                if isinstance(i, CreditPayInstallmentAssetVO):
                    self._installment_assets.append(i)
                else:
                    self._installment_assets.append(CreditPayInstallmentAssetVO.from_alipay_dict(i))
    @property
    def refuse_info(self):
        return self._refuse_info

    @refuse_info.setter
    def refuse_info(self, value):
        if isinstance(value, CreditPayRefuseVO):
            self._refuse_info = value
        else:
            self._refuse_info = CreditPayRefuseVO.from_alipay_dict(value)
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradePayAssetConsultResponse, self).parse_response_content(response_content)
        if 'bill_assets' in response:
            self.bill_assets = response['bill_assets']
        if 'installment_assets' in response:
            self.installment_assets = response['installment_assets']
        if 'refuse_info' in response:
            self.refuse_info = response['refuse_info']
        if 'success' in response:
            self.success = response['success']
