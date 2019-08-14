#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KdsOrderInfoDTO(object):

    def __init__(self):
        self._biz_product = None
        self._cook_time = None
        self._dinner_area = None
        self._dinner_no = None
        self._dinner_type = None
        self._ext_info = None
        self._memo = None
        self._mobile = None
        self._order_no = None
        self._order_time = None
        self._out_order_info = None
        self._out_order_no = None
        self._partner_id = None
        self._pay_style = None
        self._schedule_time = None
        self._shop_id = None
        self._take_channel = None
        self._user_id = None

    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def cook_time(self):
        return self._cook_time

    @cook_time.setter
    def cook_time(self, value):
        self._cook_time = value
    @property
    def dinner_area(self):
        return self._dinner_area

    @dinner_area.setter
    def dinner_area(self, value):
        self._dinner_area = value
    @property
    def dinner_no(self):
        return self._dinner_no

    @dinner_no.setter
    def dinner_no(self, value):
        self._dinner_no = value
    @property
    def dinner_type(self):
        return self._dinner_type

    @dinner_type.setter
    def dinner_type(self, value):
        self._dinner_type = value
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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def out_order_info(self):
        return self._out_order_info

    @out_order_info.setter
    def out_order_info(self, value):
        self._out_order_info = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
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
    def schedule_time(self):
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, value):
        self._schedule_time = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def take_channel(self):
        return self._take_channel

    @take_channel.setter
    def take_channel(self, value):
        self._take_channel = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.cook_time:
            if hasattr(self.cook_time, 'to_alipay_dict'):
                params['cook_time'] = self.cook_time.to_alipay_dict()
            else:
                params['cook_time'] = self.cook_time
        if self.dinner_area:
            if hasattr(self.dinner_area, 'to_alipay_dict'):
                params['dinner_area'] = self.dinner_area.to_alipay_dict()
            else:
                params['dinner_area'] = self.dinner_area
        if self.dinner_no:
            if hasattr(self.dinner_no, 'to_alipay_dict'):
                params['dinner_no'] = self.dinner_no.to_alipay_dict()
            else:
                params['dinner_no'] = self.dinner_no
        if self.dinner_type:
            if hasattr(self.dinner_type, 'to_alipay_dict'):
                params['dinner_type'] = self.dinner_type.to_alipay_dict()
            else:
                params['dinner_type'] = self.dinner_type
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
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.out_order_info:
            if hasattr(self.out_order_info, 'to_alipay_dict'):
                params['out_order_info'] = self.out_order_info.to_alipay_dict()
            else:
                params['out_order_info'] = self.out_order_info
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
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
        if self.schedule_time:
            if hasattr(self.schedule_time, 'to_alipay_dict'):
                params['schedule_time'] = self.schedule_time.to_alipay_dict()
            else:
                params['schedule_time'] = self.schedule_time
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.take_channel:
            if hasattr(self.take_channel, 'to_alipay_dict'):
                params['take_channel'] = self.take_channel.to_alipay_dict()
            else:
                params['take_channel'] = self.take_channel
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KdsOrderInfoDTO()
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'cook_time' in d:
            o.cook_time = d['cook_time']
        if 'dinner_area' in d:
            o.dinner_area = d['dinner_area']
        if 'dinner_no' in d:
            o.dinner_no = d['dinner_no']
        if 'dinner_type' in d:
            o.dinner_type = d['dinner_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'memo' in d:
            o.memo = d['memo']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'out_order_info' in d:
            o.out_order_info = d['out_order_info']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_style' in d:
            o.pay_style = d['pay_style']
        if 'schedule_time' in d:
            o.schedule_time = d['schedule_time']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'take_channel' in d:
            o.take_channel = d['take_channel']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


