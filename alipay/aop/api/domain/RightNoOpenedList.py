#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RightNoOpenedList(object):

    def __init__(self):
        self._gift_prod_code = None
        self._opened = None
        self._right_no = None

    @property
    def gift_prod_code(self):
        return self._gift_prod_code

    @gift_prod_code.setter
    def gift_prod_code(self, value):
        self._gift_prod_code = value
    @property
    def opened(self):
        return self._opened

    @opened.setter
    def opened(self, value):
        self._opened = value
    @property
    def right_no(self):
        return self._right_no

    @right_no.setter
    def right_no(self, value):
        self._right_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.gift_prod_code:
            if hasattr(self.gift_prod_code, 'to_alipay_dict'):
                params['gift_prod_code'] = self.gift_prod_code.to_alipay_dict()
            else:
                params['gift_prod_code'] = self.gift_prod_code
        if self.opened:
            if hasattr(self.opened, 'to_alipay_dict'):
                params['opened'] = self.opened.to_alipay_dict()
            else:
                params['opened'] = self.opened
        if self.right_no:
            if hasattr(self.right_no, 'to_alipay_dict'):
                params['right_no'] = self.right_no.to_alipay_dict()
            else:
                params['right_no'] = self.right_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RightNoOpenedList()
        if 'gift_prod_code' in d:
            o.gift_prod_code = d['gift_prod_code']
        if 'opened' in d:
            o.opened = d['opened']
        if 'right_no' in d:
            o.right_no = d['right_no']
        return o


