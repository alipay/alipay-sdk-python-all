#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingPassInstanceQueryModel(object):

    def __init__(self):
        self._page_num = None
        self._page_size = None
        self._pass_id = None
        self._serial_number = None
        self._tpl_id = None
        self._user_id = None

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def pass_id(self):
        return self._pass_id

    @pass_id.setter
    def pass_id(self, value):
        self._pass_id = value
    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, value):
        self._serial_number = value
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.pass_id:
            if hasattr(self.pass_id, 'to_alipay_dict'):
                params['pass_id'] = self.pass_id.to_alipay_dict()
            else:
                params['pass_id'] = self.pass_id
        if self.serial_number:
            if hasattr(self.serial_number, 'to_alipay_dict'):
                params['serial_number'] = self.serial_number.to_alipay_dict()
            else:
                params['serial_number'] = self.serial_number
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingPassInstanceQueryModel()
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'pass_id' in d:
            o.pass_id = d['pass_id']
        if 'serial_number' in d:
            o.serial_number = d['serial_number']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


