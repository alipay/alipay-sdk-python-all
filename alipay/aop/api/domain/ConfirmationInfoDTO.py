#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConfirmationInfoDTO(object):

    def __init__(self):
        self._confirm_num = None
        self._confirm_result = None
        self._confirm_time = None
        self._instant_confirm = None

    @property
    def confirm_num(self):
        return self._confirm_num

    @confirm_num.setter
    def confirm_num(self, value):
        self._confirm_num = value
    @property
    def confirm_result(self):
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, value):
        self._confirm_result = value
    @property
    def confirm_time(self):
        return self._confirm_time

    @confirm_time.setter
    def confirm_time(self, value):
        self._confirm_time = value
    @property
    def instant_confirm(self):
        return self._instant_confirm

    @instant_confirm.setter
    def instant_confirm(self, value):
        self._instant_confirm = value


    def to_alipay_dict(self):
        params = dict()
        if self.confirm_num:
            if hasattr(self.confirm_num, 'to_alipay_dict'):
                params['confirm_num'] = self.confirm_num.to_alipay_dict()
            else:
                params['confirm_num'] = self.confirm_num
        if self.confirm_result:
            if hasattr(self.confirm_result, 'to_alipay_dict'):
                params['confirm_result'] = self.confirm_result.to_alipay_dict()
            else:
                params['confirm_result'] = self.confirm_result
        if self.confirm_time:
            if hasattr(self.confirm_time, 'to_alipay_dict'):
                params['confirm_time'] = self.confirm_time.to_alipay_dict()
            else:
                params['confirm_time'] = self.confirm_time
        if self.instant_confirm:
            if hasattr(self.instant_confirm, 'to_alipay_dict'):
                params['instant_confirm'] = self.instant_confirm.to_alipay_dict()
            else:
                params['instant_confirm'] = self.instant_confirm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConfirmationInfoDTO()
        if 'confirm_num' in d:
            o.confirm_num = d['confirm_num']
        if 'confirm_result' in d:
            o.confirm_result = d['confirm_result']
        if 'confirm_time' in d:
            o.confirm_time = d['confirm_time']
        if 'instant_confirm' in d:
            o.instant_confirm = d['instant_confirm']
        return o


