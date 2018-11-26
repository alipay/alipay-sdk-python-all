#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PintuanUserInfo import PintuanUserInfo


class PintuanUserInfos(object):

    def __init__(self):
        self._pintuan_user_info_list = None

    @property
    def pintuan_user_info_list(self):
        return self._pintuan_user_info_list

    @pintuan_user_info_list.setter
    def pintuan_user_info_list(self, value):
        if isinstance(value, PintuanUserInfo):
            self._pintuan_user_info_list = value
        else:
            self._pintuan_user_info_list = PintuanUserInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.pintuan_user_info_list:
            if hasattr(self.pintuan_user_info_list, 'to_alipay_dict'):
                params['pintuan_user_info_list'] = self.pintuan_user_info_list.to_alipay_dict()
            else:
                params['pintuan_user_info_list'] = self.pintuan_user_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PintuanUserInfos()
        if 'pintuan_user_info_list' in d:
            o.pintuan_user_info_list = d['pintuan_user_info_list']
        return o


