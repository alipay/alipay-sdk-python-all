#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HbFqPayInfo(object):

    def __init__(self):
        self._fq_amount = None
        self._user_install_num = None

    @property
    def fq_amount(self):
        return self._fq_amount

    @fq_amount.setter
    def fq_amount(self, value):
        self._fq_amount = value
    @property
    def user_install_num(self):
        return self._user_install_num

    @user_install_num.setter
    def user_install_num(self, value):
        self._user_install_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.fq_amount:
            if hasattr(self.fq_amount, 'to_alipay_dict'):
                params['fq_amount'] = self.fq_amount.to_alipay_dict()
            else:
                params['fq_amount'] = self.fq_amount
        if self.user_install_num:
            if hasattr(self.user_install_num, 'to_alipay_dict'):
                params['user_install_num'] = self.user_install_num.to_alipay_dict()
            else:
                params['user_install_num'] = self.user_install_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HbFqPayInfo()
        if 'fq_amount' in d:
            o.fq_amount = d['fq_amount']
        if 'user_install_num' in d:
            o.user_install_num = d['user_install_num']
        return o


