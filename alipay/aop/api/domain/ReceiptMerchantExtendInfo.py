#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiptMerchantExtendInfo(object):

    def __init__(self):
        self._cash_register_id = None
        self._cashier_id = None
        self._cashier_name = None
        self._font_colour = None
        self._hot_line = None
        self._slogan = None
        self._ticket_record_no = None
        self._tips = None

    @property
    def cash_register_id(self):
        return self._cash_register_id

    @cash_register_id.setter
    def cash_register_id(self, value):
        self._cash_register_id = value
    @property
    def cashier_id(self):
        return self._cashier_id

    @cashier_id.setter
    def cashier_id(self, value):
        self._cashier_id = value
    @property
    def cashier_name(self):
        return self._cashier_name

    @cashier_name.setter
    def cashier_name(self, value):
        self._cashier_name = value
    @property
    def font_colour(self):
        return self._font_colour

    @font_colour.setter
    def font_colour(self, value):
        self._font_colour = value
    @property
    def hot_line(self):
        return self._hot_line

    @hot_line.setter
    def hot_line(self, value):
        self._hot_line = value
    @property
    def slogan(self):
        return self._slogan

    @slogan.setter
    def slogan(self, value):
        self._slogan = value
    @property
    def ticket_record_no(self):
        return self._ticket_record_no

    @ticket_record_no.setter
    def ticket_record_no(self, value):
        self._ticket_record_no = value
    @property
    def tips(self):
        return self._tips

    @tips.setter
    def tips(self, value):
        self._tips = value


    def to_alipay_dict(self):
        params = dict()
        if self.cash_register_id:
            if hasattr(self.cash_register_id, 'to_alipay_dict'):
                params['cash_register_id'] = self.cash_register_id.to_alipay_dict()
            else:
                params['cash_register_id'] = self.cash_register_id
        if self.cashier_id:
            if hasattr(self.cashier_id, 'to_alipay_dict'):
                params['cashier_id'] = self.cashier_id.to_alipay_dict()
            else:
                params['cashier_id'] = self.cashier_id
        if self.cashier_name:
            if hasattr(self.cashier_name, 'to_alipay_dict'):
                params['cashier_name'] = self.cashier_name.to_alipay_dict()
            else:
                params['cashier_name'] = self.cashier_name
        if self.font_colour:
            if hasattr(self.font_colour, 'to_alipay_dict'):
                params['font_colour'] = self.font_colour.to_alipay_dict()
            else:
                params['font_colour'] = self.font_colour
        if self.hot_line:
            if hasattr(self.hot_line, 'to_alipay_dict'):
                params['hot_line'] = self.hot_line.to_alipay_dict()
            else:
                params['hot_line'] = self.hot_line
        if self.slogan:
            if hasattr(self.slogan, 'to_alipay_dict'):
                params['slogan'] = self.slogan.to_alipay_dict()
            else:
                params['slogan'] = self.slogan
        if self.ticket_record_no:
            if hasattr(self.ticket_record_no, 'to_alipay_dict'):
                params['ticket_record_no'] = self.ticket_record_no.to_alipay_dict()
            else:
                params['ticket_record_no'] = self.ticket_record_no
        if self.tips:
            if hasattr(self.tips, 'to_alipay_dict'):
                params['tips'] = self.tips.to_alipay_dict()
            else:
                params['tips'] = self.tips
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiptMerchantExtendInfo()
        if 'cash_register_id' in d:
            o.cash_register_id = d['cash_register_id']
        if 'cashier_id' in d:
            o.cashier_id = d['cashier_id']
        if 'cashier_name' in d:
            o.cashier_name = d['cashier_name']
        if 'font_colour' in d:
            o.font_colour = d['font_colour']
        if 'hot_line' in d:
            o.hot_line = d['hot_line']
        if 'slogan' in d:
            o.slogan = d['slogan']
        if 'ticket_record_no' in d:
            o.ticket_record_no = d['ticket_record_no']
        if 'tips' in d:
            o.tips = d['tips']
        return o


