#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AntfarmUserDonationInfo import AntfarmUserDonationInfo


class AlipaySocialAntfarmDonationinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipaySocialAntfarmDonationinfoQueryResponse, self).__init__()
        self._donation_list = None

    @property
    def donation_list(self):
        return self._donation_list

    @donation_list.setter
    def donation_list(self, value):
        if isinstance(value, list):
            self._donation_list = list()
            for i in value:
                if isinstance(i, AntfarmUserDonationInfo):
                    self._donation_list.append(i)
                else:
                    self._donation_list.append(AntfarmUserDonationInfo.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipaySocialAntfarmDonationinfoQueryResponse, self).parse_response_content(response_content)
        if 'donation_list' in response:
            self.donation_list = response['donation_list']
