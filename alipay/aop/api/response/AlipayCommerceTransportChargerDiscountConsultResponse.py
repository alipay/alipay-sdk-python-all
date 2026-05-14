#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.ChargerDiscountActivityInfo import ChargerDiscountActivityInfo
from alipay.aop.api.domain.ChargerDiscountActivityQuota import ChargerDiscountActivityQuota


class AlipayCommerceTransportChargerDiscountConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportChargerDiscountConsultResponse, self).__init__()
        self._activity_info = None
        self._activity_quota = None
        self._biz_date = None

    @property
    def activity_info(self):
        return self._activity_info

    @activity_info.setter
    def activity_info(self, value):
        if isinstance(value, ChargerDiscountActivityInfo):
            self._activity_info = value
        else:
            self._activity_info = ChargerDiscountActivityInfo.from_alipay_dict(value)
    @property
    def activity_quota(self):
        return self._activity_quota

    @activity_quota.setter
    def activity_quota(self, value):
        if isinstance(value, list):
            self._activity_quota = list()
            for i in value:
                if isinstance(i, ChargerDiscountActivityQuota):
                    self._activity_quota.append(i)
                else:
                    self._activity_quota.append(ChargerDiscountActivityQuota.from_alipay_dict(i))
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportChargerDiscountConsultResponse, self).parse_response_content(response_content)
        if 'activity_info' in response:
            self.activity_info = response['activity_info']
        if 'activity_quota' in response:
            self.activity_quota = response['activity_quota']
        if 'biz_date' in response:
            self.biz_date = response['biz_date']
