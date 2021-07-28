#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HbFqPayInfo(object):

    def __init__(self):
        self._user_install_num = None

    @property
    def user_install_num(self):
        return self._user_install_num

    @user_install_num.setter
    def user_install_num(self, value):
        self._user_install_num = value


    def to_alipay_dict(self):
        params = dict()
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
        if 'user_install_num' in d:
            o.user_install_num = d['user_install_num']
        return o


