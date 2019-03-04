#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParamModel(object):

    def __init__(self):
        self._cabinet_enabled = None
        self._carry_rule = None
        self._dining_mode = None
        self._kds_display_mode = None
        self._kds_enabled = None
        self._kds_voice_call_enabled = None
        self._multi_cabinet_per_order_allowed = None
        self._open_ele = None
        self._reason_flag = None
        self._shop_id = None
        self._shop_name = None
        self._table_flag = None
        self._tail_number_rule = None
        self._takeout_auto_receipt = None

    @property
    def cabinet_enabled(self):
        return self._cabinet_enabled

    @cabinet_enabled.setter
    def cabinet_enabled(self, value):
        self._cabinet_enabled = value
    @property
    def carry_rule(self):
        return self._carry_rule

    @carry_rule.setter
    def carry_rule(self, value):
        self._carry_rule = value
    @property
    def dining_mode(self):
        return self._dining_mode

    @dining_mode.setter
    def dining_mode(self, value):
        self._dining_mode = value
    @property
    def kds_display_mode(self):
        return self._kds_display_mode

    @kds_display_mode.setter
    def kds_display_mode(self, value):
        self._kds_display_mode = value
    @property
    def kds_enabled(self):
        return self._kds_enabled

    @kds_enabled.setter
    def kds_enabled(self, value):
        self._kds_enabled = value
    @property
    def kds_voice_call_enabled(self):
        return self._kds_voice_call_enabled

    @kds_voice_call_enabled.setter
    def kds_voice_call_enabled(self, value):
        self._kds_voice_call_enabled = value
    @property
    def multi_cabinet_per_order_allowed(self):
        return self._multi_cabinet_per_order_allowed

    @multi_cabinet_per_order_allowed.setter
    def multi_cabinet_per_order_allowed(self, value):
        self._multi_cabinet_per_order_allowed = value
    @property
    def open_ele(self):
        return self._open_ele

    @open_ele.setter
    def open_ele(self, value):
        self._open_ele = value
    @property
    def reason_flag(self):
        return self._reason_flag

    @reason_flag.setter
    def reason_flag(self, value):
        self._reason_flag = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def table_flag(self):
        return self._table_flag

    @table_flag.setter
    def table_flag(self, value):
        self._table_flag = value
    @property
    def tail_number_rule(self):
        return self._tail_number_rule

    @tail_number_rule.setter
    def tail_number_rule(self, value):
        self._tail_number_rule = value
    @property
    def takeout_auto_receipt(self):
        return self._takeout_auto_receipt

    @takeout_auto_receipt.setter
    def takeout_auto_receipt(self, value):
        self._takeout_auto_receipt = value


    def to_alipay_dict(self):
        params = dict()
        if self.cabinet_enabled:
            if hasattr(self.cabinet_enabled, 'to_alipay_dict'):
                params['cabinet_enabled'] = self.cabinet_enabled.to_alipay_dict()
            else:
                params['cabinet_enabled'] = self.cabinet_enabled
        if self.carry_rule:
            if hasattr(self.carry_rule, 'to_alipay_dict'):
                params['carry_rule'] = self.carry_rule.to_alipay_dict()
            else:
                params['carry_rule'] = self.carry_rule
        if self.dining_mode:
            if hasattr(self.dining_mode, 'to_alipay_dict'):
                params['dining_mode'] = self.dining_mode.to_alipay_dict()
            else:
                params['dining_mode'] = self.dining_mode
        if self.kds_display_mode:
            if hasattr(self.kds_display_mode, 'to_alipay_dict'):
                params['kds_display_mode'] = self.kds_display_mode.to_alipay_dict()
            else:
                params['kds_display_mode'] = self.kds_display_mode
        if self.kds_enabled:
            if hasattr(self.kds_enabled, 'to_alipay_dict'):
                params['kds_enabled'] = self.kds_enabled.to_alipay_dict()
            else:
                params['kds_enabled'] = self.kds_enabled
        if self.kds_voice_call_enabled:
            if hasattr(self.kds_voice_call_enabled, 'to_alipay_dict'):
                params['kds_voice_call_enabled'] = self.kds_voice_call_enabled.to_alipay_dict()
            else:
                params['kds_voice_call_enabled'] = self.kds_voice_call_enabled
        if self.multi_cabinet_per_order_allowed:
            if hasattr(self.multi_cabinet_per_order_allowed, 'to_alipay_dict'):
                params['multi_cabinet_per_order_allowed'] = self.multi_cabinet_per_order_allowed.to_alipay_dict()
            else:
                params['multi_cabinet_per_order_allowed'] = self.multi_cabinet_per_order_allowed
        if self.open_ele:
            if hasattr(self.open_ele, 'to_alipay_dict'):
                params['open_ele'] = self.open_ele.to_alipay_dict()
            else:
                params['open_ele'] = self.open_ele
        if self.reason_flag:
            if hasattr(self.reason_flag, 'to_alipay_dict'):
                params['reason_flag'] = self.reason_flag.to_alipay_dict()
            else:
                params['reason_flag'] = self.reason_flag
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.table_flag:
            if hasattr(self.table_flag, 'to_alipay_dict'):
                params['table_flag'] = self.table_flag.to_alipay_dict()
            else:
                params['table_flag'] = self.table_flag
        if self.tail_number_rule:
            if hasattr(self.tail_number_rule, 'to_alipay_dict'):
                params['tail_number_rule'] = self.tail_number_rule.to_alipay_dict()
            else:
                params['tail_number_rule'] = self.tail_number_rule
        if self.takeout_auto_receipt:
            if hasattr(self.takeout_auto_receipt, 'to_alipay_dict'):
                params['takeout_auto_receipt'] = self.takeout_auto_receipt.to_alipay_dict()
            else:
                params['takeout_auto_receipt'] = self.takeout_auto_receipt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParamModel()
        if 'cabinet_enabled' in d:
            o.cabinet_enabled = d['cabinet_enabled']
        if 'carry_rule' in d:
            o.carry_rule = d['carry_rule']
        if 'dining_mode' in d:
            o.dining_mode = d['dining_mode']
        if 'kds_display_mode' in d:
            o.kds_display_mode = d['kds_display_mode']
        if 'kds_enabled' in d:
            o.kds_enabled = d['kds_enabled']
        if 'kds_voice_call_enabled' in d:
            o.kds_voice_call_enabled = d['kds_voice_call_enabled']
        if 'multi_cabinet_per_order_allowed' in d:
            o.multi_cabinet_per_order_allowed = d['multi_cabinet_per_order_allowed']
        if 'open_ele' in d:
            o.open_ele = d['open_ele']
        if 'reason_flag' in d:
            o.reason_flag = d['reason_flag']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'table_flag' in d:
            o.table_flag = d['table_flag']
        if 'tail_number_rule' in d:
            o.tail_number_rule = d['tail_number_rule']
        if 'takeout_auto_receipt' in d:
            o.takeout_auto_receipt = d['takeout_auto_receipt']
        return o


