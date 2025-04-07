#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FreigtFlowAccount import FreigtFlowAccount


class AlipayCommerceLogisticsFreightflowSubaccountCreateModel(object):

    def __init__(self):
        self._logistics_code = None
        self._mode = None
        self._out_trade_no = None
        self._out_user_id = None
        self._out_user_name = None
        self._parent_info = None
        self._partner_id = None

    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def out_user_name(self):
        return self._out_user_name

    @out_user_name.setter
    def out_user_name(self, value):
        self._out_user_name = value
    @property
    def parent_info(self):
        return self._parent_info

    @parent_info.setter
    def parent_info(self, value):
        if isinstance(value, FreigtFlowAccount):
            self._parent_info = value
        else:
            self._parent_info = FreigtFlowAccount.from_alipay_dict(value)
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.out_user_name:
            if hasattr(self.out_user_name, 'to_alipay_dict'):
                params['out_user_name'] = self.out_user_name.to_alipay_dict()
            else:
                params['out_user_name'] = self.out_user_name
        if self.parent_info:
            if hasattr(self.parent_info, 'to_alipay_dict'):
                params['parent_info'] = self.parent_info.to_alipay_dict()
            else:
                params['parent_info'] = self.parent_info
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowSubaccountCreateModel()
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'out_user_name' in d:
            o.out_user_name = d['out_user_name']
        if 'parent_info' in d:
            o.parent_info = d['parent_info']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


