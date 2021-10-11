#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PointReceiveInfo import PointReceiveInfo


class AlipayCommerceOperationPromoterPointReceiveResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceOperationPromoterPointReceiveResponse, self).__init__()
        self._point_receive_result = None

    @property
    def point_receive_result(self):
        return self._point_receive_result

    @point_receive_result.setter
    def point_receive_result(self, value):
        if isinstance(value, PointReceiveInfo):
            self._point_receive_result = value
        else:
            self._point_receive_result = PointReceiveInfo.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceOperationPromoterPointReceiveResponse, self).parse_response_content(response_content)
        if 'point_receive_result' in response:
            self.point_receive_result = response['point_receive_result']
