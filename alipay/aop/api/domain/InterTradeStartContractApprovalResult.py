#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InterTradeStartContractApprovalResult(object):

    def __init__(self):
        self._need_approval_flag = None

    @property
    def need_approval_flag(self):
        return self._need_approval_flag

    @need_approval_flag.setter
    def need_approval_flag(self, value):
        self._need_approval_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.need_approval_flag:
            if hasattr(self.need_approval_flag, 'to_alipay_dict'):
                params['need_approval_flag'] = self.need_approval_flag.to_alipay_dict()
            else:
                params['need_approval_flag'] = self.need_approval_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterTradeStartContractApprovalResult()
        if 'need_approval_flag' in d:
            o.need_approval_flag = d['need_approval_flag']
        return o


