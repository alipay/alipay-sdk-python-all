#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentExtInfo import RentExtInfo
from alipay.aop.api.domain.RentInfo import RentInfo
from alipay.aop.api.domain.RentRiskInfo import RentRiskInfo


class AlipayCommerceRentOrderInvestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentOrderInvestQueryResponse, self).__init__()
        self._rent_ext_info = None
        self._rent_info = None
        self._rent_risk_info = None

    @property
    def rent_ext_info(self):
        return self._rent_ext_info

    @rent_ext_info.setter
    def rent_ext_info(self, value):
        if isinstance(value, RentExtInfo):
            self._rent_ext_info = value
        else:
            self._rent_ext_info = RentExtInfo.from_alipay_dict(value)
    @property
    def rent_info(self):
        return self._rent_info

    @rent_info.setter
    def rent_info(self, value):
        if isinstance(value, RentInfo):
            self._rent_info = value
        else:
            self._rent_info = RentInfo.from_alipay_dict(value)
    @property
    def rent_risk_info(self):
        return self._rent_risk_info

    @rent_risk_info.setter
    def rent_risk_info(self, value):
        if isinstance(value, list):
            self._rent_risk_info = list()
            for i in value:
                if isinstance(i, RentRiskInfo):
                    self._rent_risk_info.append(i)
                else:
                    self._rent_risk_info.append(RentRiskInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentOrderInvestQueryResponse, self).parse_response_content(response_content)
        if 'rent_ext_info' in response:
            self.rent_ext_info = response['rent_ext_info']
        if 'rent_info' in response:
            self.rent_info = response['rent_info']
        if 'rent_risk_info' in response:
            self.rent_risk_info = response['rent_risk_info']
