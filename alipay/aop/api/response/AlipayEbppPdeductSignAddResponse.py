#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppPdeductSignAddResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppPdeductSignAddResponse, self).__init__()
        self._agreement_id = None
        self._agreement_status = None
        self._extend_field = None
        self._notify_config = None
        self._out_agreement_id = None
        self._pay_config = None
        self._sign_date = None

    @property
    def agreement_id(self):
        return self._agreement_id

    @agreement_id.setter
    def agreement_id(self, value):
        self._agreement_id = value
    @property
    def agreement_status(self):
        return self._agreement_status

    @agreement_status.setter
    def agreement_status(self, value):
        self._agreement_status = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def notify_config(self):
        return self._notify_config

    @notify_config.setter
    def notify_config(self, value):
        self._notify_config = value
    @property
    def out_agreement_id(self):
        return self._out_agreement_id

    @out_agreement_id.setter
    def out_agreement_id(self, value):
        self._out_agreement_id = value
    @property
    def pay_config(self):
        return self._pay_config

    @pay_config.setter
    def pay_config(self, value):
        if isinstance(value, list):
            self._pay_config = list()
            for i in value:
                self._pay_config.append(i)
    @property
    def sign_date(self):
        return self._sign_date

    @sign_date.setter
    def sign_date(self, value):
        self._sign_date = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppPdeductSignAddResponse, self).parse_response_content(response_content)
        if 'agreement_id' in response:
            self.agreement_id = response['agreement_id']
        if 'agreement_status' in response:
            self.agreement_status = response['agreement_status']
        if 'extend_field' in response:
            self.extend_field = response['extend_field']
        if 'notify_config' in response:
            self.notify_config = response['notify_config']
        if 'out_agreement_id' in response:
            self.out_agreement_id = response['out_agreement_id']
        if 'pay_config' in response:
            self.pay_config = response['pay_config']
        if 'sign_date' in response:
            self.sign_date = response['sign_date']
