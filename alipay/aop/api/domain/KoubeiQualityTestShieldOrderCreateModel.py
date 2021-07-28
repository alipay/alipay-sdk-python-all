#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ShieldDishList import ShieldDishList


class KoubeiQualityTestShieldOrderCreateModel(object):

    def __init__(self):
        self._action_name = None
        self._batch_no = None
        self._cook_id = None
        self._dish_list = None
        self._ext_infos = None
        self._order_id = None
        self._out_biz_no = None
        self._partner_id = None
        self._pay_style = None
        self._shop_id = None
        self._table_no = None

    @property
    def action_name(self):
        return self._action_name

    @action_name.setter
    def action_name(self, value):
        self._action_name = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def cook_id(self):
        return self._cook_id

    @cook_id.setter
    def cook_id(self, value):
        self._cook_id = value
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, ShieldDishList):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(ShieldDishList.from_alipay_dict(i))
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_style(self):
        return self._pay_style

    @pay_style.setter
    def pay_style(self, value):
        self._pay_style = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_no(self):
        return self._table_no

    @table_no.setter
    def table_no(self, value):
        self._table_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_name:
            if hasattr(self.action_name, 'to_alipay_dict'):
                params['action_name'] = self.action_name.to_alipay_dict()
            else:
                params['action_name'] = self.action_name
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.cook_id:
            if hasattr(self.cook_id, 'to_alipay_dict'):
                params['cook_id'] = self.cook_id.to_alipay_dict()
            else:
                params['cook_id'] = self.cook_id
        if self.dish_list:
            if isinstance(self.dish_list, list):
                for i in range(0, len(self.dish_list)):
                    element = self.dish_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_list, 'to_alipay_dict'):
                params['dish_list'] = self.dish_list.to_alipay_dict()
            else:
                params['dish_list'] = self.dish_list
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_style:
            if hasattr(self.pay_style, 'to_alipay_dict'):
                params['pay_style'] = self.pay_style.to_alipay_dict()
            else:
                params['pay_style'] = self.pay_style
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.table_no:
            if hasattr(self.table_no, 'to_alipay_dict'):
                params['table_no'] = self.table_no.to_alipay_dict()
            else:
                params['table_no'] = self.table_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiQualityTestShieldOrderCreateModel()
        if 'action_name' in d:
            o.action_name = d['action_name']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'cook_id' in d:
            o.cook_id = d['cook_id']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_style' in d:
            o.pay_style = d['pay_style']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'table_no' in d:
            o.table_no = d['table_no']
        return o


