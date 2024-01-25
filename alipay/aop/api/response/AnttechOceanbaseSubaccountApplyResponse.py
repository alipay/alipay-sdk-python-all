#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SubAccountApplyResult import SubAccountApplyResult


class AnttechOceanbaseSubaccountApplyResponse(AlipayResponse):

    def __init__(self):
        super(AnttechOceanbaseSubaccountApplyResponse, self).__init__()
        self._sub_account_apply_result = None

    @property
    def sub_account_apply_result(self):
        return self._sub_account_apply_result

    @sub_account_apply_result.setter
    def sub_account_apply_result(self, value):
        if isinstance(value, SubAccountApplyResult):
            self._sub_account_apply_result = value
        else:
            self._sub_account_apply_result = SubAccountApplyResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AnttechOceanbaseSubaccountApplyResponse, self).parse_response_content(response_content)
        if 'sub_account_apply_result' in response:
            self.sub_account_apply_result = response['sub_account_apply_result']
