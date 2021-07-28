#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.OrderApplyStatusBriefDTO import OrderApplyStatusBriefDTO


class AlipayEbppInvoiceApplystatusQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppInvoiceApplystatusQueryResponse, self).__init__()
        self._apply_status_brief_dtos = None

    @property
    def apply_status_brief_dtos(self):
        return self._apply_status_brief_dtos

    @apply_status_brief_dtos.setter
    def apply_status_brief_dtos(self, value):
        if isinstance(value, list):
            self._apply_status_brief_dtos = list()
            for i in value:
                if isinstance(i, OrderApplyStatusBriefDTO):
                    self._apply_status_brief_dtos.append(i)
                else:
                    self._apply_status_brief_dtos.append(OrderApplyStatusBriefDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayEbppInvoiceApplystatusQueryResponse, self).parse_response_content(response_content)
        if 'apply_status_brief_dtos' in response:
            self.apply_status_brief_dtos = response['apply_status_brief_dtos']
