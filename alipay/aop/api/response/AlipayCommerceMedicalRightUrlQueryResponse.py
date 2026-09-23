#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RightDetailUrlInfo import RightDetailUrlInfo


class AlipayCommerceMedicalRightUrlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalRightUrlQueryResponse, self).__init__()
        self._right_detail_url_info = None

    @property
    def right_detail_url_info(self):
        return self._right_detail_url_info

    @right_detail_url_info.setter
    def right_detail_url_info(self, value):
        if isinstance(value, RightDetailUrlInfo):
            self._right_detail_url_info = value
        else:
            self._right_detail_url_info = RightDetailUrlInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalRightUrlQueryResponse, self).parse_response_content(response_content)
        if 'right_detail_url_info' in response:
            self.right_detail_url_info = response['right_detail_url_info']
