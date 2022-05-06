#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserDetailDto import UserDetailDto


class AlipayCommerceEducateSceneTokenApplyModel(object):

    def __init__(self):
        self._biz_code = None
        self._user_detail_info = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def user_detail_info(self):
        return self._user_detail_info

    @user_detail_info.setter
    def user_detail_info(self, value):
        if isinstance(value, UserDetailDto):
            self._user_detail_info = value
        else:
            self._user_detail_info = UserDetailDto.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.user_detail_info:
            if hasattr(self.user_detail_info, 'to_alipay_dict'):
                params['user_detail_info'] = self.user_detail_info.to_alipay_dict()
            else:
                params['user_detail_info'] = self.user_detail_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateSceneTokenApplyModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'user_detail_info' in d:
            o.user_detail_info = d['user_detail_info']
        return o


