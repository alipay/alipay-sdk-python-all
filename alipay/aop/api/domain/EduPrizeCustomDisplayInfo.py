#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EduPrizeCustomDisplayInfo(object):

    def __init__(self):
        self._amount_unit_text = None
        self._benefit_background_pic_url = None
        self._benefit_icon = None
        self._benefit_item_type = None
        self._benefit_logo = None
        self._benefit_long_name = None
        self._benefit_medium_name = None
        self._benefit_merchant_name = None
        self._benefit_name = None
        self._benefit_name_without_amount = None
        self._benefit_rule_desc = None
        self._benefit_usage_desc = None
        self._ceil_money_amount = None
        self._discount = None
        self._form_type = None
        self._item_name = None
        self._max_use_count = None
        self._original_money_amount = None
        self._platform_type = None
        self._preferential_money_amount = None
        self._promo_link = None
        self._scope = None
        self._show_amount_text = None
        self._specified_money_amount = None
        self._sub_form_type = None
        self._threshold_amount_text = None
        self._threshold_money_amount = None

    @property
    def amount_unit_text(self):
        return self._amount_unit_text

    @amount_unit_text.setter
    def amount_unit_text(self, value):
        self._amount_unit_text = value
    @property
    def benefit_background_pic_url(self):
        return self._benefit_background_pic_url

    @benefit_background_pic_url.setter
    def benefit_background_pic_url(self, value):
        self._benefit_background_pic_url = value
    @property
    def benefit_icon(self):
        return self._benefit_icon

    @benefit_icon.setter
    def benefit_icon(self, value):
        self._benefit_icon = value
    @property
    def benefit_item_type(self):
        return self._benefit_item_type

    @benefit_item_type.setter
    def benefit_item_type(self, value):
        self._benefit_item_type = value
    @property
    def benefit_logo(self):
        return self._benefit_logo

    @benefit_logo.setter
    def benefit_logo(self, value):
        self._benefit_logo = value
    @property
    def benefit_long_name(self):
        return self._benefit_long_name

    @benefit_long_name.setter
    def benefit_long_name(self, value):
        self._benefit_long_name = value
    @property
    def benefit_medium_name(self):
        return self._benefit_medium_name

    @benefit_medium_name.setter
    def benefit_medium_name(self, value):
        self._benefit_medium_name = value
    @property
    def benefit_merchant_name(self):
        return self._benefit_merchant_name

    @benefit_merchant_name.setter
    def benefit_merchant_name(self, value):
        self._benefit_merchant_name = value
    @property
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def benefit_name_without_amount(self):
        return self._benefit_name_without_amount

    @benefit_name_without_amount.setter
    def benefit_name_without_amount(self, value):
        self._benefit_name_without_amount = value
    @property
    def benefit_rule_desc(self):
        return self._benefit_rule_desc

    @benefit_rule_desc.setter
    def benefit_rule_desc(self, value):
        self._benefit_rule_desc = value
    @property
    def benefit_usage_desc(self):
        return self._benefit_usage_desc

    @benefit_usage_desc.setter
    def benefit_usage_desc(self, value):
        self._benefit_usage_desc = value
    @property
    def ceil_money_amount(self):
        return self._ceil_money_amount

    @ceil_money_amount.setter
    def ceil_money_amount(self, value):
        self._ceil_money_amount = value
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value
    @property
    def form_type(self):
        return self._form_type

    @form_type.setter
    def form_type(self, value):
        self._form_type = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def max_use_count(self):
        return self._max_use_count

    @max_use_count.setter
    def max_use_count(self, value):
        self._max_use_count = value
    @property
    def original_money_amount(self):
        return self._original_money_amount

    @original_money_amount.setter
    def original_money_amount(self, value):
        self._original_money_amount = value
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def preferential_money_amount(self):
        return self._preferential_money_amount

    @preferential_money_amount.setter
    def preferential_money_amount(self, value):
        self._preferential_money_amount = value
    @property
    def promo_link(self):
        return self._promo_link

    @promo_link.setter
    def promo_link(self, value):
        self._promo_link = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def show_amount_text(self):
        return self._show_amount_text

    @show_amount_text.setter
    def show_amount_text(self, value):
        self._show_amount_text = value
    @property
    def specified_money_amount(self):
        return self._specified_money_amount

    @specified_money_amount.setter
    def specified_money_amount(self, value):
        self._specified_money_amount = value
    @property
    def sub_form_type(self):
        return self._sub_form_type

    @sub_form_type.setter
    def sub_form_type(self, value):
        self._sub_form_type = value
    @property
    def threshold_amount_text(self):
        return self._threshold_amount_text

    @threshold_amount_text.setter
    def threshold_amount_text(self, value):
        self._threshold_amount_text = value
    @property
    def threshold_money_amount(self):
        return self._threshold_money_amount

    @threshold_money_amount.setter
    def threshold_money_amount(self, value):
        self._threshold_money_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_unit_text:
            if hasattr(self.amount_unit_text, 'to_alipay_dict'):
                params['amount_unit_text'] = self.amount_unit_text.to_alipay_dict()
            else:
                params['amount_unit_text'] = self.amount_unit_text
        if self.benefit_background_pic_url:
            if hasattr(self.benefit_background_pic_url, 'to_alipay_dict'):
                params['benefit_background_pic_url'] = self.benefit_background_pic_url.to_alipay_dict()
            else:
                params['benefit_background_pic_url'] = self.benefit_background_pic_url
        if self.benefit_icon:
            if hasattr(self.benefit_icon, 'to_alipay_dict'):
                params['benefit_icon'] = self.benefit_icon.to_alipay_dict()
            else:
                params['benefit_icon'] = self.benefit_icon
        if self.benefit_item_type:
            if hasattr(self.benefit_item_type, 'to_alipay_dict'):
                params['benefit_item_type'] = self.benefit_item_type.to_alipay_dict()
            else:
                params['benefit_item_type'] = self.benefit_item_type
        if self.benefit_logo:
            if hasattr(self.benefit_logo, 'to_alipay_dict'):
                params['benefit_logo'] = self.benefit_logo.to_alipay_dict()
            else:
                params['benefit_logo'] = self.benefit_logo
        if self.benefit_long_name:
            if hasattr(self.benefit_long_name, 'to_alipay_dict'):
                params['benefit_long_name'] = self.benefit_long_name.to_alipay_dict()
            else:
                params['benefit_long_name'] = self.benefit_long_name
        if self.benefit_medium_name:
            if hasattr(self.benefit_medium_name, 'to_alipay_dict'):
                params['benefit_medium_name'] = self.benefit_medium_name.to_alipay_dict()
            else:
                params['benefit_medium_name'] = self.benefit_medium_name
        if self.benefit_merchant_name:
            if hasattr(self.benefit_merchant_name, 'to_alipay_dict'):
                params['benefit_merchant_name'] = self.benefit_merchant_name.to_alipay_dict()
            else:
                params['benefit_merchant_name'] = self.benefit_merchant_name
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.benefit_name_without_amount:
            if hasattr(self.benefit_name_without_amount, 'to_alipay_dict'):
                params['benefit_name_without_amount'] = self.benefit_name_without_amount.to_alipay_dict()
            else:
                params['benefit_name_without_amount'] = self.benefit_name_without_amount
        if self.benefit_rule_desc:
            if hasattr(self.benefit_rule_desc, 'to_alipay_dict'):
                params['benefit_rule_desc'] = self.benefit_rule_desc.to_alipay_dict()
            else:
                params['benefit_rule_desc'] = self.benefit_rule_desc
        if self.benefit_usage_desc:
            if hasattr(self.benefit_usage_desc, 'to_alipay_dict'):
                params['benefit_usage_desc'] = self.benefit_usage_desc.to_alipay_dict()
            else:
                params['benefit_usage_desc'] = self.benefit_usage_desc
        if self.ceil_money_amount:
            if hasattr(self.ceil_money_amount, 'to_alipay_dict'):
                params['ceil_money_amount'] = self.ceil_money_amount.to_alipay_dict()
            else:
                params['ceil_money_amount'] = self.ceil_money_amount
        if self.discount:
            if hasattr(self.discount, 'to_alipay_dict'):
                params['discount'] = self.discount.to_alipay_dict()
            else:
                params['discount'] = self.discount
        if self.form_type:
            if hasattr(self.form_type, 'to_alipay_dict'):
                params['form_type'] = self.form_type.to_alipay_dict()
            else:
                params['form_type'] = self.form_type
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.max_use_count:
            if hasattr(self.max_use_count, 'to_alipay_dict'):
                params['max_use_count'] = self.max_use_count.to_alipay_dict()
            else:
                params['max_use_count'] = self.max_use_count
        if self.original_money_amount:
            if hasattr(self.original_money_amount, 'to_alipay_dict'):
                params['original_money_amount'] = self.original_money_amount.to_alipay_dict()
            else:
                params['original_money_amount'] = self.original_money_amount
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.preferential_money_amount:
            if hasattr(self.preferential_money_amount, 'to_alipay_dict'):
                params['preferential_money_amount'] = self.preferential_money_amount.to_alipay_dict()
            else:
                params['preferential_money_amount'] = self.preferential_money_amount
        if self.promo_link:
            if hasattr(self.promo_link, 'to_alipay_dict'):
                params['promo_link'] = self.promo_link.to_alipay_dict()
            else:
                params['promo_link'] = self.promo_link
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        if self.show_amount_text:
            if hasattr(self.show_amount_text, 'to_alipay_dict'):
                params['show_amount_text'] = self.show_amount_text.to_alipay_dict()
            else:
                params['show_amount_text'] = self.show_amount_text
        if self.specified_money_amount:
            if hasattr(self.specified_money_amount, 'to_alipay_dict'):
                params['specified_money_amount'] = self.specified_money_amount.to_alipay_dict()
            else:
                params['specified_money_amount'] = self.specified_money_amount
        if self.sub_form_type:
            if hasattr(self.sub_form_type, 'to_alipay_dict'):
                params['sub_form_type'] = self.sub_form_type.to_alipay_dict()
            else:
                params['sub_form_type'] = self.sub_form_type
        if self.threshold_amount_text:
            if hasattr(self.threshold_amount_text, 'to_alipay_dict'):
                params['threshold_amount_text'] = self.threshold_amount_text.to_alipay_dict()
            else:
                params['threshold_amount_text'] = self.threshold_amount_text
        if self.threshold_money_amount:
            if hasattr(self.threshold_money_amount, 'to_alipay_dict'):
                params['threshold_money_amount'] = self.threshold_money_amount.to_alipay_dict()
            else:
                params['threshold_money_amount'] = self.threshold_money_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EduPrizeCustomDisplayInfo()
        if 'amount_unit_text' in d:
            o.amount_unit_text = d['amount_unit_text']
        if 'benefit_background_pic_url' in d:
            o.benefit_background_pic_url = d['benefit_background_pic_url']
        if 'benefit_icon' in d:
            o.benefit_icon = d['benefit_icon']
        if 'benefit_item_type' in d:
            o.benefit_item_type = d['benefit_item_type']
        if 'benefit_logo' in d:
            o.benefit_logo = d['benefit_logo']
        if 'benefit_long_name' in d:
            o.benefit_long_name = d['benefit_long_name']
        if 'benefit_medium_name' in d:
            o.benefit_medium_name = d['benefit_medium_name']
        if 'benefit_merchant_name' in d:
            o.benefit_merchant_name = d['benefit_merchant_name']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'benefit_name_without_amount' in d:
            o.benefit_name_without_amount = d['benefit_name_without_amount']
        if 'benefit_rule_desc' in d:
            o.benefit_rule_desc = d['benefit_rule_desc']
        if 'benefit_usage_desc' in d:
            o.benefit_usage_desc = d['benefit_usage_desc']
        if 'ceil_money_amount' in d:
            o.ceil_money_amount = d['ceil_money_amount']
        if 'discount' in d:
            o.discount = d['discount']
        if 'form_type' in d:
            o.form_type = d['form_type']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'max_use_count' in d:
            o.max_use_count = d['max_use_count']
        if 'original_money_amount' in d:
            o.original_money_amount = d['original_money_amount']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'preferential_money_amount' in d:
            o.preferential_money_amount = d['preferential_money_amount']
        if 'promo_link' in d:
            o.promo_link = d['promo_link']
        if 'scope' in d:
            o.scope = d['scope']
        if 'show_amount_text' in d:
            o.show_amount_text = d['show_amount_text']
        if 'specified_money_amount' in d:
            o.specified_money_amount = d['specified_money_amount']
        if 'sub_form_type' in d:
            o.sub_form_type = d['sub_form_type']
        if 'threshold_amount_text' in d:
            o.threshold_amount_text = d['threshold_amount_text']
        if 'threshold_money_amount' in d:
            o.threshold_money_amount = d['threshold_money_amount']
        return o


