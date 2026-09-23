#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoyagerVoucherVO(object):

    def __init__(self):
        self._active_time = None
        self._claim_time = None
        self._coupon_discount_type = None
        self._expired_time = None
        self._how_to_use = None
        self._industry = None
        self._jump_url = None
        self._label = None
        self._logo_url = None
        self._max_discount = None
        self._max_discount_unit = None
        self._name = None
        self._promo_code = None
        self._redeem_time = None
        self._status = None
        self._template_id = None
        self._threshold = None
        self._threshold_unit = None
        self._type = None
        self._use_rule = None
        self._value = None
        self._value_unit = None
        self._voucher_id = None

    @property
    def active_time(self):
        return self._active_time

    @active_time.setter
    def active_time(self, value):
        self._active_time = value
    @property
    def claim_time(self):
        return self._claim_time

    @claim_time.setter
    def claim_time(self, value):
        self._claim_time = value
    @property
    def coupon_discount_type(self):
        return self._coupon_discount_type

    @coupon_discount_type.setter
    def coupon_discount_type(self, value):
        self._coupon_discount_type = value
    @property
    def expired_time(self):
        return self._expired_time

    @expired_time.setter
    def expired_time(self, value):
        self._expired_time = value
    @property
    def how_to_use(self):
        return self._how_to_use

    @how_to_use.setter
    def how_to_use(self, value):
        self._how_to_use = value
    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value
    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label = value
    @property
    def logo_url(self):
        return self._logo_url

    @logo_url.setter
    def logo_url(self, value):
        self._logo_url = value
    @property
    def max_discount(self):
        return self._max_discount

    @max_discount.setter
    def max_discount(self, value):
        self._max_discount = value
    @property
    def max_discount_unit(self):
        return self._max_discount_unit

    @max_discount_unit.setter
    def max_discount_unit(self, value):
        self._max_discount_unit = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def promo_code(self):
        return self._promo_code

    @promo_code.setter
    def promo_code(self, value):
        self._promo_code = value
    @property
    def redeem_time(self):
        return self._redeem_time

    @redeem_time.setter
    def redeem_time(self, value):
        self._redeem_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = value
    @property
    def threshold_unit(self):
        return self._threshold_unit

    @threshold_unit.setter
    def threshold_unit(self, value):
        self._threshold_unit = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def use_rule(self):
        return self._use_rule

    @use_rule.setter
    def use_rule(self, value):
        self._use_rule = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    @property
    def value_unit(self):
        return self._value_unit

    @value_unit.setter
    def value_unit(self, value):
        self._value_unit = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.active_time:
            if hasattr(self.active_time, 'to_alipay_dict'):
                params['active_time'] = self.active_time.to_alipay_dict()
            else:
                params['active_time'] = self.active_time
        if self.claim_time:
            if hasattr(self.claim_time, 'to_alipay_dict'):
                params['claim_time'] = self.claim_time.to_alipay_dict()
            else:
                params['claim_time'] = self.claim_time
        if self.coupon_discount_type:
            if hasattr(self.coupon_discount_type, 'to_alipay_dict'):
                params['coupon_discount_type'] = self.coupon_discount_type.to_alipay_dict()
            else:
                params['coupon_discount_type'] = self.coupon_discount_type
        if self.expired_time:
            if hasattr(self.expired_time, 'to_alipay_dict'):
                params['expired_time'] = self.expired_time.to_alipay_dict()
            else:
                params['expired_time'] = self.expired_time
        if self.how_to_use:
            if hasattr(self.how_to_use, 'to_alipay_dict'):
                params['how_to_use'] = self.how_to_use.to_alipay_dict()
            else:
                params['how_to_use'] = self.how_to_use
        if self.industry:
            if hasattr(self.industry, 'to_alipay_dict'):
                params['industry'] = self.industry.to_alipay_dict()
            else:
                params['industry'] = self.industry
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.label:
            if hasattr(self.label, 'to_alipay_dict'):
                params['label'] = self.label.to_alipay_dict()
            else:
                params['label'] = self.label
        if self.logo_url:
            if hasattr(self.logo_url, 'to_alipay_dict'):
                params['logo_url'] = self.logo_url.to_alipay_dict()
            else:
                params['logo_url'] = self.logo_url
        if self.max_discount:
            if hasattr(self.max_discount, 'to_alipay_dict'):
                params['max_discount'] = self.max_discount.to_alipay_dict()
            else:
                params['max_discount'] = self.max_discount
        if self.max_discount_unit:
            if hasattr(self.max_discount_unit, 'to_alipay_dict'):
                params['max_discount_unit'] = self.max_discount_unit.to_alipay_dict()
            else:
                params['max_discount_unit'] = self.max_discount_unit
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.promo_code:
            if hasattr(self.promo_code, 'to_alipay_dict'):
                params['promo_code'] = self.promo_code.to_alipay_dict()
            else:
                params['promo_code'] = self.promo_code
        if self.redeem_time:
            if hasattr(self.redeem_time, 'to_alipay_dict'):
                params['redeem_time'] = self.redeem_time.to_alipay_dict()
            else:
                params['redeem_time'] = self.redeem_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.threshold:
            if hasattr(self.threshold, 'to_alipay_dict'):
                params['threshold'] = self.threshold.to_alipay_dict()
            else:
                params['threshold'] = self.threshold
        if self.threshold_unit:
            if hasattr(self.threshold_unit, 'to_alipay_dict'):
                params['threshold_unit'] = self.threshold_unit.to_alipay_dict()
            else:
                params['threshold_unit'] = self.threshold_unit
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.use_rule:
            if hasattr(self.use_rule, 'to_alipay_dict'):
                params['use_rule'] = self.use_rule.to_alipay_dict()
            else:
                params['use_rule'] = self.use_rule
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        if self.value_unit:
            if hasattr(self.value_unit, 'to_alipay_dict'):
                params['value_unit'] = self.value_unit.to_alipay_dict()
            else:
                params['value_unit'] = self.value_unit
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoyagerVoucherVO()
        if 'active_time' in d:
            o.active_time = d['active_time']
        if 'claim_time' in d:
            o.claim_time = d['claim_time']
        if 'coupon_discount_type' in d:
            o.coupon_discount_type = d['coupon_discount_type']
        if 'expired_time' in d:
            o.expired_time = d['expired_time']
        if 'how_to_use' in d:
            o.how_to_use = d['how_to_use']
        if 'industry' in d:
            o.industry = d['industry']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'label' in d:
            o.label = d['label']
        if 'logo_url' in d:
            o.logo_url = d['logo_url']
        if 'max_discount' in d:
            o.max_discount = d['max_discount']
        if 'max_discount_unit' in d:
            o.max_discount_unit = d['max_discount_unit']
        if 'name' in d:
            o.name = d['name']
        if 'promo_code' in d:
            o.promo_code = d['promo_code']
        if 'redeem_time' in d:
            o.redeem_time = d['redeem_time']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'threshold' in d:
            o.threshold = d['threshold']
        if 'threshold_unit' in d:
            o.threshold_unit = d['threshold_unit']
        if 'type' in d:
            o.type = d['type']
        if 'use_rule' in d:
            o.use_rule = d['use_rule']
        if 'value' in d:
            o.value = d['value']
        if 'value_unit' in d:
            o.value_unit = d['value_unit']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


