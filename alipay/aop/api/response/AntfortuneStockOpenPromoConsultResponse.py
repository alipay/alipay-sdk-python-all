#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AwardedEquityVO import AwardedEquityVO
from alipay.aop.api.domain.PendingEquityVO import PendingEquityVO


class AntfortuneStockOpenPromoConsultResponse(AlipayResponse):

    def __init__(self):
        super(AntfortuneStockOpenPromoConsultResponse, self).__init__()
        self._awarded_equity_list = None
        self._pending_equity_list = None

    @property
    def awarded_equity_list(self):
        return self._awarded_equity_list

    @awarded_equity_list.setter
    def awarded_equity_list(self, value):
        if isinstance(value, list):
            self._awarded_equity_list = list()
            for i in value:
                if isinstance(i, AwardedEquityVO):
                    self._awarded_equity_list.append(i)
                else:
                    self._awarded_equity_list.append(AwardedEquityVO.from_alipay_dict(i))
    @property
    def pending_equity_list(self):
        return self._pending_equity_list

    @pending_equity_list.setter
    def pending_equity_list(self, value):
        if isinstance(value, list):
            self._pending_equity_list = list()
            for i in value:
                if isinstance(i, PendingEquityVO):
                    self._pending_equity_list.append(i)
                else:
                    self._pending_equity_list.append(PendingEquityVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AntfortuneStockOpenPromoConsultResponse, self).parse_response_content(response_content)
        if 'awarded_equity_list' in response:
            self.awarded_equity_list = response['awarded_equity_list']
        if 'pending_equity_list' in response:
            self.pending_equity_list = response['pending_equity_list']
