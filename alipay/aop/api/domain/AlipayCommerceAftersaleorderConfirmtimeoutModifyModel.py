#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAftersaleorderConfirmtimeoutModifyModel(object):

    def __init__(self):
        self._aftersales_id = None
        self._wait_user_confirm_timeout_expand_hour = None

    @property
    def aftersales_id(self):
        return self._aftersales_id

    @aftersales_id.setter
    def aftersales_id(self, value):
        self._aftersales_id = value
    @property
    def wait_user_confirm_timeout_expand_hour(self):
        return self._wait_user_confirm_timeout_expand_hour

    @wait_user_confirm_timeout_expand_hour.setter
    def wait_user_confirm_timeout_expand_hour(self, value):
        self._wait_user_confirm_timeout_expand_hour = value


    def to_alipay_dict(self):
        params = dict()
        if self.aftersales_id:
            if hasattr(self.aftersales_id, 'to_alipay_dict'):
                params['aftersales_id'] = self.aftersales_id.to_alipay_dict()
            else:
                params['aftersales_id'] = self.aftersales_id
        if self.wait_user_confirm_timeout_expand_hour:
            if hasattr(self.wait_user_confirm_timeout_expand_hour, 'to_alipay_dict'):
                params['wait_user_confirm_timeout_expand_hour'] = self.wait_user_confirm_timeout_expand_hour.to_alipay_dict()
            else:
                params['wait_user_confirm_timeout_expand_hour'] = self.wait_user_confirm_timeout_expand_hour
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAftersaleorderConfirmtimeoutModifyModel()
        if 'aftersales_id' in d:
            o.aftersales_id = d['aftersales_id']
        if 'wait_user_confirm_timeout_expand_hour' in d:
            o.wait_user_confirm_timeout_expand_hour = d['wait_user_confirm_timeout_expand_hour']
        return o


