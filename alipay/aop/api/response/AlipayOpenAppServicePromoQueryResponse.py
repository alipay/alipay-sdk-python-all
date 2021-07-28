#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ServicePromoBaseVO import ServicePromoBaseVO
from alipay.aop.api.domain.ServicePromoBaseVO import ServicePromoBaseVO


class AlipayOpenAppServicePromoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppServicePromoQueryResponse, self).__init__()
        self._editing_service_promo = None
        self._valid_service_promo = None

    @property
    def editing_service_promo(self):
        return self._editing_service_promo

    @editing_service_promo.setter
    def editing_service_promo(self, value):
        if isinstance(value, ServicePromoBaseVO):
            self._editing_service_promo = value
        else:
            self._editing_service_promo = ServicePromoBaseVO.from_alipay_dict(value)
    @property
    def valid_service_promo(self):
        return self._valid_service_promo

    @valid_service_promo.setter
    def valid_service_promo(self, value):
        if isinstance(value, ServicePromoBaseVO):
            self._valid_service_promo = value
        else:
            self._valid_service_promo = ServicePromoBaseVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppServicePromoQueryResponse, self).parse_response_content(response_content)
        if 'editing_service_promo' in response:
            self.editing_service_promo = response['editing_service_promo']
        if 'valid_service_promo' in response:
            self.valid_service_promo = response['valid_service_promo']
