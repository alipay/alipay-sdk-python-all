#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.MpcOrderVO import MpcOrderVO


class TechriskInnovateMpcpromoOrderCreateResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateMpcpromoOrderCreateResponse, self).__init__()
        self._mpc_order = None

    @property
    def mpc_order(self):
        return self._mpc_order

    @mpc_order.setter
    def mpc_order(self, value):
        if isinstance(value, MpcOrderVO):
            self._mpc_order = value
        else:
            self._mpc_order = MpcOrderVO.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateMpcpromoOrderCreateResponse, self).parse_response_content(response_content)
        if 'mpc_order' in response:
            self.mpc_order = response['mpc_order']
