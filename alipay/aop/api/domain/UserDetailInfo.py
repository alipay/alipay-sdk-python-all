#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserProfileDetail import UserProfileDetail


class UserDetailInfo(object):

    def __init__(self):
        self._alipay_user_id = None
        self._ext_profile_list = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def ext_profile_list(self):
        return self._ext_profile_list

    @ext_profile_list.setter
    def ext_profile_list(self, value):
        if isinstance(value, list):
            self._ext_profile_list = list()
            for i in value:
                if isinstance(i, UserProfileDetail):
                    self._ext_profile_list.append(i)
                else:
                    self._ext_profile_list.append(UserProfileDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.ext_profile_list:
            if isinstance(self.ext_profile_list, list):
                for i in range(0, len(self.ext_profile_list)):
                    element = self.ext_profile_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_profile_list[i] = element.to_alipay_dict()
            if hasattr(self.ext_profile_list, 'to_alipay_dict'):
                params['ext_profile_list'] = self.ext_profile_list.to_alipay_dict()
            else:
                params['ext_profile_list'] = self.ext_profile_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserDetailInfo()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'ext_profile_list' in d:
            o.ext_profile_list = d['ext_profile_list']
        return o


