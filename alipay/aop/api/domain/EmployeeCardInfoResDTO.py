#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmployeeCardWalletInfoResDTO import EmployeeCardWalletInfoResDTO


class EmployeeCardInfoResDTO(object):

    def __init__(self):
        self._employee_card_no = None
        self._employee_card_wallet_info = None

    @property
    def employee_card_no(self):
        return self._employee_card_no

    @employee_card_no.setter
    def employee_card_no(self, value):
        self._employee_card_no = value
    @property
    def employee_card_wallet_info(self):
        return self._employee_card_wallet_info

    @employee_card_wallet_info.setter
    def employee_card_wallet_info(self, value):
        if isinstance(value, EmployeeCardWalletInfoResDTO):
            self._employee_card_wallet_info = value
        else:
            self._employee_card_wallet_info = EmployeeCardWalletInfoResDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.employee_card_no:
            if hasattr(self.employee_card_no, 'to_alipay_dict'):
                params['employee_card_no'] = self.employee_card_no.to_alipay_dict()
            else:
                params['employee_card_no'] = self.employee_card_no
        if self.employee_card_wallet_info:
            if hasattr(self.employee_card_wallet_info, 'to_alipay_dict'):
                params['employee_card_wallet_info'] = self.employee_card_wallet_info.to_alipay_dict()
            else:
                params['employee_card_wallet_info'] = self.employee_card_wallet_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EmployeeCardInfoResDTO()
        if 'employee_card_no' in d:
            o.employee_card_no = d['employee_card_no']
        if 'employee_card_wallet_info' in d:
            o.employee_card_wallet_info = d['employee_card_wallet_info']
        return o


