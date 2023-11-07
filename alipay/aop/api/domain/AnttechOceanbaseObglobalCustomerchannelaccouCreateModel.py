#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreateCustomerChannelAccountRequest import CreateCustomerChannelAccountRequest


class AnttechOceanbaseObglobalCustomerchannelaccouCreateModel(object):

    def __init__(self):
        self._create_customer_channel_account_request = None

    @property
    def create_customer_channel_account_request(self):
        return self._create_customer_channel_account_request

    @create_customer_channel_account_request.setter
    def create_customer_channel_account_request(self, value):
        if isinstance(value, CreateCustomerChannelAccountRequest):
            self._create_customer_channel_account_request = value
        else:
            self._create_customer_channel_account_request = CreateCustomerChannelAccountRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.create_customer_channel_account_request:
            if hasattr(self.create_customer_channel_account_request, 'to_alipay_dict'):
                params['create_customer_channel_account_request'] = self.create_customer_channel_account_request.to_alipay_dict()
            else:
                params['create_customer_channel_account_request'] = self.create_customer_channel_account_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalCustomerchannelaccouCreateModel()
        if 'create_customer_channel_account_request' in d:
            o.create_customer_channel_account_request = d['create_customer_channel_account_request']
        return o


