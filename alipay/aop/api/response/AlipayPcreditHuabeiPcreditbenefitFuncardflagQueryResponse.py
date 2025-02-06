#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiPcreditbenefitFuncardflagQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditbenefitFuncardflagQueryResponse, self).__init__()
        self._edu_quan_flag = None
        self._hb_sign = None
        self._hua_plus = None
        self._mobile_info = None
        self._youth_flag = None

    @property
    def edu_quan_flag(self):
        return self._edu_quan_flag

    @edu_quan_flag.setter
    def edu_quan_flag(self, value):
        self._edu_quan_flag = value
    @property
    def hb_sign(self):
        return self._hb_sign

    @hb_sign.setter
    def hb_sign(self, value):
        self._hb_sign = value
    @property
    def hua_plus(self):
        return self._hua_plus

    @hua_plus.setter
    def hua_plus(self, value):
        self._hua_plus = value
    @property
    def mobile_info(self):
        return self._mobile_info

    @mobile_info.setter
    def mobile_info(self, value):
        self._mobile_info = value
    @property
    def youth_flag(self):
        return self._youth_flag

    @youth_flag.setter
    def youth_flag(self, value):
        self._youth_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditbenefitFuncardflagQueryResponse, self).parse_response_content(response_content)
        if 'edu_quan_flag' in response:
            self.edu_quan_flag = response['edu_quan_flag']
        if 'hb_sign' in response:
            self.hb_sign = response['hb_sign']
        if 'hua_plus' in response:
            self.hua_plus = response['hua_plus']
        if 'mobile_info' in response:
            self.mobile_info = response['mobile_info']
        if 'youth_flag' in response:
            self.youth_flag = response['youth_flag']
