#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KeyValueMap import KeyValueMap


class PrizeCustomDisplayInfo(object):

    def __init__(self):
        self._amount_unit_text = None
        self._ceil_money_amount = None
        self._discount = None
        self._ext_info = None
        self._form_type = None
        self._item_name = None
        self._max_use_count = None
        self._original_money_amount = None
        self._platform_type = None
        self._preferential_money_amount = None
        self._prize_background_pic_url = None
        self._prize_display_name = None
        self._prize_icon = None
        self._prize_item_type = None
        self._prize_logo = None
        self._prize_long_name = None
        self._prize_medium_name = None
        self._prize_merchant_name = None
        self._prize_name_without_amount = None
        self._prize_rule_desc = None
        self._prize_usage_desc = None
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
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, KeyValueMap):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(KeyValueMap.from_alipay_dict(i))
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
    def prize_background_pic_url(self):
        return self._prize_background_pic_url

    @prize_background_pic_url.setter
    def prize_background_pic_url(self, value):
        self._prize_background_pic_url = value
    @property
    def prize_display_name(self):
        return self._prize_display_name

    @prize_display_name.setter
    def prize_display_name(self, value):
        self._prize_display_name = value
    @property
    def prize_icon(self):
        return self._prize_icon

    @prize_icon.setter
    def prize_icon(self, value):
        self._prize_icon = value
    @property
    def prize_item_type(self):
        return self._prize_item_type

    @prize_item_type.setter
    def prize_item_type(self, value):
        self._prize_item_type = value
    @property
    def prize_logo(self):
        return self._prize_logo

    @prize_logo.setter
    def prize_logo(self, value):
        self._prize_logo = value
    @property
    def prize_long_name(self):
        return self._prize_long_name

    @prize_long_name.setter
    def prize_long_name(self, value):
        self._prize_long_name = value
    @property
    def prize_medium_name(self):
        return self._prize_medium_name

    @prize_medium_name.setter
    def prize_medium_name(self, value):
        self._prize_medium_name = value
    @property
    def prize_merchant_name(self):
        return self._prize_merchant_name

    @prize_merchant_name.setter
    def prize_merchant_name(self, value):
        self._prize_merchant_name = value
    @property
    def prize_name_without_amount(self):
        return self._prize_name_without_amount

    @prize_name_without_amount.setter
    def prize_name_without_amount(self, value):
        self._prize_name_without_amount = value
    @property
    def prize_rule_desc(self):
        return self._prize_rule_desc

    @prize_rule_desc.setter
    def prize_rule_desc(self, value):
        self._prize_rule_desc = value
    @property
    def prize_usage_desc(self):
        return self._prize_usage_desc

    @prize_usage_desc.setter
    def prize_usage_desc(self, value):
        self._prize_usage_desc = value
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
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
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
        if self.prize_background_pic_url:
            if hasattr(self.prize_background_pic_url, 'to_alipay_dict'):
                params['prize_background_pic_url'] = self.prize_background_pic_url.to_alipay_dict()
            else:
                params['prize_background_pic_url'] = self.prize_background_pic_url
        if self.prize_display_name:
            if hasattr(self.prize_display_name, 'to_alipay_dict'):
                params['prize_display_name'] = self.prize_display_name.to_alipay_dict()
            else:
                params['prize_display_name'] = self.prize_display_name
        if self.prize_icon:
            if hasattr(self.prize_icon, 'to_alipay_dict'):
                params['prize_icon'] = self.prize_icon.to_alipay_dict()
            else:
                params['prize_icon'] = self.prize_icon
        if self.prize_item_type:
            if hasattr(self.prize_item_type, 'to_alipay_dict'):
                params['prize_item_type'] = self.prize_item_type.to_alipay_dict()
            else:
                params['prize_item_type'] = self.prize_item_type
        if self.prize_logo:
            if hasattr(self.prize_logo, 'to_alipay_dict'):
                params['prize_logo'] = self.prize_logo.to_alipay_dict()
            else:
                params['prize_logo'] = self.prize_logo
        if self.prize_long_name:
            if hasattr(self.prize_long_name, 'to_alipay_dict'):
                params['prize_long_name'] = self.prize_long_name.to_alipay_dict()
            else:
                params['prize_long_name'] = self.prize_long_name
        if self.prize_medium_name:
            if hasattr(self.prize_medium_name, 'to_alipay_dict'):
                params['prize_medium_name'] = self.prize_medium_name.to_alipay_dict()
            else:
                params['prize_medium_name'] = self.prize_medium_name
        if self.prize_merchant_name:
            if hasattr(self.prize_merchant_name, 'to_alipay_dict'):
                params['prize_merchant_name'] = self.prize_merchant_name.to_alipay_dict()
            else:
                params['prize_merchant_name'] = self.prize_merchant_name
        if self.prize_name_without_amount:
            if hasattr(self.prize_name_without_amount, 'to_alipay_dict'):
                params['prize_name_without_amount'] = self.prize_name_without_amount.to_alipay_dict()
            else:
                params['prize_name_without_amount'] = self.prize_name_without_amount
        if self.prize_rule_desc:
            if hasattr(self.prize_rule_desc, 'to_alipay_dict'):
                params['prize_rule_desc'] = self.prize_rule_desc.to_alipay_dict()
            else:
                params['prize_rule_desc'] = self.prize_rule_desc
        if self.prize_usage_desc:
            if hasattr(self.prize_usage_desc, 'to_alipay_dict'):
                params['prize_usage_desc'] = self.prize_usage_desc.to_alipay_dict()
            else:
                params['prize_usage_desc'] = self.prize_usage_desc
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
        o = PrizeCustomDisplayInfo()
        if 'amount_unit_text' in d:
            o.amount_unit_text = d['amount_unit_text']
        if 'ceil_money_amount' in d:
            o.ceil_money_amount = d['ceil_money_amount']
        if 'discount' in d:
            o.discount = d['discount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
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
        if 'prize_background_pic_url' in d:
            o.prize_background_pic_url = d['prize_background_pic_url']
        if 'prize_display_name' in d:
            o.prize_display_name = d['prize_display_name']
        if 'prize_icon' in d:
            o.prize_icon = d['prize_icon']
        if 'prize_item_type' in d:
            o.prize_item_type = d['prize_item_type']
        if 'prize_logo' in d:
            o.prize_logo = d['prize_logo']
        if 'prize_long_name' in d:
            o.prize_long_name = d['prize_long_name']
        if 'prize_medium_name' in d:
            o.prize_medium_name = d['prize_medium_name']
        if 'prize_merchant_name' in d:
            o.prize_merchant_name = d['prize_merchant_name']
        if 'prize_name_without_amount' in d:
            o.prize_name_without_amount = d['prize_name_without_amount']
        if 'prize_rule_desc' in d:
            o.prize_rule_desc = d['prize_rule_desc']
        if 'prize_usage_desc' in d:
            o.prize_usage_desc = d['prize_usage_desc']
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


