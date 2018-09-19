#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InteligentClauseTerm import InteligentClauseTerm
from alipay.aop.api.domain.InteligentDelayInfo import InteligentDelayInfo
from alipay.aop.api.domain.InteligentVoucherDescDetail import InteligentVoucherDescDetail
from alipay.aop.api.domain.InteligentDisplayConfig import InteligentDisplayConfig
from alipay.aop.api.domain.InteligentItemInfo import InteligentItemInfo
from alipay.aop.api.domain.InteligentUseRule import InteligentUseRule


class InteligentVoucher(object):

    def __init__(self):
        self._brand_name = None
        self._desc = None
        self._donate_flag = None
        self._effect_type = None
        self._end_time = None
        self._ext_info = None
        self._inteligent_clause_terms = None
        self._inteligent_delay_info = None
        self._inteligent_desc_detail_list = None
        self._inteligent_display_config = None
        self._inteligent_item_info = None
        self._inteligent_use_rule = None
        self._logo = None
        self._max_amount = None
        self._multi_use_mode = None
        self._name = None
        self._rate = None
        self._relative_time = None
        self._rounding_rule = None
        self._start_time = None
        self._type = None
        self._use_instructions = None
        self._validate_type = None
        self._verify_mode = None
        self._voucher_img = None
        self._voucher_note = None
        self._worth_value = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def donate_flag(self):
        return self._donate_flag

    @donate_flag.setter
    def donate_flag(self, value):
        self._donate_flag = value
    @property
    def effect_type(self):
        return self._effect_type

    @effect_type.setter
    def effect_type(self, value):
        self._effect_type = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def inteligent_clause_terms(self):
        return self._inteligent_clause_terms

    @inteligent_clause_terms.setter
    def inteligent_clause_terms(self, value):
        if isinstance(value, list):
            self._inteligent_clause_terms = list()
            for i in value:
                if isinstance(i, InteligentClauseTerm):
                    self._inteligent_clause_terms.append(i)
                else:
                    self._inteligent_clause_terms.append(InteligentClauseTerm.from_alipay_dict(i))
    @property
    def inteligent_delay_info(self):
        return self._inteligent_delay_info

    @inteligent_delay_info.setter
    def inteligent_delay_info(self, value):
        if isinstance(value, InteligentDelayInfo):
            self._inteligent_delay_info = value
        else:
            self._inteligent_delay_info = InteligentDelayInfo.from_alipay_dict(value)
    @property
    def inteligent_desc_detail_list(self):
        return self._inteligent_desc_detail_list

    @inteligent_desc_detail_list.setter
    def inteligent_desc_detail_list(self, value):
        if isinstance(value, list):
            self._inteligent_desc_detail_list = list()
            for i in value:
                if isinstance(i, InteligentVoucherDescDetail):
                    self._inteligent_desc_detail_list.append(i)
                else:
                    self._inteligent_desc_detail_list.append(InteligentVoucherDescDetail.from_alipay_dict(i))
    @property
    def inteligent_display_config(self):
        return self._inteligent_display_config

    @inteligent_display_config.setter
    def inteligent_display_config(self, value):
        if isinstance(value, InteligentDisplayConfig):
            self._inteligent_display_config = value
        else:
            self._inteligent_display_config = InteligentDisplayConfig.from_alipay_dict(value)
    @property
    def inteligent_item_info(self):
        return self._inteligent_item_info

    @inteligent_item_info.setter
    def inteligent_item_info(self, value):
        if isinstance(value, InteligentItemInfo):
            self._inteligent_item_info = value
        else:
            self._inteligent_item_info = InteligentItemInfo.from_alipay_dict(value)
    @property
    def inteligent_use_rule(self):
        return self._inteligent_use_rule

    @inteligent_use_rule.setter
    def inteligent_use_rule(self, value):
        if isinstance(value, InteligentUseRule):
            self._inteligent_use_rule = value
        else:
            self._inteligent_use_rule = InteligentUseRule.from_alipay_dict(value)
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def multi_use_mode(self):
        return self._multi_use_mode

    @multi_use_mode.setter
    def multi_use_mode(self, value):
        self._multi_use_mode = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def relative_time(self):
        return self._relative_time

    @relative_time.setter
    def relative_time(self, value):
        self._relative_time = value
    @property
    def rounding_rule(self):
        return self._rounding_rule

    @rounding_rule.setter
    def rounding_rule(self, value):
        self._rounding_rule = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def use_instructions(self):
        return self._use_instructions

    @use_instructions.setter
    def use_instructions(self, value):
        if isinstance(value, list):
            self._use_instructions = list()
            for i in value:
                self._use_instructions.append(i)
    @property
    def validate_type(self):
        return self._validate_type

    @validate_type.setter
    def validate_type(self, value):
        self._validate_type = value
    @property
    def verify_mode(self):
        return self._verify_mode

    @verify_mode.setter
    def verify_mode(self, value):
        self._verify_mode = value
    @property
    def voucher_img(self):
        return self._voucher_img

    @voucher_img.setter
    def voucher_img(self, value):
        self._voucher_img = value
    @property
    def voucher_note(self):
        return self._voucher_note

    @voucher_note.setter
    def voucher_note(self, value):
        self._voucher_note = value
    @property
    def worth_value(self):
        return self._worth_value

    @worth_value.setter
    def worth_value(self, value):
        self._worth_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.donate_flag:
            if hasattr(self.donate_flag, 'to_alipay_dict'):
                params['donate_flag'] = self.donate_flag.to_alipay_dict()
            else:
                params['donate_flag'] = self.donate_flag
        if self.effect_type:
            if hasattr(self.effect_type, 'to_alipay_dict'):
                params['effect_type'] = self.effect_type.to_alipay_dict()
            else:
                params['effect_type'] = self.effect_type
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.inteligent_clause_terms:
            if isinstance(self.inteligent_clause_terms, list):
                for i in range(0, len(self.inteligent_clause_terms)):
                    element = self.inteligent_clause_terms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteligent_clause_terms[i] = element.to_alipay_dict()
            if hasattr(self.inteligent_clause_terms, 'to_alipay_dict'):
                params['inteligent_clause_terms'] = self.inteligent_clause_terms.to_alipay_dict()
            else:
                params['inteligent_clause_terms'] = self.inteligent_clause_terms
        if self.inteligent_delay_info:
            if hasattr(self.inteligent_delay_info, 'to_alipay_dict'):
                params['inteligent_delay_info'] = self.inteligent_delay_info.to_alipay_dict()
            else:
                params['inteligent_delay_info'] = self.inteligent_delay_info
        if self.inteligent_desc_detail_list:
            if isinstance(self.inteligent_desc_detail_list, list):
                for i in range(0, len(self.inteligent_desc_detail_list)):
                    element = self.inteligent_desc_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.inteligent_desc_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.inteligent_desc_detail_list, 'to_alipay_dict'):
                params['inteligent_desc_detail_list'] = self.inteligent_desc_detail_list.to_alipay_dict()
            else:
                params['inteligent_desc_detail_list'] = self.inteligent_desc_detail_list
        if self.inteligent_display_config:
            if hasattr(self.inteligent_display_config, 'to_alipay_dict'):
                params['inteligent_display_config'] = self.inteligent_display_config.to_alipay_dict()
            else:
                params['inteligent_display_config'] = self.inteligent_display_config
        if self.inteligent_item_info:
            if hasattr(self.inteligent_item_info, 'to_alipay_dict'):
                params['inteligent_item_info'] = self.inteligent_item_info.to_alipay_dict()
            else:
                params['inteligent_item_info'] = self.inteligent_item_info
        if self.inteligent_use_rule:
            if hasattr(self.inteligent_use_rule, 'to_alipay_dict'):
                params['inteligent_use_rule'] = self.inteligent_use_rule.to_alipay_dict()
            else:
                params['inteligent_use_rule'] = self.inteligent_use_rule
        if self.logo:
            if hasattr(self.logo, 'to_alipay_dict'):
                params['logo'] = self.logo.to_alipay_dict()
            else:
                params['logo'] = self.logo
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.multi_use_mode:
            if hasattr(self.multi_use_mode, 'to_alipay_dict'):
                params['multi_use_mode'] = self.multi_use_mode.to_alipay_dict()
            else:
                params['multi_use_mode'] = self.multi_use_mode
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.rate:
            if hasattr(self.rate, 'to_alipay_dict'):
                params['rate'] = self.rate.to_alipay_dict()
            else:
                params['rate'] = self.rate
        if self.relative_time:
            if hasattr(self.relative_time, 'to_alipay_dict'):
                params['relative_time'] = self.relative_time.to_alipay_dict()
            else:
                params['relative_time'] = self.relative_time
        if self.rounding_rule:
            if hasattr(self.rounding_rule, 'to_alipay_dict'):
                params['rounding_rule'] = self.rounding_rule.to_alipay_dict()
            else:
                params['rounding_rule'] = self.rounding_rule
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.use_instructions:
            if isinstance(self.use_instructions, list):
                for i in range(0, len(self.use_instructions)):
                    element = self.use_instructions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.use_instructions[i] = element.to_alipay_dict()
            if hasattr(self.use_instructions, 'to_alipay_dict'):
                params['use_instructions'] = self.use_instructions.to_alipay_dict()
            else:
                params['use_instructions'] = self.use_instructions
        if self.validate_type:
            if hasattr(self.validate_type, 'to_alipay_dict'):
                params['validate_type'] = self.validate_type.to_alipay_dict()
            else:
                params['validate_type'] = self.validate_type
        if self.verify_mode:
            if hasattr(self.verify_mode, 'to_alipay_dict'):
                params['verify_mode'] = self.verify_mode.to_alipay_dict()
            else:
                params['verify_mode'] = self.verify_mode
        if self.voucher_img:
            if hasattr(self.voucher_img, 'to_alipay_dict'):
                params['voucher_img'] = self.voucher_img.to_alipay_dict()
            else:
                params['voucher_img'] = self.voucher_img
        if self.voucher_note:
            if hasattr(self.voucher_note, 'to_alipay_dict'):
                params['voucher_note'] = self.voucher_note.to_alipay_dict()
            else:
                params['voucher_note'] = self.voucher_note
        if self.worth_value:
            if hasattr(self.worth_value, 'to_alipay_dict'):
                params['worth_value'] = self.worth_value.to_alipay_dict()
            else:
                params['worth_value'] = self.worth_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentVoucher()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'desc' in d:
            o.desc = d['desc']
        if 'donate_flag' in d:
            o.donate_flag = d['donate_flag']
        if 'effect_type' in d:
            o.effect_type = d['effect_type']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'inteligent_clause_terms' in d:
            o.inteligent_clause_terms = d['inteligent_clause_terms']
        if 'inteligent_delay_info' in d:
            o.inteligent_delay_info = d['inteligent_delay_info']
        if 'inteligent_desc_detail_list' in d:
            o.inteligent_desc_detail_list = d['inteligent_desc_detail_list']
        if 'inteligent_display_config' in d:
            o.inteligent_display_config = d['inteligent_display_config']
        if 'inteligent_item_info' in d:
            o.inteligent_item_info = d['inteligent_item_info']
        if 'inteligent_use_rule' in d:
            o.inteligent_use_rule = d['inteligent_use_rule']
        if 'logo' in d:
            o.logo = d['logo']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'multi_use_mode' in d:
            o.multi_use_mode = d['multi_use_mode']
        if 'name' in d:
            o.name = d['name']
        if 'rate' in d:
            o.rate = d['rate']
        if 'relative_time' in d:
            o.relative_time = d['relative_time']
        if 'rounding_rule' in d:
            o.rounding_rule = d['rounding_rule']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'type' in d:
            o.type = d['type']
        if 'use_instructions' in d:
            o.use_instructions = d['use_instructions']
        if 'validate_type' in d:
            o.validate_type = d['validate_type']
        if 'verify_mode' in d:
            o.verify_mode = d['verify_mode']
        if 'voucher_img' in d:
            o.voucher_img = d['voucher_img']
        if 'voucher_note' in d:
            o.voucher_note = d['voucher_note']
        if 'worth_value' in d:
            o.worth_value = d['worth_value']
        return o


