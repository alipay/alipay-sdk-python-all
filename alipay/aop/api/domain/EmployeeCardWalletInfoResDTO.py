#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EmployeeCardWalletInfoResDTO(object):

    def __init__(self):
        self._asset_type_name = None
        self._desensitize_card_no = None

    @property
    def asset_type_name(self):
        return self._asset_type_name

    @asset_type_name.setter
    def asset_type_name(self, value):
        self._asset_type_name = value
    @property
    def desensitize_card_no(self):
        return self._desensitize_card_no

    @desensitize_card_no.setter
    def desensitize_card_no(self, value):
        self._desensitize_card_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.asset_type_name:
            if hasattr(self.asset_type_name, 'to_alipay_dict'):
                params['asset_type_name'] = self.asset_type_name.to_alipay_dict()
            else:
                params['asset_type_name'] = self.asset_type_name
        if self.desensitize_card_no:
            if hasattr(self.desensitize_card_no, 'to_alipay_dict'):
                params['desensitize_card_no'] = self.desensitize_card_no.to_alipay_dict()
            else:
                params['desensitize_card_no'] = self.desensitize_card_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EmployeeCardWalletInfoResDTO()
        if 'asset_type_name' in d:
            o.asset_type_name = d['asset_type_name']
        if 'desensitize_card_no' in d:
            o.desensitize_card_no = d['desensitize_card_no']
        return o


