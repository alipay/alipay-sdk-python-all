#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentRiskProVO import RentRiskProVO
from alipay.aop.api.domain.RentRiskProVO import RentRiskProVO
from alipay.aop.api.domain.RentRiskInfoVO import RentRiskInfoVO


class AlipayCommerceRentRiskConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentRiskConsultResponse, self).__init__()
        self._extremely_low_risk_models = None
        self._high_risk_models = None
        self._product_edition = None
        self._risk_infos = None

    @property
    def extremely_low_risk_models(self):
        return self._extremely_low_risk_models

    @extremely_low_risk_models.setter
    def extremely_low_risk_models(self, value):
        if isinstance(value, RentRiskProVO):
            self._extremely_low_risk_models = value
        else:
            self._extremely_low_risk_models = RentRiskProVO.from_alipay_dict(value)
    @property
    def high_risk_models(self):
        return self._high_risk_models

    @high_risk_models.setter
    def high_risk_models(self, value):
        if isinstance(value, RentRiskProVO):
            self._high_risk_models = value
        else:
            self._high_risk_models = RentRiskProVO.from_alipay_dict(value)
    @property
    def product_edition(self):
        return self._product_edition

    @product_edition.setter
    def product_edition(self, value):
        self._product_edition = value
    @property
    def risk_infos(self):
        return self._risk_infos

    @risk_infos.setter
    def risk_infos(self, value):
        if isinstance(value, list):
            self._risk_infos = list()
            for i in value:
                if isinstance(i, RentRiskInfoVO):
                    self._risk_infos.append(i)
                else:
                    self._risk_infos.append(RentRiskInfoVO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentRiskConsultResponse, self).parse_response_content(response_content)
        if 'extremely_low_risk_models' in response:
            self.extremely_low_risk_models = response['extremely_low_risk_models']
        if 'high_risk_models' in response:
            self.high_risk_models = response['high_risk_models']
        if 'product_edition' in response:
            self.product_edition = response['product_edition']
        if 'risk_infos' in response:
            self.risk_infos = response['risk_infos']
