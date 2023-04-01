#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryActivityInfo(object):

    def __init__(self):
        self._activity_id = None
        self._activity_name = None
        self._activity_type = None
        self._bank_card_bin_list = None
        self._bank_card_type = None
        self._bank_inst_id = None
        self._bank_logo = None
        self._bank_name = None
        self._delivery_prefer_type = None
        self._discount_max_amount = None
        self._discount_max_ratio = None
        self._discount_model = None
        self._discount_threshold_amount = None
        self._discount_type = None
        self._discount_use_scene_list = None
        self._gmt_begin = None
        self._gmt_end = None
        self._voucher_template_id = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
    @property
    def activity_name(self):
        return self._activity_name

    @activity_name.setter
    def activity_name(self, value):
        self._activity_name = value
    @property
    def activity_type(self):
        return self._activity_type

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value
    @property
    def bank_card_bin_list(self):
        return self._bank_card_bin_list

    @bank_card_bin_list.setter
    def bank_card_bin_list(self, value):
        if isinstance(value, list):
            self._bank_card_bin_list = list()
            for i in value:
                self._bank_card_bin_list.append(i)
    @property
    def bank_card_type(self):
        return self._bank_card_type

    @bank_card_type.setter
    def bank_card_type(self, value):
        self._bank_card_type = value
    @property
    def bank_inst_id(self):
        return self._bank_inst_id

    @bank_inst_id.setter
    def bank_inst_id(self, value):
        self._bank_inst_id = value
    @property
    def bank_logo(self):
        return self._bank_logo

    @bank_logo.setter
    def bank_logo(self, value):
        self._bank_logo = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def delivery_prefer_type(self):
        return self._delivery_prefer_type

    @delivery_prefer_type.setter
    def delivery_prefer_type(self, value):
        self._delivery_prefer_type = value
    @property
    def discount_max_amount(self):
        return self._discount_max_amount

    @discount_max_amount.setter
    def discount_max_amount(self, value):
        self._discount_max_amount = value
    @property
    def discount_max_ratio(self):
        return self._discount_max_ratio

    @discount_max_ratio.setter
    def discount_max_ratio(self, value):
        self._discount_max_ratio = value
    @property
    def discount_model(self):
        return self._discount_model

    @discount_model.setter
    def discount_model(self, value):
        self._discount_model = value
    @property
    def discount_threshold_amount(self):
        return self._discount_threshold_amount

    @discount_threshold_amount.setter
    def discount_threshold_amount(self, value):
        self._discount_threshold_amount = value
    @property
    def discount_type(self):
        return self._discount_type

    @discount_type.setter
    def discount_type(self, value):
        self._discount_type = value
    @property
    def discount_use_scene_list(self):
        return self._discount_use_scene_list

    @discount_use_scene_list.setter
    def discount_use_scene_list(self, value):
        if isinstance(value, list):
            self._discount_use_scene_list = list()
            for i in value:
                self._discount_use_scene_list.append(i)
    @property
    def gmt_begin(self):
        return self._gmt_begin

    @gmt_begin.setter
    def gmt_begin(self, value):
        self._gmt_begin = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
        if self.activity_name:
            if hasattr(self.activity_name, 'to_alipay_dict'):
                params['activity_name'] = self.activity_name.to_alipay_dict()
            else:
                params['activity_name'] = self.activity_name
        if self.activity_type:
            if hasattr(self.activity_type, 'to_alipay_dict'):
                params['activity_type'] = self.activity_type.to_alipay_dict()
            else:
                params['activity_type'] = self.activity_type
        if self.bank_card_bin_list:
            if isinstance(self.bank_card_bin_list, list):
                for i in range(0, len(self.bank_card_bin_list)):
                    element = self.bank_card_bin_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bank_card_bin_list[i] = element.to_alipay_dict()
            if hasattr(self.bank_card_bin_list, 'to_alipay_dict'):
                params['bank_card_bin_list'] = self.bank_card_bin_list.to_alipay_dict()
            else:
                params['bank_card_bin_list'] = self.bank_card_bin_list
        if self.bank_card_type:
            if hasattr(self.bank_card_type, 'to_alipay_dict'):
                params['bank_card_type'] = self.bank_card_type.to_alipay_dict()
            else:
                params['bank_card_type'] = self.bank_card_type
        if self.bank_inst_id:
            if hasattr(self.bank_inst_id, 'to_alipay_dict'):
                params['bank_inst_id'] = self.bank_inst_id.to_alipay_dict()
            else:
                params['bank_inst_id'] = self.bank_inst_id
        if self.bank_logo:
            if hasattr(self.bank_logo, 'to_alipay_dict'):
                params['bank_logo'] = self.bank_logo.to_alipay_dict()
            else:
                params['bank_logo'] = self.bank_logo
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.delivery_prefer_type:
            if hasattr(self.delivery_prefer_type, 'to_alipay_dict'):
                params['delivery_prefer_type'] = self.delivery_prefer_type.to_alipay_dict()
            else:
                params['delivery_prefer_type'] = self.delivery_prefer_type
        if self.discount_max_amount:
            if hasattr(self.discount_max_amount, 'to_alipay_dict'):
                params['discount_max_amount'] = self.discount_max_amount.to_alipay_dict()
            else:
                params['discount_max_amount'] = self.discount_max_amount
        if self.discount_max_ratio:
            if hasattr(self.discount_max_ratio, 'to_alipay_dict'):
                params['discount_max_ratio'] = self.discount_max_ratio.to_alipay_dict()
            else:
                params['discount_max_ratio'] = self.discount_max_ratio
        if self.discount_model:
            if hasattr(self.discount_model, 'to_alipay_dict'):
                params['discount_model'] = self.discount_model.to_alipay_dict()
            else:
                params['discount_model'] = self.discount_model
        if self.discount_threshold_amount:
            if hasattr(self.discount_threshold_amount, 'to_alipay_dict'):
                params['discount_threshold_amount'] = self.discount_threshold_amount.to_alipay_dict()
            else:
                params['discount_threshold_amount'] = self.discount_threshold_amount
        if self.discount_type:
            if hasattr(self.discount_type, 'to_alipay_dict'):
                params['discount_type'] = self.discount_type.to_alipay_dict()
            else:
                params['discount_type'] = self.discount_type
        if self.discount_use_scene_list:
            if isinstance(self.discount_use_scene_list, list):
                for i in range(0, len(self.discount_use_scene_list)):
                    element = self.discount_use_scene_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_use_scene_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_use_scene_list, 'to_alipay_dict'):
                params['discount_use_scene_list'] = self.discount_use_scene_list.to_alipay_dict()
            else:
                params['discount_use_scene_list'] = self.discount_use_scene_list
        if self.gmt_begin:
            if hasattr(self.gmt_begin, 'to_alipay_dict'):
                params['gmt_begin'] = self.gmt_begin.to_alipay_dict()
            else:
                params['gmt_begin'] = self.gmt_begin
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.voucher_template_id:
            if hasattr(self.voucher_template_id, 'to_alipay_dict'):
                params['voucher_template_id'] = self.voucher_template_id.to_alipay_dict()
            else:
                params['voucher_template_id'] = self.voucher_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryActivityInfo()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'activity_name' in d:
            o.activity_name = d['activity_name']
        if 'activity_type' in d:
            o.activity_type = d['activity_type']
        if 'bank_card_bin_list' in d:
            o.bank_card_bin_list = d['bank_card_bin_list']
        if 'bank_card_type' in d:
            o.bank_card_type = d['bank_card_type']
        if 'bank_inst_id' in d:
            o.bank_inst_id = d['bank_inst_id']
        if 'bank_logo' in d:
            o.bank_logo = d['bank_logo']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'delivery_prefer_type' in d:
            o.delivery_prefer_type = d['delivery_prefer_type']
        if 'discount_max_amount' in d:
            o.discount_max_amount = d['discount_max_amount']
        if 'discount_max_ratio' in d:
            o.discount_max_ratio = d['discount_max_ratio']
        if 'discount_model' in d:
            o.discount_model = d['discount_model']
        if 'discount_threshold_amount' in d:
            o.discount_threshold_amount = d['discount_threshold_amount']
        if 'discount_type' in d:
            o.discount_type = d['discount_type']
        if 'discount_use_scene_list' in d:
            o.discount_use_scene_list = d['discount_use_scene_list']
        if 'gmt_begin' in d:
            o.gmt_begin = d['gmt_begin']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'voucher_template_id' in d:
            o.voucher_template_id = d['voucher_template_id']
        return o


