#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoQrcodeApplyModel(object):

    def __init__(self):
        self._biz_code = None
        self._idempotent_num = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def idempotent_num(self):
        return self._idempotent_num

    @idempotent_num.setter
    def idempotent_num(self, value):
        self._idempotent_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_code:
            if hasattr(self.biz_code, 'to_alipay_dict'):
                params['biz_code'] = self.biz_code.to_alipay_dict()
            else:
                params['biz_code'] = self.biz_code
        if self.idempotent_num:
            if hasattr(self.idempotent_num, 'to_alipay_dict'):
                params['idempotent_num'] = self.idempotent_num.to_alipay_dict()
            else:
                params['idempotent_num'] = self.idempotent_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoQrcodeApplyModel()
        if 'biz_code' in d:
            o.biz_code = d['biz_code']
        if 'idempotent_num' in d:
            o.idempotent_num = d['idempotent_num']
        return o


