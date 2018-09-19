#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbPosOrderDishDetail import KbPosOrderDishDetail
from alipay.aop.api.domain.PosOrderKey import PosOrderKey


class KoubeiCateringOrderInfoCreateModel(object):

    def __init__(self):
        self._business_type = None
        self._channel = None
        self._dinner_type = None
        self._dish_details = None
        self._ext_info = None
        self._memo = None
        self._operator = None
        self._order_style = None
        self._order_time = None
        self._org_dv_sn = None
        self._org_out_biz_no = None
        self._other_amount = None
        self._packing_amount = None
        self._people_num = None
        self._pos_order_key = None
        self._service_amount = None
        self._shop_id = None
        self._table_time = None
        self._take_no = None
        self._take_style = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def dinner_type(self):
        return self._dinner_type

    @dinner_type.setter
    def dinner_type(self, value):
        self._dinner_type = value
    @property
    def dish_details(self):
        return self._dish_details

    @dish_details.setter
    def dish_details(self, value):
        if isinstance(value, list):
            self._dish_details = list()
            for i in value:
                if isinstance(i, KbPosOrderDishDetail):
                    self._dish_details.append(i)
                else:
                    self._dish_details.append(KbPosOrderDishDetail.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def order_style(self):
        return self._order_style

    @order_style.setter
    def order_style(self, value):
        self._order_style = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def org_dv_sn(self):
        return self._org_dv_sn

    @org_dv_sn.setter
    def org_dv_sn(self, value):
        self._org_dv_sn = value
    @property
    def org_out_biz_no(self):
        return self._org_out_biz_no

    @org_out_biz_no.setter
    def org_out_biz_no(self, value):
        self._org_out_biz_no = value
    @property
    def other_amount(self):
        return self._other_amount

    @other_amount.setter
    def other_amount(self, value):
        self._other_amount = value
    @property
    def packing_amount(self):
        return self._packing_amount

    @packing_amount.setter
    def packing_amount(self, value):
        self._packing_amount = value
    @property
    def people_num(self):
        return self._people_num

    @people_num.setter
    def people_num(self, value):
        self._people_num = value
    @property
    def pos_order_key(self):
        return self._pos_order_key

    @pos_order_key.setter
    def pos_order_key(self, value):
        if isinstance(value, PosOrderKey):
            self._pos_order_key = value
        else:
            self._pos_order_key = PosOrderKey.from_alipay_dict(value)
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_time(self):
        return self._table_time

    @table_time.setter
    def table_time(self, value):
        self._table_time = value
    @property
    def take_no(self):
        return self._take_no

    @take_no.setter
    def take_no(self, value):
        self._take_no = value
    @property
    def take_style(self):
        return self._take_style

    @take_style.setter
    def take_style(self, value):
        self._take_style = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.dinner_type:
            if hasattr(self.dinner_type, 'to_alipay_dict'):
                params['dinner_type'] = self.dinner_type.to_alipay_dict()
            else:
                params['dinner_type'] = self.dinner_type
        if self.dish_details:
            if isinstance(self.dish_details, list):
                for i in range(0, len(self.dish_details)):
                    element = self.dish_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_details[i] = element.to_alipay_dict()
            if hasattr(self.dish_details, 'to_alipay_dict'):
                params['dish_details'] = self.dish_details.to_alipay_dict()
            else:
                params['dish_details'] = self.dish_details
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.order_style:
            if hasattr(self.order_style, 'to_alipay_dict'):
                params['order_style'] = self.order_style.to_alipay_dict()
            else:
                params['order_style'] = self.order_style
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.org_dv_sn:
            if hasattr(self.org_dv_sn, 'to_alipay_dict'):
                params['org_dv_sn'] = self.org_dv_sn.to_alipay_dict()
            else:
                params['org_dv_sn'] = self.org_dv_sn
        if self.org_out_biz_no:
            if hasattr(self.org_out_biz_no, 'to_alipay_dict'):
                params['org_out_biz_no'] = self.org_out_biz_no.to_alipay_dict()
            else:
                params['org_out_biz_no'] = self.org_out_biz_no
        if self.other_amount:
            if hasattr(self.other_amount, 'to_alipay_dict'):
                params['other_amount'] = self.other_amount.to_alipay_dict()
            else:
                params['other_amount'] = self.other_amount
        if self.packing_amount:
            if hasattr(self.packing_amount, 'to_alipay_dict'):
                params['packing_amount'] = self.packing_amount.to_alipay_dict()
            else:
                params['packing_amount'] = self.packing_amount
        if self.people_num:
            if hasattr(self.people_num, 'to_alipay_dict'):
                params['people_num'] = self.people_num.to_alipay_dict()
            else:
                params['people_num'] = self.people_num
        if self.pos_order_key:
            if hasattr(self.pos_order_key, 'to_alipay_dict'):
                params['pos_order_key'] = self.pos_order_key.to_alipay_dict()
            else:
                params['pos_order_key'] = self.pos_order_key
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.table_time:
            if hasattr(self.table_time, 'to_alipay_dict'):
                params['table_time'] = self.table_time.to_alipay_dict()
            else:
                params['table_time'] = self.table_time
        if self.take_no:
            if hasattr(self.take_no, 'to_alipay_dict'):
                params['take_no'] = self.take_no.to_alipay_dict()
            else:
                params['take_no'] = self.take_no
        if self.take_style:
            if hasattr(self.take_style, 'to_alipay_dict'):
                params['take_style'] = self.take_style.to_alipay_dict()
            else:
                params['take_style'] = self.take_style
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderInfoCreateModel()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'dinner_type' in d:
            o.dinner_type = d['dinner_type']
        if 'dish_details' in d:
            o.dish_details = d['dish_details']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'order_style' in d:
            o.order_style = d['order_style']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'org_dv_sn' in d:
            o.org_dv_sn = d['org_dv_sn']
        if 'org_out_biz_no' in d:
            o.org_out_biz_no = d['org_out_biz_no']
        if 'other_amount' in d:
            o.other_amount = d['other_amount']
        if 'packing_amount' in d:
            o.packing_amount = d['packing_amount']
        if 'people_num' in d:
            o.people_num = d['people_num']
        if 'pos_order_key' in d:
            o.pos_order_key = d['pos_order_key']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'table_time' in d:
            o.table_time = d['table_time']
        if 'take_no' in d:
            o.take_no = d['take_no']
        if 'take_style' in d:
            o.take_style = d['take_style']
        return o


