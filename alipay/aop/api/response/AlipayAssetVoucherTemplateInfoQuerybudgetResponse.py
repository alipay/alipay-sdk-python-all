#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.VoucherTemplateBudgetDTO import VoucherTemplateBudgetDTO


class AlipayAssetVoucherTemplateInfoQuerybudgetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAssetVoucherTemplateInfoQuerybudgetResponse, self).__init__()
        self._template_list = None

    @property
    def template_list(self):
        return self._template_list

    @template_list.setter
    def template_list(self, value):
        if isinstance(value, list):
            self._template_list = list()
            for i in value:
                if isinstance(i, VoucherTemplateBudgetDTO):
                    self._template_list.append(i)
                else:
                    self._template_list.append(VoucherTemplateBudgetDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayAssetVoucherTemplateInfoQuerybudgetResponse, self).parse_response_content(response_content)
        if 'template_list' in response:
            self.template_list = response['template_list']
