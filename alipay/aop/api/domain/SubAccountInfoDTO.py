#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubAccountAndBindDTO import SubAccountAndBindDTO


class SubAccountInfoDTO(object):

    def __init__(self):
        self._apply_status = None
        self._sub_account_info = None

    @property
    def apply_status(self):
        return self._apply_status

    @apply_status.setter
    def apply_status(self, value):
        self._apply_status = value
    @property
    def sub_account_info(self):
        return self._sub_account_info

    @sub_account_info.setter
    def sub_account_info(self, value):
        if isinstance(value, SubAccountAndBindDTO):
            self._sub_account_info = value
        else:
            self._sub_account_info = SubAccountAndBindDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.apply_status:
            if hasattr(self.apply_status, 'to_alipay_dict'):
                params['apply_status'] = self.apply_status.to_alipay_dict()
            else:
                params['apply_status'] = self.apply_status
        if self.sub_account_info:
            if hasattr(self.sub_account_info, 'to_alipay_dict'):
                params['sub_account_info'] = self.sub_account_info.to_alipay_dict()
            else:
                params['sub_account_info'] = self.sub_account_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubAccountInfoDTO()
        if 'apply_status' in d:
            o.apply_status = d['apply_status']
        if 'sub_account_info' in d:
            o.sub_account_info = d['sub_account_info']
        return o


