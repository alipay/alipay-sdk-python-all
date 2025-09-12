#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubscriptionPackageDetailDTO import SubscriptionPackageDetailDTO


class SubscribeInitiateApiResponse(object):

    def __init__(self):
        self._subscribe_token = None
        self._subscribe_url = None
        self._subscription_packages = None

    @property
    def subscribe_token(self):
        return self._subscribe_token

    @subscribe_token.setter
    def subscribe_token(self, value):
        self._subscribe_token = value
    @property
    def subscribe_url(self):
        return self._subscribe_url

    @subscribe_url.setter
    def subscribe_url(self, value):
        self._subscribe_url = value
    @property
    def subscription_packages(self):
        return self._subscription_packages

    @subscription_packages.setter
    def subscription_packages(self, value):
        if isinstance(value, SubscriptionPackageDetailDTO):
            self._subscription_packages = value
        else:
            self._subscription_packages = SubscriptionPackageDetailDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.subscribe_token:
            if hasattr(self.subscribe_token, 'to_alipay_dict'):
                params['subscribe_token'] = self.subscribe_token.to_alipay_dict()
            else:
                params['subscribe_token'] = self.subscribe_token
        if self.subscribe_url:
            if hasattr(self.subscribe_url, 'to_alipay_dict'):
                params['subscribe_url'] = self.subscribe_url.to_alipay_dict()
            else:
                params['subscribe_url'] = self.subscribe_url
        if self.subscription_packages:
            if hasattr(self.subscription_packages, 'to_alipay_dict'):
                params['subscription_packages'] = self.subscription_packages.to_alipay_dict()
            else:
                params['subscription_packages'] = self.subscription_packages
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubscribeInitiateApiResponse()
        if 'subscribe_token' in d:
            o.subscribe_token = d['subscribe_token']
        if 'subscribe_url' in d:
            o.subscribe_url = d['subscribe_url']
        if 'subscription_packages' in d:
            o.subscription_packages = d['subscription_packages']
        return o


