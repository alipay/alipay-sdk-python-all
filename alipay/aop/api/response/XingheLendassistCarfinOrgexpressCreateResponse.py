#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class XingheLendassistCarfinOrgexpressCreateResponse(AlipayResponse):

    def __init__(self):
        super(XingheLendassistCarfinOrgexpressCreateResponse, self).__init__()
        self._express_no = None
        self._pickup_code = None
        self._refuse_msg = None
        self._status = None
        self._tracking_no = None

    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def pickup_code(self):
        return self._pickup_code

    @pickup_code.setter
    def pickup_code(self, value):
        self._pickup_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tracking_no(self):
        return self._tracking_no

    @tracking_no.setter
    def tracking_no(self, value):
        self._tracking_no = value

    def parse_response_content(self, response_content):
        response = super(XingheLendassistCarfinOrgexpressCreateResponse, self).parse_response_content(response_content)
        if 'express_no' in response:
            self.express_no = response['express_no']
        if 'pickup_code' in response:
            self.pickup_code = response['pickup_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'status' in response:
            self.status = response['status']
        if 'tracking_no' in response:
            self.tracking_no = response['tracking_no']
