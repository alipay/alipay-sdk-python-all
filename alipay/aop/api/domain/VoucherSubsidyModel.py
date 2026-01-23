#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherSubsidyModel(object):

    def __init__(self):
        self._applicable_inst_id_list = None
        self._available_count = None
        self._discount_buyer_rate = None
        self._end_date = None
        self._fee_discount_ratio = None
        self._fq_product_scene_list = None
        self._fq_subsidy_point_operation = None
        self._government_subsidy_plat_from_discount = None
        self._inst_price_code = None
        self._install_num = None
        self._min_write_off_num = None
        self._show_desc_cashier = None
        self._used_scenes = None
        self._voucher_id = None
        self._voucher_name = None
        self._voucher_product_code = None

    @property
    def applicable_inst_id_list(self):
        return self._applicable_inst_id_list

    @applicable_inst_id_list.setter
    def applicable_inst_id_list(self, value):
        if isinstance(value, list):
            self._applicable_inst_id_list = list()
            for i in value:
                self._applicable_inst_id_list.append(i)
    @property
    def available_count(self):
        return self._available_count

    @available_count.setter
    def available_count(self, value):
        self._available_count = value
    @property
    def discount_buyer_rate(self):
        return self._discount_buyer_rate

    @discount_buyer_rate.setter
    def discount_buyer_rate(self, value):
        self._discount_buyer_rate = value
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def fee_discount_ratio(self):
        return self._fee_discount_ratio

    @fee_discount_ratio.setter
    def fee_discount_ratio(self, value):
        self._fee_discount_ratio = value
    @property
    def fq_product_scene_list(self):
        return self._fq_product_scene_list

    @fq_product_scene_list.setter
    def fq_product_scene_list(self, value):
        if isinstance(value, list):
            self._fq_product_scene_list = list()
            for i in value:
                self._fq_product_scene_list.append(i)
    @property
    def fq_subsidy_point_operation(self):
        return self._fq_subsidy_point_operation

    @fq_subsidy_point_operation.setter
    def fq_subsidy_point_operation(self, value):
        self._fq_subsidy_point_operation = value
    @property
    def government_subsidy_plat_from_discount(self):
        return self._government_subsidy_plat_from_discount

    @government_subsidy_plat_from_discount.setter
    def government_subsidy_plat_from_discount(self, value):
        self._government_subsidy_plat_from_discount = value
    @property
    def inst_price_code(self):
        return self._inst_price_code

    @inst_price_code.setter
    def inst_price_code(self, value):
        self._inst_price_code = value
    @property
    def install_num(self):
        return self._install_num

    @install_num.setter
    def install_num(self, value):
        self._install_num = value
    @property
    def min_write_off_num(self):
        return self._min_write_off_num

    @min_write_off_num.setter
    def min_write_off_num(self, value):
        self._min_write_off_num = value
    @property
    def show_desc_cashier(self):
        return self._show_desc_cashier

    @show_desc_cashier.setter
    def show_desc_cashier(self, value):
        self._show_desc_cashier = value
    @property
    def used_scenes(self):
        return self._used_scenes

    @used_scenes.setter
    def used_scenes(self, value):
        self._used_scenes = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_name(self):
        return self._voucher_name

    @voucher_name.setter
    def voucher_name(self, value):
        self._voucher_name = value
    @property
    def voucher_product_code(self):
        return self._voucher_product_code

    @voucher_product_code.setter
    def voucher_product_code(self, value):
        self._voucher_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.applicable_inst_id_list:
            if isinstance(self.applicable_inst_id_list, list):
                for i in range(0, len(self.applicable_inst_id_list)):
                    element = self.applicable_inst_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.applicable_inst_id_list[i] = element.to_alipay_dict()
            if hasattr(self.applicable_inst_id_list, 'to_alipay_dict'):
                params['applicable_inst_id_list'] = self.applicable_inst_id_list.to_alipay_dict()
            else:
                params['applicable_inst_id_list'] = self.applicable_inst_id_list
        if self.available_count:
            if hasattr(self.available_count, 'to_alipay_dict'):
                params['available_count'] = self.available_count.to_alipay_dict()
            else:
                params['available_count'] = self.available_count
        if self.discount_buyer_rate:
            if hasattr(self.discount_buyer_rate, 'to_alipay_dict'):
                params['discount_buyer_rate'] = self.discount_buyer_rate.to_alipay_dict()
            else:
                params['discount_buyer_rate'] = self.discount_buyer_rate
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.fee_discount_ratio:
            if hasattr(self.fee_discount_ratio, 'to_alipay_dict'):
                params['fee_discount_ratio'] = self.fee_discount_ratio.to_alipay_dict()
            else:
                params['fee_discount_ratio'] = self.fee_discount_ratio
        if self.fq_product_scene_list:
            if isinstance(self.fq_product_scene_list, list):
                for i in range(0, len(self.fq_product_scene_list)):
                    element = self.fq_product_scene_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fq_product_scene_list[i] = element.to_alipay_dict()
            if hasattr(self.fq_product_scene_list, 'to_alipay_dict'):
                params['fq_product_scene_list'] = self.fq_product_scene_list.to_alipay_dict()
            else:
                params['fq_product_scene_list'] = self.fq_product_scene_list
        if self.fq_subsidy_point_operation:
            if hasattr(self.fq_subsidy_point_operation, 'to_alipay_dict'):
                params['fq_subsidy_point_operation'] = self.fq_subsidy_point_operation.to_alipay_dict()
            else:
                params['fq_subsidy_point_operation'] = self.fq_subsidy_point_operation
        if self.government_subsidy_plat_from_discount:
            if hasattr(self.government_subsidy_plat_from_discount, 'to_alipay_dict'):
                params['government_subsidy_plat_from_discount'] = self.government_subsidy_plat_from_discount.to_alipay_dict()
            else:
                params['government_subsidy_plat_from_discount'] = self.government_subsidy_plat_from_discount
        if self.inst_price_code:
            if hasattr(self.inst_price_code, 'to_alipay_dict'):
                params['inst_price_code'] = self.inst_price_code.to_alipay_dict()
            else:
                params['inst_price_code'] = self.inst_price_code
        if self.install_num:
            if hasattr(self.install_num, 'to_alipay_dict'):
                params['install_num'] = self.install_num.to_alipay_dict()
            else:
                params['install_num'] = self.install_num
        if self.min_write_off_num:
            if hasattr(self.min_write_off_num, 'to_alipay_dict'):
                params['min_write_off_num'] = self.min_write_off_num.to_alipay_dict()
            else:
                params['min_write_off_num'] = self.min_write_off_num
        if self.show_desc_cashier:
            if hasattr(self.show_desc_cashier, 'to_alipay_dict'):
                params['show_desc_cashier'] = self.show_desc_cashier.to_alipay_dict()
            else:
                params['show_desc_cashier'] = self.show_desc_cashier
        if self.used_scenes:
            if hasattr(self.used_scenes, 'to_alipay_dict'):
                params['used_scenes'] = self.used_scenes.to_alipay_dict()
            else:
                params['used_scenes'] = self.used_scenes
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_name:
            if hasattr(self.voucher_name, 'to_alipay_dict'):
                params['voucher_name'] = self.voucher_name.to_alipay_dict()
            else:
                params['voucher_name'] = self.voucher_name
        if self.voucher_product_code:
            if hasattr(self.voucher_product_code, 'to_alipay_dict'):
                params['voucher_product_code'] = self.voucher_product_code.to_alipay_dict()
            else:
                params['voucher_product_code'] = self.voucher_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherSubsidyModel()
        if 'applicable_inst_id_list' in d:
            o.applicable_inst_id_list = d['applicable_inst_id_list']
        if 'available_count' in d:
            o.available_count = d['available_count']
        if 'discount_buyer_rate' in d:
            o.discount_buyer_rate = d['discount_buyer_rate']
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'fee_discount_ratio' in d:
            o.fee_discount_ratio = d['fee_discount_ratio']
        if 'fq_product_scene_list' in d:
            o.fq_product_scene_list = d['fq_product_scene_list']
        if 'fq_subsidy_point_operation' in d:
            o.fq_subsidy_point_operation = d['fq_subsidy_point_operation']
        if 'government_subsidy_plat_from_discount' in d:
            o.government_subsidy_plat_from_discount = d['government_subsidy_plat_from_discount']
        if 'inst_price_code' in d:
            o.inst_price_code = d['inst_price_code']
        if 'install_num' in d:
            o.install_num = d['install_num']
        if 'min_write_off_num' in d:
            o.min_write_off_num = d['min_write_off_num']
        if 'show_desc_cashier' in d:
            o.show_desc_cashier = d['show_desc_cashier']
        if 'used_scenes' in d:
            o.used_scenes = d['used_scenes']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_name' in d:
            o.voucher_name = d['voucher_name']
        if 'voucher_product_code' in d:
            o.voucher_product_code = d['voucher_product_code']
        return o


