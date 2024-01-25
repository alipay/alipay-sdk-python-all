#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubAccountApplyRequest import SubAccountApplyRequest


class AnttechOceanbaseSubaccountApplyModel(object):

    def __init__(self):
        self._sub_account_apply_request = None

    @property
    def sub_account_apply_request(self):
        return self._sub_account_apply_request

    @sub_account_apply_request.setter
    def sub_account_apply_request(self, value):
        if isinstance(value, SubAccountApplyRequest):
            self._sub_account_apply_request = value
        else:
            self._sub_account_apply_request = SubAccountApplyRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.sub_account_apply_request:
            if hasattr(self.sub_account_apply_request, 'to_alipay_dict'):
                params['sub_account_apply_request'] = self.sub_account_apply_request.to_alipay_dict()
            else:
                params['sub_account_apply_request'] = self.sub_account_apply_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseSubaccountApplyModel()
        if 'sub_account_apply_request' in d:
            o.sub_account_apply_request = d['sub_account_apply_request']
        return o


