#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherNode(object):

    def __init__(self):
        self._amount = None
        self._award_id = None
        self._award_rule = None
        self._award_type = None
        self._camp_id = None
        self._check_number = None
        self._cost_quantity = None
        self._customize_action_url = None
        self._description = None
        self._has_apply = None
        self._has_budget = None
        self._has_check_in = None
        self._jump_url = None
        self._prize_id = None
        self._prize_type = None
        self._raffle_url = None
        self._receive_order_id = None
        self._redeem_code = None
        self._rel_biz_id = None
        self._unit = None
        self._user_can_apply = None
        self._voucher_image_url = None
        self._voucher_name = None
        self._voucher_template_id = None
        self._voucher_toast_image = None
        self._voucher_toast_title = None
        self._voucher_toast_word = None
        self._voucher_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def award_id(self):
        return self._award_id

    @award_id.setter
    def award_id(self, value):
        self._award_id = value
    @property
    def award_rule(self):
        return self._award_rule

    @award_rule.setter
    def award_rule(self, value):
        self._award_rule = value
    @property
    def award_type(self):
        return self._award_type

    @award_type.setter
    def award_type(self, value):
        self._award_type = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def check_number(self):
        return self._check_number

    @check_number.setter
    def check_number(self, value):
        self._check_number = value
    @property
    def cost_quantity(self):
        return self._cost_quantity

    @cost_quantity.setter
    def cost_quantity(self, value):
        self._cost_quantity = value
    @property
    def customize_action_url(self):
        return self._customize_action_url

    @customize_action_url.setter
    def customize_action_url(self, value):
        self._customize_action_url = value
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def has_apply(self):
        return self._has_apply

    @has_apply.setter
    def has_apply(self, value):
        self._has_apply = value
    @property
    def has_budget(self):
        return self._has_budget

    @has_budget.setter
    def has_budget(self, value):
        self._has_budget = value
    @property
    def has_check_in(self):
        return self._has_check_in

    @has_check_in.setter
    def has_check_in(self, value):
        self._has_check_in = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def raffle_url(self):
        return self._raffle_url

    @raffle_url.setter
    def raffle_url(self, value):
        self._raffle_url = value
    @property
    def receive_order_id(self):
        return self._receive_order_id

    @receive_order_id.setter
    def receive_order_id(self, value):
        self._receive_order_id = value
    @property
    def redeem_code(self):
        return self._redeem_code

    @redeem_code.setter
    def redeem_code(self, value):
        self._redeem_code = value
    @property
    def rel_biz_id(self):
        return self._rel_biz_id

    @rel_biz_id.setter
    def rel_biz_id(self, value):
        self._rel_biz_id = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value
    @property
    def user_can_apply(self):
        return self._user_can_apply

    @user_can_apply.setter
    def user_can_apply(self, value):
        self._user_can_apply = value
    @property
    def voucher_image_url(self):
        return self._voucher_image_url

    @voucher_image_url.setter
    def voucher_image_url(self, value):
        self._voucher_image_url = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value
    @property
    def voucher_toast_image(self):
        return self._voucher_toast_image

    @voucher_toast_image.setter
    def voucher_toast_image(self, value):
        self._voucher_toast_image = value
    @property
    def voucher_toast_title(self):
        return self._voucher_toast_title

    @voucher_toast_title.setter
    def voucher_toast_title(self, value):
        self._voucher_toast_title = value
    @property
    def voucher_toast_word(self):
        return self._voucher_toast_word

    @voucher_toast_word.setter
    def voucher_toast_word(self, value):
        self._voucher_toast_word = value
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.award_id:
            if hasattr(self.award_id, 'to_alipay_dict'):
                params['award_id'] = self.award_id.to_alipay_dict()
            else:
                params['award_id'] = self.award_id
        if self.award_rule:
            if hasattr(self.award_rule, 'to_alipay_dict'):
                params['award_rule'] = self.award_rule.to_alipay_dict()
            else:
                params['award_rule'] = self.award_rule
        if self.award_type:
            if hasattr(self.award_type, 'to_alipay_dict'):
                params['award_type'] = self.award_type.to_alipay_dict()
            else:
                params['award_type'] = self.award_type
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.check_number:
            if hasattr(self.check_number, 'to_alipay_dict'):
                params['check_number'] = self.check_number.to_alipay_dict()
            else:
                params['check_number'] = self.check_number
        if self.cost_quantity:
            if hasattr(self.cost_quantity, 'to_alipay_dict'):
                params['cost_quantity'] = self.cost_quantity.to_alipay_dict()
            else:
                params['cost_quantity'] = self.cost_quantity
        if self.customize_action_url:
            if hasattr(self.customize_action_url, 'to_alipay_dict'):
                params['customize_action_url'] = self.customize_action_url.to_alipay_dict()
            else:
                params['customize_action_url'] = self.customize_action_url
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.has_apply:
            if hasattr(self.has_apply, 'to_alipay_dict'):
                params['has_apply'] = self.has_apply.to_alipay_dict()
            else:
                params['has_apply'] = self.has_apply
        if self.has_budget:
            if hasattr(self.has_budget, 'to_alipay_dict'):
                params['has_budget'] = self.has_budget.to_alipay_dict()
            else:
                params['has_budget'] = self.has_budget
        if self.has_check_in:
            if hasattr(self.has_check_in, 'to_alipay_dict'):
                params['has_check_in'] = self.has_check_in.to_alipay_dict()
            else:
                params['has_check_in'] = self.has_check_in
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.raffle_url:
            if hasattr(self.raffle_url, 'to_alipay_dict'):
                params['raffle_url'] = self.raffle_url.to_alipay_dict()
            else:
                params['raffle_url'] = self.raffle_url
        if self.receive_order_id:
            if hasattr(self.receive_order_id, 'to_alipay_dict'):
                params['receive_order_id'] = self.receive_order_id.to_alipay_dict()
            else:
                params['receive_order_id'] = self.receive_order_id
        if self.redeem_code:
            if hasattr(self.redeem_code, 'to_alipay_dict'):
                params['redeem_code'] = self.redeem_code.to_alipay_dict()
            else:
                params['redeem_code'] = self.redeem_code
        if self.rel_biz_id:
            if hasattr(self.rel_biz_id, 'to_alipay_dict'):
                params['rel_biz_id'] = self.rel_biz_id.to_alipay_dict()
            else:
                params['rel_biz_id'] = self.rel_biz_id
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        if self.user_can_apply:
            if hasattr(self.user_can_apply, 'to_alipay_dict'):
                params['user_can_apply'] = self.user_can_apply.to_alipay_dict()
            else:
                params['user_can_apply'] = self.user_can_apply
        if self.voucher_image_url:
            if hasattr(self.voucher_image_url, 'to_alipay_dict'):
                params['voucher_image_url'] = self.voucher_image_url.to_alipay_dict()
            else:
                params['voucher_image_url'] = self.voucher_image_url
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_template_id:
            if hasattr(self.voucher_template_id, 'to_alipay_dict'):
                params['voucher_template_id'] = self.voucher_template_id.to_alipay_dict()
            else:
                params['voucher_template_id'] = self.voucher_template_id
        if self.voucher_toast_image:
            if hasattr(self.voucher_toast_image, 'to_alipay_dict'):
                params['voucher_toast_image'] = self.voucher_toast_image.to_alipay_dict()
            else:
                params['voucher_toast_image'] = self.voucher_toast_image
        if self.voucher_toast_title:
            if hasattr(self.voucher_toast_title, 'to_alipay_dict'):
                params['voucher_toast_title'] = self.voucher_toast_title.to_alipay_dict()
            else:
                params['voucher_toast_title'] = self.voucher_toast_title
        if self.voucher_toast_word:
            if hasattr(self.voucher_toast_word, 'to_alipay_dict'):
                params['voucher_toast_word'] = self.voucher_toast_word.to_alipay_dict()
            else:
                params['voucher_toast_word'] = self.voucher_toast_word
        if self.voucher_type:
            if hasattr(self.voucher_type, 'to_alipay_dict'):
                params['voucher_type'] = self.voucher_type.to_alipay_dict()
            else:
                params['voucher_type'] = self.voucher_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherNode()
        if 'amount' in d:
            o.amount = d['amount']
        if 'award_id' in d:
            o.award_id = d['award_id']
        if 'award_rule' in d:
            o.award_rule = d['award_rule']
        if 'award_type' in d:
            o.award_type = d['award_type']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'check_number' in d:
            o.check_number = d['check_number']
        if 'cost_quantity' in d:
            o.cost_quantity = d['cost_quantity']
        if 'customize_action_url' in d:
            o.customize_action_url = d['customize_action_url']
        if 'description' in d:
            o.description = d['description']
        if 'has_apply' in d:
            o.has_apply = d['has_apply']
        if 'has_budget' in d:
            o.has_budget = d['has_budget']
        if 'has_check_in' in d:
            o.has_check_in = d['has_check_in']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'raffle_url' in d:
            o.raffle_url = d['raffle_url']
        if 'receive_order_id' in d:
            o.receive_order_id = d['receive_order_id']
        if 'redeem_code' in d:
            o.redeem_code = d['redeem_code']
        if 'rel_biz_id' in d:
            o.rel_biz_id = d['rel_biz_id']
        if 'unit' in d:
            o.unit = d['unit']
        if 'user_can_apply' in d:
            o.user_can_apply = d['user_can_apply']
        if 'voucher_image_url' in d:
            o.voucher_image_url = d['voucher_image_url']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_template_id' in d:
            o.voucher_template_id = d['voucher_template_id']
        if 'voucher_toast_image' in d:
            o.voucher_toast_image = d['voucher_toast_image']
        if 'voucher_toast_title' in d:
            o.voucher_toast_title = d['voucher_toast_title']
        if 'voucher_toast_word' in d:
            o.voucher_toast_word = d['voucher_toast_word']
        if 'voucher_type' in d:
            o.voucher_type = d['voucher_type']
        return o


