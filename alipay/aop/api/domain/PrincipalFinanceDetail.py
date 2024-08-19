#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrincipalFinanceDetail(object):

    def __init__(self):
        self._alipay_account = None
        self._biz_date = None
        self._cash_amount_format = None
        self._credit_amount_format = None
        self._cut_amount_format = None
        self._principal_name = None
        self._rebate_red_packet_amount_format = None
        self._red_packet_amount_format = None
        self._scene_type_name = None
        self._sell_mode_name = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def biz_date(self):
        return self._biz_date

    @biz_date.setter
    def biz_date(self, value):
        self._biz_date = value
    @property
    def cash_amount_format(self):
        return self._cash_amount_format

    @cash_amount_format.setter
    def cash_amount_format(self, value):
        self._cash_amount_format = value
    @property
    def credit_amount_format(self):
        return self._credit_amount_format

    @credit_amount_format.setter
    def credit_amount_format(self, value):
        self._credit_amount_format = value
    @property
    def cut_amount_format(self):
        return self._cut_amount_format

    @cut_amount_format.setter
    def cut_amount_format(self, value):
        self._cut_amount_format = value
    @property
    def principal_name(self):
        return self._principal_name

    @principal_name.setter
    def principal_name(self, value):
        self._principal_name = value
    @property
    def rebate_red_packet_amount_format(self):
        return self._rebate_red_packet_amount_format

    @rebate_red_packet_amount_format.setter
    def rebate_red_packet_amount_format(self, value):
        self._rebate_red_packet_amount_format = value
    @property
    def red_packet_amount_format(self):
        return self._red_packet_amount_format

    @red_packet_amount_format.setter
    def red_packet_amount_format(self, value):
        self._red_packet_amount_format = value
    @property
    def scene_type_name(self):
        return self._scene_type_name

    @scene_type_name.setter
    def scene_type_name(self, value):
        self._scene_type_name = value
    @property
    def sell_mode_name(self):
        return self._sell_mode_name

    @sell_mode_name.setter
    def sell_mode_name(self, value):
        self._sell_mode_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.biz_date:
            if hasattr(self.biz_date, 'to_alipay_dict'):
                params['biz_date'] = self.biz_date.to_alipay_dict()
            else:
                params['biz_date'] = self.biz_date
        if self.cash_amount_format:
            if hasattr(self.cash_amount_format, 'to_alipay_dict'):
                params['cash_amount_format'] = self.cash_amount_format.to_alipay_dict()
            else:
                params['cash_amount_format'] = self.cash_amount_format
        if self.credit_amount_format:
            if hasattr(self.credit_amount_format, 'to_alipay_dict'):
                params['credit_amount_format'] = self.credit_amount_format.to_alipay_dict()
            else:
                params['credit_amount_format'] = self.credit_amount_format
        if self.cut_amount_format:
            if hasattr(self.cut_amount_format, 'to_alipay_dict'):
                params['cut_amount_format'] = self.cut_amount_format.to_alipay_dict()
            else:
                params['cut_amount_format'] = self.cut_amount_format
        if self.principal_name:
            if hasattr(self.principal_name, 'to_alipay_dict'):
                params['principal_name'] = self.principal_name.to_alipay_dict()
            else:
                params['principal_name'] = self.principal_name
        if self.rebate_red_packet_amount_format:
            if hasattr(self.rebate_red_packet_amount_format, 'to_alipay_dict'):
                params['rebate_red_packet_amount_format'] = self.rebate_red_packet_amount_format.to_alipay_dict()
            else:
                params['rebate_red_packet_amount_format'] = self.rebate_red_packet_amount_format
        if self.red_packet_amount_format:
            if hasattr(self.red_packet_amount_format, 'to_alipay_dict'):
                params['red_packet_amount_format'] = self.red_packet_amount_format.to_alipay_dict()
            else:
                params['red_packet_amount_format'] = self.red_packet_amount_format
        if self.scene_type_name:
            if hasattr(self.scene_type_name, 'to_alipay_dict'):
                params['scene_type_name'] = self.scene_type_name.to_alipay_dict()
            else:
                params['scene_type_name'] = self.scene_type_name
        if self.sell_mode_name:
            if hasattr(self.sell_mode_name, 'to_alipay_dict'):
                params['sell_mode_name'] = self.sell_mode_name.to_alipay_dict()
            else:
                params['sell_mode_name'] = self.sell_mode_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrincipalFinanceDetail()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'biz_date' in d:
            o.biz_date = d['biz_date']
        if 'cash_amount_format' in d:
            o.cash_amount_format = d['cash_amount_format']
        if 'credit_amount_format' in d:
            o.credit_amount_format = d['credit_amount_format']
        if 'cut_amount_format' in d:
            o.cut_amount_format = d['cut_amount_format']
        if 'principal_name' in d:
            o.principal_name = d['principal_name']
        if 'rebate_red_packet_amount_format' in d:
            o.rebate_red_packet_amount_format = d['rebate_red_packet_amount_format']
        if 'red_packet_amount_format' in d:
            o.red_packet_amount_format = d['red_packet_amount_format']
        if 'scene_type_name' in d:
            o.scene_type_name = d['scene_type_name']
        if 'sell_mode_name' in d:
            o.sell_mode_name = d['sell_mode_name']
        return o


