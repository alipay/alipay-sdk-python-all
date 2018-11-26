#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AdUserQualification import AdUserQualification


class AlipayCommerceTransportAdAduserqualificationBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportAdAduserqualificationBatchqueryResponse, self).__init__()
        self._ad_user_qualification = None

    @property
    def ad_user_qualification(self):
        return self._ad_user_qualification

    @ad_user_qualification.setter
    def ad_user_qualification(self, value):
        if isinstance(value, list):
            self._ad_user_qualification = list()
            for i in value:
                if isinstance(i, AdUserQualification):
                    self._ad_user_qualification.append(i)
                else:
                    self._ad_user_qualification.append(AdUserQualification.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportAdAduserqualificationBatchqueryResponse, self).parse_response_content(response_content)
        if 'ad_user_qualification' in response:
            self.ad_user_qualification = response['ad_user_qualification']
