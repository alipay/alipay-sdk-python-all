#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SettleExtendParams(object):

    def __init__(self):
        self._royalty_finish = None
        self._royalty_finish_amount = None

    @property
    def royalty_finish(self):
        return self._royalty_finish

    @royalty_finish.setter
    def royalty_finish(self, value):
        self._royalty_finish = value
    @property
    def royalty_finish_amount(self):
        return self._royalty_finish_amount

    @royalty_finish_amount.setter
    def royalty_finish_amount(self, value):
        self._royalty_finish_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalty_finish:
            if hasattr(self.royalty_finish, 'to_alipay_dict'):
                params['royalty_finish'] = self.royalty_finish.to_alipay_dict()
            else:
                params['royalty_finish'] = self.royalty_finish
        if self.royalty_finish_amount:
            if hasattr(self.royalty_finish_amount, 'to_alipay_dict'):
                params['royalty_finish_amount'] = self.royalty_finish_amount.to_alipay_dict()
            else:
                params['royalty_finish_amount'] = self.royalty_finish_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SettleExtendParams()
        if 'royalty_finish' in d:
            o.royalty_finish = d['royalty_finish']
        if 'royalty_finish_amount' in d:
            o.royalty_finish_amount = d['royalty_finish_amount']
        return o


