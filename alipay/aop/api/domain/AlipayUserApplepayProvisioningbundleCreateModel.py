#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserApplepayProvisioningbundleCreateModel(object):

    def __init__(self):
        self._alipay_user_identifier = None

    @property
    def alipay_user_identifier(self):
        return self._alipay_user_identifier

    @alipay_user_identifier.setter
    def alipay_user_identifier(self, value):
        self._alipay_user_identifier = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_identifier:
            if hasattr(self.alipay_user_identifier, 'to_alipay_dict'):
                params['alipay_user_identifier'] = self.alipay_user_identifier.to_alipay_dict()
            else:
                params['alipay_user_identifier'] = self.alipay_user_identifier
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserApplepayProvisioningbundleCreateModel()
        if 'alipay_user_identifier' in d:
            o.alipay_user_identifier = d['alipay_user_identifier']
        return o


