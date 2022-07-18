#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MrchCrmUser import MrchCrmUser


class AlipayMerchantUserUploadModel(object):

    def __init__(self):
        self._user_list = None

    @property
    def user_list(self):
        return self._user_list

    @user_list.setter
    def user_list(self, value):
        if isinstance(value, list):
            self._user_list = list()
            for i in value:
                if isinstance(i, MrchCrmUser):
                    self._user_list.append(i)
                else:
                    self._user_list.append(MrchCrmUser.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.user_list:
            if isinstance(self.user_list, list):
                for i in range(0, len(self.user_list)):
                    element = self.user_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_list[i] = element.to_alipay_dict()
            if hasattr(self.user_list, 'to_alipay_dict'):
                params['user_list'] = self.user_list.to_alipay_dict()
            else:
                params['user_list'] = self.user_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantUserUploadModel()
        if 'user_list' in d:
            o.user_list = d['user_list']
        return o


