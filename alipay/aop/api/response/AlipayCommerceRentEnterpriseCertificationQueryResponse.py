#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RentEnterpriseCertification import RentEnterpriseCertification


class AlipayCommerceRentEnterpriseCertificationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRentEnterpriseCertificationQueryResponse, self).__init__()
        self._rent_enterprise_certification = None

    @property
    def rent_enterprise_certification(self):
        return self._rent_enterprise_certification

    @rent_enterprise_certification.setter
    def rent_enterprise_certification(self, value):
        if isinstance(value, RentEnterpriseCertification):
            self._rent_enterprise_certification = value
        else:
            self._rent_enterprise_certification = RentEnterpriseCertification.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRentEnterpriseCertificationQueryResponse, self).parse_response_content(response_content)
        if 'rent_enterprise_certification' in response:
            self.rent_enterprise_certification = response['rent_enterprise_certification']
